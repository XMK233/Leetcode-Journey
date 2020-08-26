# 1. [Wiki-words-250@v1](https://aihub.cloud.google.com/p/products%2F12ce75a1-5f7c-4452-997c-73b9998373ad)
## Overview

Text embedding based on skipgram version of word2vec with 1 out-of-vocabulary
bucket. Maps from text to 250-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/Wiki-words-250/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Skipgram model, hierarchical softmax, sub-sampling 1e-5.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Module maps all out-of-vocabulary tokens into one bucket that is initialized
with zeros.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean.
[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781).
In Proceedings of Workshop at ICLR, 2013.
---------
# 2. [Wiki-words-250-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Fda0a53b5-a301-4641-b41d-d8aec0db9753)
## Overview

Text embedding based on skipgram version of word2vec with 1 out-of-vocabulary
bucket. Maps from text to 250-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/Wiki-words-250-with-normalization/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Skipgram model, hierarchical softmax, sub-sampling 1e-5.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Module maps all out-of-vocabulary tokens into one bucket that is initialized
with zeros.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean.
[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781).
In Proceedings of Workshop at ICLR, 2013.
---------
# 3. [Wiki-words-500@v1](https://aihub.cloud.google.com/p/products%2Ffdbabad5-758b-46c7-a841-08386afa204f)
## Overview

Text embedding based on skipgram version of word2vec with 1 out-of-vocabulary
bucket. Maps from text to 500-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/Wiki-words-500/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Skipgram model, hierarchical softmax, sub-sampling 1e-5.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Module maps all out-of-vocabulary tokens into one bucket that is initialized
with zeros.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean.
[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781).
In Proceedings of Workshop at ICLR, 2013.
---------
# 4. [Wiki-words-500-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Fae958f02-81f5-43ce-acfe-469b1fb18517)
## Overview

Text embedding based on skipgram version of word2vec with 1 out-of-vocabulary
bucket. Maps from text to 500-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/Wiki-words-500-with-normalization/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Skipgram model, hierarchical softmax, sub-sampling 1e-5.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Module maps all out-of-vocabulary tokens into one bucket that is initialized
with zeros.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean.
[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781).
In Proceedings of Workshop at ICLR, 2013.
---------
