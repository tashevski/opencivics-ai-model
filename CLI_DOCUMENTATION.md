# OpenCivics AI Model - CLI Documentation

Comprehensive guide for using the OpenCivics AI Model command-line interface for policy analysis, document summarization, and civic engagement tasks.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command Reference](#command-reference)
- [Usage Modes](#usage-modes)
- [Practical Examples](#practical-examples)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Installation

### Prerequisites

Ensure you have Python 3.8+ installed and the required dependencies:

```bash
pip install torch transformers peft
```

### Verify Installation

Check that the CLI tool is accessible:

```bash
python policy_llm/cli.py --help
```

## Quick Start

### Basic Commands

```bash
# Interactive mode - start a conversation with the AI
python policy_llm/cli.py --interactive

# Analyze a single document
python policy_llm/cli.py --file document.txt

# Quick prompt analysis
python policy_llm/cli.py --prompt "Summarize the key policy changes"

# Save output to file
python policy_llm/cli.py --prompt "Identify stakeholders" --output results.txt
```

## Command Reference

### Syntax

```bash
python policy_llm/cli.py [MODE] [OPTIONS]
```

### Modes

| Mode | Short | Description |
|------|-------|-------------|
| `--interactive` | `-i` | Start interactive conversation mode |
| `--prompt TEXT` | `-p TEXT` | Process a direct text prompt |
| `--file PATH` | `-f PATH` | Analyze a document from file |

### Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--output PATH` | `-o PATH` | string | stdout | Save output to specified file |
| `--max-length NUM` | `-m NUM` | integer | 512 | Maximum generation length |
| `--temperature NUM` | `-t NUM` | float | 0.7 | Sampling temperature (0.1-2.0) |
| `--adapter-path PATH` | `-a PATH` | string | default | Custom LoRA adapter directory |
| `--help` | `-h` | - | - | Show help message |

### Parameter Details

#### Temperature (`--temperature`)
- **Range:** 0.1 - 2.0
- **Low (0.1-0.3):** More focused, deterministic responses
- **Medium (0.7-0.9):** Balanced creativity and coherence (recommended)
- **High (1.0-2.0):** More creative but potentially less coherent

#### Max Length (`--max-length`)
- **Range:** 50 - 2048 tokens
- **Short (50-256):** Brief summaries and quick answers
- **Medium (512-1024):** Detailed analysis (recommended)
- **Long (1024-2048):** Comprehensive reports

## Usage Modes

### 1. Interactive Mode

Start a conversational session with the AI model.

```bash
python policy_llm/cli.py --interactive
```

**Features:**
- Natural language conversation
- Follow-up questions
- Context awareness within session
- Exit with `quit`, `exit`, or `q`

**Example Session:**
```
$ python policy_llm/cli.py --interactive

Policy LLM Interactive Mode (type 'quit' to exit)
--------------------------------------------------

Enter your prompt: What are the main objectives of this environmental policy?

Generating response...

Response:
The environmental policy outlines three main objectives:
1. Reduce carbon emissions by 30% by 2030
2. Protect biodiversity through habitat conservation
3. Promote sustainable resource management

Enter your prompt: Who would be responsible for implementing these objectives?

Generating response...

Response:
Implementation responsibility would fall to several key stakeholders:
- Department of Environment and Energy (lead agency)
- State and territory environmental agencies
- Local government councils
- Industry bodies and private sector partners
```

### 2. File Processing Mode

Analyze documents from files (supports .txt, .md, and other text formats).

```bash
python policy_llm/cli.py --file path/to/document.txt
```

**Supported Formats:**
- Plain text (.txt)
- Markdown (.md)
- Policy documents
- Reports and papers

**Example:**
```bash
# Analyze a policy document
python policy_llm/cli.py --file housing_policy_2024.txt --output analysis.txt

# Process with custom parameters
python policy_llm/cli.py --file legislation.txt --max-length 1024 --temperature 0.5
```

### 3. Direct Prompt Mode

Process specific questions or analysis requests.

```bash
python policy_llm/cli.py --prompt "Your question here"
```

**Example:**
```bash
# Quick stakeholder analysis
python policy_llm/cli.py --prompt "Identify the main stakeholders affected by this healthcare reform"

# Policy impact assessment
python policy_llm/cli.py --prompt "What are the potential economic impacts of this taxation policy?"
```

## Practical Examples

### Policy Document Analysis

#### Comprehensive Document Review
```bash
python policy_llm/cli.py --file policy_document.txt \
  --prompt "Provide a comprehensive analysis including: 1) Key objectives, 2) Main stakeholders, 3) Implementation timeline, 4) Potential challenges" \
  --max-length 1024 \
  --output full_analysis.txt
```

#### Quick Summary
```bash
python policy_llm/cli.py --file long_report.txt \
  --prompt "Summarize this document in 3 key points" \
  --max-length 256
```

### Stakeholder Analysis

#### Identify Affected Parties
```bash
python policy_llm/cli.py --prompt "Who would be most affected by this proposed change to education funding?" \
  --temperature 0.5 \
  --output stakeholders.txt
```

#### Impact Assessment
```bash
python policy_llm/cli.py --file urban_planning_proposal.txt \
  --prompt "Analyze the potential impacts on different community groups" \
  --max-length 800
```

### Legislative Analysis

#### Bill Summary
```bash
python policy_llm/cli.py --file senate_bill_123.txt \
  --prompt "Summarize the key provisions and their implications" \
  --max-length 600 \
  --temperature 0.6
```

#### Amendment Comparison
```bash
python policy_llm/cli.py --interactive
# Then: "Compare the original bill with the proposed amendments. What are the main changes?"
```

### Batch Processing Workflow

Process multiple documents systematically:

```bash
#!/bin/bash
# Process multiple policy documents

for file in policies/*.txt; do
    echo "Processing $file..."
    python policy_llm/cli.py --file "$file" \
      --prompt "Provide a 3-sentence summary of key points" \
      --output "summaries/$(basename "$file" .txt)_summary.txt"
done
```

## Configuration

### Custom Adapter Path

Use a different model adapter:

```bash
python policy_llm/cli.py --adapter-path /path/to/custom/adapter --interactive
```

### Environment Variables

Set default parameters using environment variables:

```bash
# Set default temperature
export POLICY_LLM_TEMPERATURE=0.8

# Set default max length
export POLICY_LLM_MAX_LENGTH=1024

# Use in CLI
python policy_llm/cli.py --prompt "Analyze this policy"
```

### Configuration File

Create a `config.json` for default settings:

```json
{
    "temperature": 0.7,
    "max_length": 512,
    "adapter_path": "policy-mini-lora-optimized-20250715_180318_final"
}
```

## Troubleshooting

### Common Issues

#### Model Loading Errors

**Problem:** "Error loading model" or CUDA/MPS errors
```bash
# Solution: Use CPU-only mode
CUDA_VISIBLE_DEVICES="" python policy_llm/cli.py --interactive
```

**Problem:** Out of memory errors
```bash
# Solution: Reduce max_length or use CPU
python policy_llm/cli.py --prompt "Your prompt" --max-length 256
```

#### File Processing Issues

**Problem:** "File not found" error
```bash
# Check file path (use absolute paths)
python policy_llm/cli.py --file /full/path/to/document.txt
```

**Problem:** Empty or garbled output
```bash
# Check file encoding and format
file document.txt  # Check file type
python policy_llm/cli.py --file document.txt --temperature 0.5 --max-length 800
```

#### Performance Issues

**Problem:** Slow response times
```bash
# Use GPU acceleration if available
python policy_llm/cli.py --interactive  # Auto-detects GPU

# Reduce max_length for faster responses
python policy_llm/cli.py --prompt "Quick summary" --max-length 256
```

### Debug Mode

Enable verbose logging:

```bash
# Add debug output
python -u policy_llm/cli.py --interactive 2>&1 | tee debug.log
```

### Hardware Requirements

| Configuration | RAM | Processing | Response Time |
|---------------|-----|------------|---------------|
| Minimum (CPU) | 8GB | CPU-only | 10-30 seconds |
| Recommended (GPU) | 16GB | CUDA/MPS | 2-5 seconds |
| Optimal | 32GB+ | High-end GPU | 1-2 seconds |

## Best Practices

### Prompt Engineering

#### Effective Prompts
```bash
# Good: Specific and clear
python policy_llm/cli.py --prompt "Identify the three main stakeholders affected by this housing policy and explain their interests"

# Better: Structured request
python policy_llm/cli.py --prompt "Analyze this policy document and provide: 1) Summary of key objectives, 2) List of affected stakeholders, 3) Implementation challenges, 4) Recommended next steps"
```

#### Prompt Guidelines
- **Be specific:** Ask for particular types of analysis
- **Use structure:** Request numbered lists or specific formats
- **Provide context:** Include relevant background information
- **Set scope:** Define the level of detail needed

### Parameter Optimization

#### Temperature Settings by Task
- **Factual Analysis:** 0.3-0.5 (more deterministic)
- **Creative Policy Solutions:** 0.7-0.9 (balanced)
- **Exploratory Questions:** 0.8-1.2 (more creative)

#### Length Settings by Output Type
- **Quick summaries:** 128-256 tokens
- **Detailed analysis:** 512-1024 tokens
- **Comprehensive reports:** 1024-2048 tokens

### Workflow Recommendations

#### 1. Document Review Workflow
```bash
# Step 1: Quick overview
python policy_llm/cli.py --file document.txt --prompt "Provide a 2-sentence overview" --max-length 128

# Step 2: Detailed analysis
python policy_llm/cli.py --file document.txt --prompt "Detailed stakeholder analysis" --max-length 800

# Step 3: Interactive follow-up
python policy_llm/cli.py --interactive
# Ask specific follow-up questions
```

#### 2. Comparative Analysis
```bash
# Analyze multiple documents
python policy_llm/cli.py --file policy_v1.txt --prompt "Key features of this policy" --output v1_features.txt
python policy_llm/cli.py --file policy_v2.txt --prompt "Key features of this policy" --output v2_features.txt

# Compare in interactive mode
python policy_llm/cli.py --interactive
# Load both analyses and ask for comparison
```

### Quality Assurance

#### Validation Checklist
- [ ] Review outputs for accuracy
- [ ] Cross-reference with source documents
- [ ] Verify stakeholder identifications
- [ ] Check for potential biases
- [ ] Validate technical terminology

#### Output Review
Always review AI-generated analysis with domain expertise:
- Use as starting point, not final authority
- Verify factual claims independently
- Consider multiple perspectives
- Document sources and methodology

## Advanced Usage

### Custom Analysis Templates

Create reusable prompt templates:

```bash
# Policy impact template
IMPACT_TEMPLATE="Analyze this policy for: 1) Economic impacts, 2) Social implications, 3) Environmental effects, 4) Implementation challenges"

python policy_llm/cli.py --file policy.txt --prompt "$IMPACT_TEMPLATE"
```

### Integration with Other Tools

#### Export to Different Formats
```bash
# Generate markdown report
python policy_llm/cli.py --file policy.txt --prompt "Create a markdown-formatted analysis report" --output report.md

# Generate CSV data
python policy_llm/cli.py --file data.txt --prompt "Extract key data points in CSV format" --output data.csv
```

#### Pipeline Integration
```bash
# Use in shell pipelines
echo "Policy text here" | python policy_llm/cli.py --prompt "Analyze this text"

# Process and format
python policy_llm/cli.py --file input.txt --prompt "Analysis" | tee analysis.txt | grep "Stakeholder"
```

## Support and Resources

### Getting Help
- Use `--help` flag for quick reference
- Check error messages for specific guidance
- Review this documentation for detailed examples
- Report issues on GitHub repository

### Community Resources
- OpenCivics website for additional guides
- GitHub discussions for community support
- Example notebooks and tutorials
- Best practices documentation

### Updates and Maintenance
- Check for model updates regularly
- Update dependencies as needed
- Review new CLI features in releases
- Backup important configurations

---

*This CLI documentation is part of the OpenCivics AI Model project. For the latest updates and additional resources, visit the project repository.*