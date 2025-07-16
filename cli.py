#!/usr/bin/env python3
import argparse
import sys
import os
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


def load_model(adapter_path="policy-mini-lora-optimized-20250715_180318_final"):
    """Load the fine-tuned Phi4 model with LoRA adapters"""
    base_model_name = "microsoft/Phi-4-mini-reasoning"
    
    print("Loading base model...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16,
        device_map="auto" if torch.cuda.is_available() else "cpu"
    )
    
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    print("Loading LoRA adapters...")
    script_dir = Path(__file__).parent
    adapter_full_path = script_dir / adapter_path
    
    model = PeftModel.from_pretrained(base_model, str(adapter_full_path))
    
    if torch.backends.mps.is_available():
        model = model.to("mps")
    
    return model, tokenizer


def generate_response(model, tokenizer, prompt, max_length=512, temperature=0.7):
    """Generate a response from the model"""
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    
    if torch.backends.mps.is_available():
        inputs = {k: v.to("mps") for k, v in inputs.items()}
    elif torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            temperature=temperature,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):].strip()


def interactive_mode(model, tokenizer):
    """Run in interactive mode"""
    print("Policy LLM Interactive Mode (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        try:
            prompt = input("\nEnter your prompt: ").strip()
            if prompt.lower() in ['quit', 'exit', 'q']:
                break
            if not prompt:
                continue
                
            print("\nGenerating response...")
            response = generate_response(model, tokenizer, prompt)
            print(f"\nResponse:\n{response}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="CLI for Policy LLM (Fine-tuned Phi4)")
    parser.add_argument("--prompt", "-p", type=str, help="Input prompt for generation")
    parser.add_argument("--file", "-f", type=str, help="Read prompt from file")
    parser.add_argument("--output", "-o", type=str, help="Save output to file")
    parser.add_argument("--max-length", "-m", type=int, default=512, help="Maximum generation length")
    parser.add_argument("--temperature", "-t", type=float, default=0.7, help="Sampling temperature")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")
    parser.add_argument("--adapter-path", "-a", type=str, 
                       default="policy-mini-lora-optimized-20250715_180318_final",
                       help="Path to LoRA adapter directory")
    
    args = parser.parse_args()
    
    try:
        print("Loading model...")
        model, tokenizer = load_model(args.adapter_path)
        print("Model loaded successfully!")
        
        if args.interactive:
            interactive_mode(model, tokenizer)
        elif args.prompt:
            response = generate_response(model, tokenizer, args.prompt, args.max_length, args.temperature)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(response)
                print(f"Response saved to {args.output}")
            else:
                print(f"\nResponse:\n{response}")
        elif args.file:
            if not os.path.exists(args.file):
                print(f"Error: File {args.file} not found")
                sys.exit(1)
            with open(args.file, 'r') as f:
                prompt = f.read().strip()
            response = generate_response(model, tokenizer, prompt, args.max_length, args.temperature)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(response)
                print(f"Response saved to {args.output}")
            else:
                print(f"\nResponse:\n{response}")
        else:
            print("No input provided. Use --prompt, --file, or --interactive mode.")
            parser.print_help()
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()