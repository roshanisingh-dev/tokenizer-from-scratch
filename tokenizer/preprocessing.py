import re

def load_text(file_path):
    """
    Load raw text from file
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def remove_gutenburg_metadata(text):
    """
    Remove Project Gutenberg header and footer
    """
    
    start_marker = "THE GOLDEN BIRD"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
    
    start_index = text.find(start_marker)
    end_index = text.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        return text[start_index :end_index]
    
    return text

def clean_text(text):
    """
    Clean text for tokenization
    """
    text = text.lower()  # Convert to lowercase
    
    # remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]","",text)
    
    #remove extra spaces and newlines
    text = re.sub(r"\s+"," ",text)
    return text.strip()

def tokenize_text(text):
    """
    Convert cleaned text into word tokens
    """
    return text.split()
