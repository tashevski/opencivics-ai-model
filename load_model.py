import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Method 1: Load your fine-tuned model
def load_finetuned_model(base_model_name="microsoft/Phi-4-mini-reasoning", 
                        adapter_path="policy-mini-lora-optimized-20250715_175548_final"):
    """
    Load the fine-tuned model with LoRA adapters
    Replace adapter_path with your actual output directory
    """
    print("Loading base model...")
    # Load the base model
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16,
        device_map="auto" if torch.cuda.is_available() else "cpu"
    )
    
    # Add padding token if needed
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    print("Loading LoRA adapters...")
    # Load your fine-tuned adapters
    model = PeftModel.from_pretrained(base_model, adapter_path)
    
    # Move to appropriate device
    if torch.backends.mps.is_available():
        model = model.to("mps")
    
    return model, tokenizer