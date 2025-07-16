---
base_model: microsoft/Phi-4-mini-reasoning
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:microsoft/Phi-4-mini-reasoning
- lora
- transformers
- policy-analysis
- civic-tech
- government
- document-summarization
---

# OpenCivics AI Model

A specialized language model fine-tuned for policy analysis, document summarization, and civic engagement tasks. Built on Microsoft's Phi-4-mini-reasoning architecture with LoRA (Low-Rank Adaptation) fine-tuning specifically for Australian policy documents and civic technology applications.

## Quick Start

```bash
# Interactive mode
python policy_llm/cli.py --interactive

# Analyze a policy document
python policy_llm/cli.py --file policy_document.txt --output analysis.txt

# Direct prompt
python policy_llm/cli.py --prompt "Summarize the key stakeholders in this housing policy"
```

## Model Details

### Model Description

The OpenCivics AI Model is a fine-tuned version of Microsoft's Phi-4-mini-reasoning model, specifically optimized for policy analysis and civic engagement tasks. This model democratizes access to sophisticated document analysis capabilities that were previously available only to well-resourced institutions.

- **Developed by:** OpenCivics Initiative
- **Model type:** Causal Language Model (Fine-tuned with LoRA)
- **Language(s):** English (Australian policy context)
- **License:** Apache 2.0
- **Base model:** microsoft/Phi-4-mini-reasoning
- **Fine-tuning method:** LoRA (Low-Rank Adaptation)

### Model Sources

