# Tokenizer From Scratch

A custom word-level tokenizer built completely from scratch in Python as part of learning Large Language Model (LLM) internals. This project demonstrates how raw text is transformed into numerical token representations suitable for transformer-based architectures.

The tokenizer is built using **Grimm’s Fairy Tales** from **Project Gutenberg** and includes preprocessing, vocabulary generation, token encoding/decoding, batch processing, sequence padding, and attention mask generation.

---

## Features

### Text Preprocessing
- Load raw text dataset
- Remove Project Gutenberg metadata/header/footer
- Clean and normalize text
- Tokenize text into words

### Vocabulary Management
- Build custom vocabulary from dataset
- Token-to-ID mapping
- ID-to-token mapping

### Special Tokens
Implemented commonly used special tokens:

| Token | Purpose |
|------|---------|
| `<PAD>` | Padding shorter sequences |
| `<UNK>` | Unknown/out-of-vocabulary tokens |
| `<BOS>` | Beginning of sequence |
| `<EOS>` | End of sequence |
| `<MASK>` | Mask token for masked language modeling |

### Tokenizer Operations
- Single sentence encoding
- Single sentence decoding
- Batch encoding
- Batch decoding
- Automatic sequence padding
- Attention mask generation

---

## Dataset Used

**Dataset:** Grimm’s Fairy Tales  
**Source:** Project Gutenberg

This dataset was chosen because:
- Publicly available
- English natural language corpus
- Suitable size for tokenizer experimentation
- Story-based realistic textual data

Dataset location in project:

```text
data/grimm_fairy_tales.txt
```

---

## Project Structure

```text
tokenizer-from-scratch/
│
├── data/
│   └── grimm_fairy_tales.txt
│
├── tokenizer/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── vocab.py
│   └── tokenizer.py
│
├── tests/
│   └── test_tokenizer.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Sample Output

### Encoded Batch

```python
[
    [2, 5, 6, 7, 3],
    [2, 8, 9, 3, 0],
    [2, 1, 7, 3, 0]
]
```

Explanation:

- `2` → `<BOS>`
- `3` → `<EOS>`
- `0` → `<PAD>`
- `1` → `<UNK>`

---

### Decoded Batch

```python
[
    ['the', 'golden', 'bird'],
    ['queen', 'bee'],
    ['bird']
]
```

---

### Attention Masks

```python
[
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]
```

Where:

- `1` = actual token
- `0` = padding token

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/roshanisingh-dev/tokenizer-from-scratch.git
cd tokenizer-from-scratch
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate virtual environment:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run tokenizer test:

```bash
python tests/test_tokenizer.py
```

---

## Learning Objectives

This project was built to understand the foundational concepts behind tokenization in LLM pipelines, including:

- Text preprocessing
- Vocabulary construction
- Numerical token representation
- Sequence padding
- Attention masking
- Batch token processing

This serves as a foundational step toward implementing transformer architectures from scratch.

---

## Future Improvements

Potential future enhancements:

- Byte Pair Encoding (BPE)
- WordPiece tokenizer
- SentencePiece tokenizer
- Vocabulary save/load support
- Token frequency statistics
- Configurable tokenizer settings

---

## Tech Stack

- Python
- Standard Python libraries
- VS Code
- Git & GitHub

---

## Author

**Roshani Singh**

Built as part of learning **LLM Engineering / Transformer internals from scratch**.