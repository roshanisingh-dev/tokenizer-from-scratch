from collections import Counter
import json

SPECIAL_TOKENS = {
    "<PAD>": 0,
    "<UNK>": 1,
    "<BOS>": 2,
    "<EOS>": 3,
    "<MASK>": 4
}

def build_vocab(tokens):
    """
    Build vocabulary mappings
    """
    
    token_counts = Counter(tokens)
    
    token_to_id = SPECIAL_TOKENS.copy()
    current_index = len(SPECIAL_TOKENS)
    
    for token in token_counts:
        if token not in token_to_id:
            token_to_id[token] = current_index
            current_index += 1
            
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    
    return token_to_id, id_to_token

def save_vocab(token_to_id, file_path):
    """
    Save vocabulary as JSON
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(token_to_id, file, indent=4)
        
def load_vocab(file_path):
    """
    Load vocabulary from JSON
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        token_to_id = json.load(file)
        
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    
    return token_to_id, id_to_token