import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tokenizer.preprocessing import (
    load_text,
    remove_gutenburg_metadata,
    clean_text,
    tokenize_text
)

from tokenizer.tokenizer import Tokenizer

text = load_text("data/grimm_fairy_tales.txt")
text = remove_gutenburg_metadata(text)
text = clean_text(text)
tokens = tokenize_text(text)

tok = Tokenizer()
tok.fit(tokens)

batch = [
    ["the", "golden", "bird"],
    ["queen", "bee"],
    ["unknownword", "bird"]
]

encoded_batch = tok.batch_encode(batch)
attention_masks = tok.create_attention_mask(encoded_batch)
decoded_batch = tok.batch_decode(encoded_batch)

print("Encoded batch:",encoded_batch)
print("Decoded batch:", decoded_batch)
print("Attention masks:", attention_masks)