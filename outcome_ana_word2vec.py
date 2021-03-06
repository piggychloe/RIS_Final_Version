"""
Created on 3/24/22

@author: qinyuzhu
"""

import re
import io
import string

import tensorboard
import tqdm
import pandas as pd
import numpy as np
import tensorflow as tf
# from tensorflow.keras import layers
#
# %load_ext tensorboard

SEED = 42
AUTOTUNE = tf.data.AUTOTUNE

sentence = "In 2006 I wrote a paper on- about how the border becomes carried by the body.technology twins immigration control with policing of women’s bodies. It will drive the most vulnerable to the riskiest spaces."
tokens = list(sentence.lower().split())
print(len(tokens))

vocab, index = {}, 1  # start indexing from 1
vocab['<pad>'] = 0  # add a padding token
for token in tokens:
  if token not in vocab:
    vocab[token] = index
    index += 1
vocab_size = len(vocab)
print(vocab)

inverse_vocab = {index: token for token, index in vocab.items()}
print(inverse_vocab)

example_sequence = [vocab[word] for word in tokens]
print(example_sequence)

window_size = 2
positive_skip_grams, _ = tf.keras.preprocessing.sequence.skipgrams(
      example_sequence,
      vocabulary_size=vocab_size,
      window_size=window_size,
      negative_samples=0)
print(len(positive_skip_grams))

for target, context in positive_skip_grams[:5]:
  print(f"({target}, {context}): ({inverse_vocab[target]}, {inverse_vocab[context]})")





if __name__ == '__main__':
    pass
