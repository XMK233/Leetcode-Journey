# 1. [random-nnlm-en-dim128@v1](https://aihub.cloud.google.com/p/products%2Fa52e9466-f691-4f91-a62e-f6e39eb967f8)
## Overview

Text embedding initialized with `tf.random_normal([vocabulary_size, 128])`. It
contains no "knowledge", but can conveniently be used as a baseline when
comparing to other modules.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/random-nnlm-en-dim128/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Vocabulary of the module is based on
[nnlm-en-dim128](https://tfhub.dev/google/nnlm-en-dim128/1).

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens from the original vocabulary (~2.5%)
are **replaced by hash buckets**, initialized also randomly and from the same
distribution.
---------
# 2. [random-nnlm-en-dim50@v1](https://aihub.cloud.google.com/p/products%2Fb0766fd5-82b5-48e3-9d6f-26c5d2601d5f)
## Overview

Text embedding initialized with `tf.random_normal([vocabulary_size, 50])`. It
contains no "knowledge", but can conveniently be used as a baseline when
comparing to other modules.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/random-nnlm-en-dim50/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Vocabulary of the module is based on
[nnlm-en-dim50](https://tfhub.dev/google/nnlm-en-dim50/1).

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens from the original vocabulary (~2.5%)
are **replaced by hash buckets**, initialized also randomly and from the same
distribution.
---------
