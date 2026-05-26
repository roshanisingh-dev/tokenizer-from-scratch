from tokenizer.vocab import build_vocab

class Tokenizer:
    def __init__(self):
        self.token_to_id = {}
        self.id_to_token = {}
        
    def fit(self, tokens):
        """
        Build vocabulary from tokens
        """
        
        self.token_to_id, self.id_to_token = build_vocab(tokens)
        
    def encode(self, text_tokens, add_special_tokens=False):
        """
        Convert tokens into token IDs
        """
        if not self.token_to_id:
            raise ValueError("Tokenizer is not fitted yet")
        
        encoded = []
        
        if add_special_tokens:
            encoded.append(self.token_to_id["<BOS>"])
            
        for token in text_tokens:
            token_id = self.token_to_id.get(token, self.token_to_id["<UNK>"])
            encoded.append(token_id)
            
        if add_special_tokens:
            encoded.append(self.token_to_id["<EOS>"])
            
        return encoded
    
    def decode(self, token_ids, skip_special_tokens=True):
        """
        Convert token IDs back into tokens
        """
        
        special_tokens = {
            "<PAD>",
            "<UNK>",
            "<BOS>",
            "<EOS>",
            "<MASK>"
        }
        
        decoded = []
        
        for token_id in token_ids:
            token = self.id_to_token.get(token_id, "<UNK>")
            
            if skip_special_tokens and token in special_tokens:
                continue
            
            decoded.append(token)
            
        return decoded
    
    def pad_sequence(self, sequences):
        """
        Pad all sequences to same length
        """
        
        max_len = max(len(seq) for seq in sequences)
        
        padded_sequences = []
        
        for seq in sequences:
            padded = seq + [self.token_to_id["<PAD>"]] * (max_len - len(seq))
            padded_sequences.append(padded)
            
        return padded_sequences
    
    def batch_encode(self, batch_tokens, add_special_tokens=True):
        """
        Encode multiple token lists
        """
        
        encoded_batch = []
        
        for tokens in batch_tokens:
            encoded = self.encode(tokens, add_special_tokens=add_special_tokens)
            encoded_batch.append(encoded)
            
        return self.pad_sequence(encoded_batch)
    
    def create_attention_mask(self, padded_sequences):
        masks = []
        
        for seq in padded_sequences:
            mask = []
            
            for token_id in seq:
                if token_id == self.token_to_id["<PAD>"]:
                    mask.append(0)
                else:
                    mask.append(1)
                    
            masks.append(mask)
            
        return masks
    
    def batch_decode(self, batch_ids):
        decoded_batch = []
        
        for seq in batch_ids:
            decoded = self.decode(seq)
            decoded_batch.append(decoded)
            
        return decoded_batch
        
                