- **Repository:** [https://github.com/tashevski/opencivics-ai-model](https://github.com/tashevski/opencivics-ai-model)
- **CLI Tool:** Included in this repository
- **Base Model:** [microsoft/Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning)

## Uses

### Direct Use

The model is designed for direct use in policy analysis and civic engagement scenarios through the provided CLI tool:

- **Policy Document Analysis:** Extract key insights from legislative documents, policy papers, and government reports
- **Stakeholder Identification:** Automatically identify affected parties, decision-makers, and relevant organizations
- **Document Summarization:** Generate concise summaries of complex policy documents
- **Impact Assessment:** Analyze potential consequences of proposed policy changes
- **Interactive Analysis:** Engage in conversational analysis of civic documents

### Target Users

- **Government Agencies:** Policy analysts, legislative drafters, and public administrators
- **NGOs and Civil Society:** Community organizations analyzing policy impacts
- **Researchers:** Academic and policy researchers studying governance and public policy
- **Citizens:** Individuals seeking to understand complex policy documents
- **Journalists:** Media professionals covering government and policy developments

### Out-of-Scope Use

- **Legal Advice:** This model should not be used as a substitute for professional legal counsel
- **Real-time Decision Making:** Not suitable for time-critical emergency response decisions
- **Financial Analysis:** Not optimized for financial or economic modeling tasks
- **Medical or Health Policy:** Requires domain expertise for health-related policy analysis

## Technical Specifications

### Model Architecture

- **Base Architecture:** Phi-4-mini-reasoning (Microsoft)
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Model Format:** SafeTensors with PEFT adapters
- **Context Length:** Inherited from base model
- **Parameters:** Base model parameters + LoRA adapters

### Hardware Requirements

- **Minimum:** 8GB RAM, CPU-only inference supported
- **Recommended:** 16GB+ RAM with GPU (CUDA or MPS)
- **Supported Platforms:** 
  - CUDA (NVIDIA GPUs)
  - MPS (Apple Silicon)
  - CPU (Intel/AMD)

### Software Dependencies

```
torch>=1.9.0
transformers>=4.21.0
peft>=0.16.0
python>=3.8
```

## Installation and Usage

### Prerequisites

1. Python 3.8 or higher
2. Required Python packages (see requirements in CLI tool)

### Basic Usage

#### Interactive Mode
```bash
python policy_llm/cli.py --interactive
```

Start an interactive session where you can ask questions about policy documents in natural language.

#### File Processing
```bash
# Process a single document
python policy_llm/cli.py --file input.txt --output analysis.txt

# Batch processing with custom parameters
python policy_llm/cli.py --file policy.pdf --max-length 1024 --temperature 0.7
```

#### Direct Prompts
```bash
# Quick analysis
python policy_llm/cli.py --prompt "What are the main environmental impacts mentioned in this policy?"

# Custom generation parameters
python policy_llm/cli.py --prompt "Identify stakeholders" --temperature 0.9 --max-length 512
```

### CLI Parameters

- `--interactive` / `-i`: Start interactive mode
- `--prompt` / `-p`: Direct prompt input
- `--file` / `-f`: Input file path
- `--output` / `-o`: Output file path
- `--max-length` / `-m`: Maximum generation length (default: 512)
- `--temperature` / `-t`: Sampling temperature (default: 0.7)
- `--adapter-path` / `-a`: Custom adapter path

## Training Details

### Training Data

The model was fine-tuned on a curated dataset of Australian policy documents, including:
- Legislative texts and bills
- Policy white papers and discussion documents
- Government reports and analyses
- Consultation documents
- Regulatory frameworks

*Note: All training data consisted of publicly available government documents to ensure transparency and avoid privacy concerns.*

### Training Procedure

- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Training Framework:** PEFT (Parameter Efficient Fine-Tuning)
- **Base Model:** microsoft/Phi-4-mini-reasoning
- **Optimization:** AdamW optimizer
- **Learning Rate:** Scheduled with warmup
- **Training Duration:** Multiple epochs with validation monitoring

### Framework Versions

- **PEFT:** 0.16.1.dev0
- **Transformers:** Compatible with latest stable releases
- **PyTorch:** 1.9.0+

## Evaluation

The model has been evaluated on policy document analysis tasks including:
- Document summarization accuracy
- Stakeholder identification precision
- Policy impact assessment quality
- Response relevance and coherence

*Detailed evaluation metrics and benchmarks are available in the full technical documentation.*

## Bias, Risks, and Limitations

### Known Limitations

- **Domain Specificity:** Optimized for Australian policy context; may require adaptation for other jurisdictions
- **Document Types:** Best performance on formal policy documents; informal communications may yield variable results
- **Language:** Primarily trained on English-language documents
- **Temporal Scope:** Training data reflects policies up to the training date

### Potential Biases

- **Institutional Bias:** May reflect perspectives present in government documents
- **Temporal Bias:** Training data may not reflect the most recent policy developments
- **Language Bias:** Optimized for formal policy language rather than colloquial expressions

### Recommendations

- Always validate model outputs with domain expertise
- Use as a starting point for analysis, not a final authority
- Consider multiple perspectives when interpreting policy implications
- Regularly update with newer policy documents for optimal performance

## Environmental Impact

This model uses LoRA fine-tuning, which significantly reduces computational requirements compared to full model fine-tuning:
- **Training Efficiency:** LoRA reduces trainable parameters by ~99%
- **Inference Efficiency:** Standard inference costs with adapter overhead
- **Carbon Footprint:** Minimal additional impact beyond base model usage

## License and Usage

This model and associated CLI tool are released under the Apache 2.0 license to promote open access to policy analysis capabilities. Users are encouraged to:
- Use the model for civic and policy analysis purposes
- Contribute improvements and extensions
- Share findings that benefit the broader civic tech community
- Respect the ethical guidelines for AI use in governance contexts

## Citation

If you use this model in your research or applications, please cite:

```bibtex
@misc{opencivics-ai-model-2025,
  title={OpenCivics AI Model: A Fine-tuned Language Model for Policy Analysis},
  author={OpenCivics Initiative},
  year={2025},
  publisher={OpenCivics},
  url={https://github.com/tashevski/opencivics-ai-model}
}
```

## Support and Contact

- **Issues:** Report bugs and feature requests on GitHub
- **Documentation:** Visit the OpenCivics website for comprehensive guides
- **Community:** Join discussions about civic technology and policy analysis
- **Contact:** For inquiries about partnerships or custom applications

## Acknowledgments

- **Base Model:** Microsoft Research for the Phi-4-mini-reasoning model
- **Framework:** Hugging Face for the transformers and PEFT libraries
- **Community:** Contributors to open policy data and civic technology initiatives

---

*This model is part of the OpenCivics initiative to democratize access to advanced policy analysis tools and promote evidence-based decision-making in government and civil society.*