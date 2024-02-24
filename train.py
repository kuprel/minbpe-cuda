"""
Train BasicTokenizer on some data with PyTorch/CUDA
"""

import os
import time
import torch
from minbpe import BasicTokenizer

# open some text and train a vocab of 512 tokens
text = open("taylorswift.txt", "r", encoding="utf-8").read()
# text = 'aaabdaaabac'

# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()

# construct the Tokenizer object and kick off verbose training
tokenizer = BasicTokenizer()
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Training with {device}")
tokenizer.train(text, 512, verbose=True, device=device)
# writes two files in the models directory: name.model, and name.vocab
prefix = os.path.join("models", "basic")
tokenizer.save(prefix)

t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")

print("Testing the model")
assert(tokenizer.decode(tokenizer.encode(text)) == text)
print("Success")

print("Testing save/load")
tok = BasicTokenizer()
tok.load(prefix + ".model")
assert(tok.decode(tok.encode(text)) == text)
print("Success")