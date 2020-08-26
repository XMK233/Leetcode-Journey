# 1. [nnlm-de-dim128@v1](https://aihub.cloud.google.com/p/products%2F581bb5fd-cc8f-4adf-bc47-6b2fba56ed82)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-de-dim128/1")
embeddings = embed(["Katze", "Katze und Hund"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 2. [nnlm-de-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F0d2e953e-7f38-4265-9e93-2095b2dd1c5c)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-de-dim128-with-normalization/1")
embeddings = embed(["Katze", "Katze und Hund"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 3. [nnlm-de-dim50@v1](https://aihub.cloud.google.com/p/products%2F79ccd5a6-b604-448f-a71c-ea818a7ebc44)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-de-dim50/1")
embeddings = embed(["Katze", "Katze und Hund"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 4. [nnlm-de-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F4bc8df1d-c51e-4727-8c00-c728f8bb28ee)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-de-dim50-with-normalization/1")
embeddings = embed(["Katze", "Katze und Hund"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 5. [nnlm-en-dim128@v1](https://aihub.cloud.google.com/p/products%2Fa3184819-f94d-402c-9b0e-854b10d03db9)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-en-dim128/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 6. [nnlm-en-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Fd62c150f-ba94-4a0e-af48-028f0740c766)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 7. [nnlm-en-dim50@v1](https://aihub.cloud.google.com/p/products%2Feb4cd7ec-6549-4b4d-bb00-eaa1de9fa3cb)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-en-dim50/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 8. [nnlm-en-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Fd0b6d1fb-7152-43b6-b8bc-f1776be3211b)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-en-dim50-with-normalization/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 9. [nnlm-es-dim128@v1](https://aihub.cloud.google.com/p/products%2Ff6a82be2-a31e-4630-b022-d746518a83ba)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-es-dim128/1")
embeddings = embed(["gato", "gato y perro"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 10. [nnlm-es-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Fad884d6a-a003-4a85-8653-76bdaff093f2)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-es-dim128-with-normalization/1")
embeddings = embed(["gato", "gato y perro"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 11. [nnlm-es-dim50@v1](https://aihub.cloud.google.com/p/products%2Ff7bf57ae-39e2-415e-b6c4-7066e03d0fd4)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-es-dim50/1")
embeddings = embed(["gato", "gato y perro"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 12. [nnlm-es-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F21cbb434-e8f4-4155-8084-7530b7b17fea)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-es-dim50-with-normalization/1")
embeddings = embed(["gato", "gato y perro"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 13. [nnlm-id-dim128@v1](https://aihub.cloud.google.com/p/products%2F3e58488d-9270-4884-ba92-aecb57373ec1)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-id-dim128/1")
embeddings = embed(["kucing", "kucing dan anjing"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 14. [nnlm-id-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F4b795742-90ab-4942-8907-dbe98884e9db)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-id-dim128-with-normalization/1")
embeddings = embed(["kucing", "kucing dan anjing"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 15. [nnlm-id-dim50@v1](https://aihub.cloud.google.com/p/products%2F09702e46-753b-4dad-80bf-d0dda1b0421f)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-id-dim50/1")
embeddings = embed(["kucing", "kucing dan anjing"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 16. [nnlm-id-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F0a8e3c49-c4f4-4c85-a8ff-307b6e6708bf)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-id-dim50-with-normalization/1")
embeddings = embed(["kucing", "kucing dan anjing"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 17. [nnlm-ja-dim128@v1](https://aihub.cloud.google.com/p/products%2Fd22a0516-404f-4737-83fa-eefaaa6952e5)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ja-dim128/1")
embeddings = embed(["ネコ", "猫 と 犬"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 18. [nnlm-ja-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F66533fdb-a87d-4415-ad5a-d72aab38269f)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ja-dim128-with-normalization/1")
embeddings = embed(["ネコ", "猫 と 犬"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 19. [nnlm-ja-dim50@v1](https://aihub.cloud.google.com/p/products%2F187a1ce7-a131-4eda-b26f-e01eee47246e)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ja-dim50/1")
embeddings = embed(["ネコ", "猫 と 犬"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 20. [nnlm-ja-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F75f7408b-31e7-49e2-958b-50e380e2b21a)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ja-dim50-with-normalization/1")
embeddings = embed(["ネコ", "猫 と 犬"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 21. [nnlm-ko-dim128@v1](https://aihub.cloud.google.com/p/products%2Ffd04f17e-9939-41c0-a2b7-7789878f7b7d)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ko-dim128/1")
embeddings = embed(["고양이", "고양이 과 개"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 22. [nnlm-ko-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Ff405f842-d604-4b1c-b074-0d16a0ff225d)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ko-dim128-with-normalization/1")
embeddings = embed(["고양이", "고양이 과 개"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 23. [nnlm-ko-dim50@v1](https://aihub.cloud.google.com/p/products%2F33345f54-4152-4228-933a-03ffdc729c02)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ko-dim50/1")
embeddings = embed(["고양이", "고양이 과 개"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 24. [nnlm-ko-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F8dd3f7e0-98b7-4d1d-aff8-fdf98e8d0528)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-ko-dim50-with-normalization/1")
embeddings = embed(["고양이", "고양이 과 개"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 25. [nnlm-zh-dim128@v1](https://aihub.cloud.google.com/p/products%2F5adc3e79-881d-4450-95ad-6a9af0df7f22)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-zh-dim128/1")
embeddings = embed(["猫", "猫 和 狗"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 26. [nnlm-zh-dim128-with-normalization@v1](https://aihub.cloud.google.com/p/products%2Faf41efc4-c8aa-4b0c-a13c-39abcd2ddfd4)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-zh-dim128-with-normalization/1")
embeddings = embed(["猫", "猫 和 狗"])
```

## Details
Based on NNLM with three hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 27. [nnlm-zh-dim50@v1](https://aihub.cloud.google.com/p/products%2F3f91c2fb-6eb8-4539-96cf-2ab91ac39e3a)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-zh-dim50/1")
embeddings = embed(["猫", "猫 和 狗"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
# 28. [nnlm-zh-dim50-with-normalization@v1](https://aihub.cloud.google.com/p/products%2F4c36797c-3d02-4332-8c8f-16f1d5c23347)
## Overview

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
```
embed = hub.Module("https://tfhub.dev/google/nnlm-zh-dim50-with-normalization/1")
embeddings = embed(["猫", "猫 和 狗"])
```

## Details
Based on NNLM with two hidden layers.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **removing punctuation and splitting on spaces**.

#### Out of vocabulary tokens
Small fraction of the least frequent tokens and embeddings (~2.5%) are
**replaced by hash buckets**. Each hash bucket is initialized using the remaining
embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin.
[A Neural Probabilistic Language Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).
Journal of Machine Learning Research, 3:1137-1155, 2003.
---------
