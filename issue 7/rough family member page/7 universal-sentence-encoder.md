# 1. [universal-sentence-encoder@v2](https://aihub.cloud.google.com/p/products%2F79c78579-2208-4f1c-ab08-c0d94f2adad1)
## Overview

The Universal Sentence Encoder encodes text into high dimensional vectors that
can be used for text classification, semantic similarity, clustering and other
natural language tasks.

The model is trained and optimized for greater-than-word length text, such as
sentences, phrases or short paragraphs. It is trained on a variety of data
sources and a variety of tasks with the aim of dynamically accommodating a wide
variety of natural language understanding tasks. The input is variable length
English text and the output is a 512 dimensional vector. We apply this model to
the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark) for
semantic similarity, and the results can be seen in the [example
notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb)
made available. The universal-sentence-encoder model is trained with a deep
averaging network (DAN) encoder.

To learn more about text embeddings, refer to the [TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation. Our encoder differs from word level embedding models in that we
train on a number of natural language prediction tasks that require modeling the
meaning of word sequences rather than just individual words. Details are
available in the paper "Universal Sentence Encoder" [1].

#### Example use

```python
embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")
embeddings = embed([
    "The quick brown fox jumps over the lazy dog.",
    "I am a sentence for which I would like to get its embedding"])

print session.run(embeddings)

# The following are example embedding output of 512 dimensions per sentence
# Embedding for: The quick brown fox jumps over the lazy dog.
# [-0.016987282782793045, -0.008949815295636654, -0.0070627182722091675, ...]
# Embedding for: I am a sentence for which I would like to get its embedding.
# [0.03531332314014435, -0.025384284555912018, -0.007880025543272495, ...]
```

This module is about 1GB. Depending on your network speed, it might take a while
to load the first time you instantiate it. After that, loading the model should
be faster as modules are cached by default
([learn more about caching](https://www.tensorflow.org/hub/basics)). Further,
once a module is loaded to memory, inference time should be relatively fast.

#### Preprocessing
The module performs best effort text input preprocessing, therefore it is not
required to preprocess the data before applying the module.

## Semantic Similarity

![Semantic Similarity Graphic](//www.gstatic.com/aihub/tfhub/universal-sentence-encoder/example-similarity.png)

Semantic similarity is a measure of the degree to which two pieces of text carry
the same meaning. This is broadly useful in obtaining good coverage over the
numerous ways that a thought can be expressed using language without needing to
manually enumerate them.

Simple applications include improving the coverage of systems that trigger
behaviors on certain keywords, phrases or utterances.
[This section of the notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb#scrollTo=BnvjATdy64eR)
shows how to encode text and compare encoding distances as a proxy for semantic
similarity.

## Classification

![Text Classification Graphic](//www.gstatic.com/aihub/tfhub/universal-sentence-encoder/example-classification.png)

[This notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/docs/tutorials/text_classification_with_tf_hub.ipynb)
shows how to train a simple binary text classifier on top of any TF-Hub module
that can embed sentences. The Universal Sentence Encoder was partly trained with
custom text classification tasks in mind. It can be trained to perform a wide
variety of classification tasks often with a very small amount of labeled
examples.

## Known issues

* This module does not work with GPU starting with TF 1.8 ([github issue](https://github.com/tensorflow/hub/issues/160)). The problem **can be avoided** by:
  *  Using a **tf-nightly-gpu** past the commit fixing this bug (1.14.1.dev20190504).
  *  Turning off the affected Grappler optimization:

```python
config = tf.ConfigProto()
config.graph_options.rewrite_options.shape_optimization = 2
session = tf.Session(config=config)
```


## Changelog

#### Version 1
*  Initial release.

#### Version 2
*  Exposed internal variables as Trainable.

## References

[1] Daniel Cer, Yinfei Yang, Sheng-yi Kong, Nan Hua, Nicole Limtiaco,
Rhomni St. John, Noah Constant, Mario Guajardo-Céspedes, Steve Yuan, Chris Tar,
Yun-Hsuan Sung, Brian Strope, Ray Kurzweil. [Universal Sentence Encoder](https://arxiv.org/abs/1803.11175).
arXiv:1803.11175, 2018.
---------
# 2. [universal-sentence-encoder-large@v3](https://aihub.cloud.google.com/p/products%2F42c1bfd4-8104-450c-a348-29b047d3691c)
## Overview

The Universal Sentence Encoder encodes text into high dimensional vectors that
can be used for text classification, semantic similarity, clustering and other
natural language tasks.

The model is trained and optimized for greater-than-word length text, such as
sentences, phrases or short paragraphs. It is trained on a variety of data
sources and a variety of tasks with the aim of dynamically accommodating a wide
variety of natural language understanding tasks. The input is variable length
English text and the output is a 512 dimensional vector. The
universal-sentence-encoder-large model is trained with a Transformer encoder.

To learn more about text embeddings, refer to the [TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation. Our encoder differs from word level embedding models in that we
train on a number of natural language prediction tasks that require modeling the
meaning of word sequences rather than just individual words. Details are
available in the paper "Universal Sentence Encoder" [1].

#### Example use

```python
embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-large/3")
embeddings = embed([
    "The quick brown fox jumps over the lazy dog.",
    "I am a sentence for which I would like to get its embedding"])

print session.run(embeddings)

# The following are example embedding output of 512 dimensions per sentence
# Embedding for: The quick brown fox jumps over the lazy dog.
# [0.0387121252716, -0.00189059402328, -0.00533464271575, ...]
# Embedding for: I am a sentence for which I would like to get its embedding.
# [0.0489358529449, -0.0615833997726, 0.0032471306622, ...]
```

This module is about 800MB. Depending on your network speed, it might take a while
to load the first time you instantiate it. After that, loading the model should
be faster as modules are cached by default
([learn more about caching](https://www.tensorflow.org/hub/basics)). Further,
once a module is loaded to memory, inference time should be relatively fast.

Please see [Universal Sentence
Encoder](https://tfhub.dev/google/universal-sentence-encoder/2) for details and
see [this
notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb)
for code examples.

#### Preprocessing
The module performs best effort text input preprocessing, therefore it is not
required to preprocess the data before applying the module.

## Changelog

#### Version 1
*  Initial release.

#### Version 2
*  Exposed internal variables as Trainable.

#### Version 3
*  Fixed batch invariant [bug](https://github.com/tensorflow/hub/issues/74). This
   version was retrained and its embedding space differs from previous versions.

## References

[1] Daniel Cer, Yinfei Yang, Sheng-yi Kong, Nan Hua, Nicole Limtiaco,
Rhomni St. John, Noah Constant, Mario Guajardo-Céspedes, Steve Yuan, Chris Tar,
Yun-Hsuan Sung, Brian Strope, Ray Kurzweil. [Universal Sentence Encoder](https://arxiv.org/abs/1803.11175).
arXiv:1803.11175, 2018.
---------
# 3. [universal-sentence-encoder-lite@v2](https://aihub.cloud.google.com/p/products%2Ffca281b8-15fd-4a79-824b-8f3228b40fa7)
## Overview

The Universal Sentence Encoder Lite module is a lightweight version of
[Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/1).
This lite version is good for use cases when your computation resource is
limited. For example, on-device inference. It's small and still gives good
performance on various natural language understanding tasks.

The model is trained and optimized for greater-than-word length text, such as
sentences, phrases or short paragraphs. It is trained on a variety of data
sources and a variety of tasks with the aim of dynamically accommodating a wide
variety of natural language understanding tasks. The input is variable length
English text and the output is a 512 dimensional vector. We apply this model to
the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark) for
semantic similarity, and the results can be seen in the [example notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder_lite.ipynb) made available.
To learn more about text embeddings, refer to the [TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation. Our encoder differs from word level embedding models in that we
train on a number of natural language prediction tasks that require modeling the
meaning of word sequences rather than just individual words. Details are
available in the paper "Universal Sentence Encoder" [1].

#### Signatures
This module provides two signatures:

  - "default": the sentence encoding signature.
    - inputs: This signature takes IDs produced from SentencePiece processor on
      the input sentences. The IDs should be represened in tf.SparseTensor
      style by three name arguments "values", "indices", and "dense_shape". See
      'process_to_IDs_in_sparse_format()' function in the example below.
    - output: A 512 dimensional vector for each sentences.
  - "spm_path": this signatures returns the path to the SenteicePiece model
      required when processing the sentences. See the next section for details.

#### Prerequisites
You need to process all the sentences with [SentencePiece library](https://github.com/google/sentencepiece) and the SentencePiece model published
with the module together. On [Google Colaboratory](https://colab.research.google.com/),
SentencePiece library is available by:

```python
!pip3 install sentencepiece
import sentencepiece
```

To initialize a SentencePiece processor with the SentencePiece model published
with the module together:

```python
with tf.Session() as sess:
  module = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-lite/2")
  spm_path = sess.run(module(signature="spm_path"))
  # spm_path now contains a path to the SentencePiece model stored inside the
  # TF-Hub module

sp = spm.SentencePieceProcessor()
sp.Load(spm_path)
```

#### Example use

```python
import sentencepiece as spm

def process_to_IDs_in_sparse_format(sp, sentences):
  # An utility method that processes sentences with the sentence piece processor
  # 'sp' and returns the results in tf.SparseTensor-similar format:
  # (values, indices, dense_shape)
  ids = [sp.EncodeAsIds(x) for x in sentences]
  max_len = max(len(x) for x in ids)
  dense_shape=(len(ids), max_len)
  values=[item for sublist in ids for item in sublist]
  indices=[[row,col] for row in range(len(ids)) for col in range(len(ids[row]))]
  return (values, indices, dense_shape)

sp = spm.SentencePieceProcessor()
sp.Load("/path/to/sentence_piece/model")

module = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-lite/2")
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "I am a sentence for which I would like to get its embedding"]

input_placeholder = tf.sparse_placeholder(tf.int64, shape=[None, None])
embeddings = module(
    inputs=dict(
        values=input_placeholder.values,
        indices=input_placeholder.indices,
        dense_shape=input_placeholder.dense_shape))

values, indices, dense_shape = process_to_IDs_in_sparse_format(sentences)

message_embeddings = session.run(
      embeddings,
      feed_dict={input_placeholder.values: values,
                input_placeholder.indices: indices,
                input_placeholder.dense_shape: dense_shape})

print(message_embeddings)

# The following are example embedding output of 512 dimensions per sentence
# Embedding for: The quick brown fox jumps over the lazy dog.
# [0.0560572519898, 0.0534118898213, -0.0112254749984, ...]
# Embedding for: I am a sentence for which I would like to get its embedding.
# [-0.0343746766448, -0.0529498048127, 0.0469399243593, ...]
```

Please see
[Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
for details and see [this notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder_lite.ipynb) for code examples.

## Changelog

#### Version 1
*  Initial release.

#### Version 2
*  Exposed internal variables as Trainable.

## References

[1] Daniel Cer, Yinfei Yang, Sheng-yi Kong, Nan Hua, Nicole Limtiaco,
Rhomni St. John, Noah Constant, Mario Guajardo-Céspedes, Steve Yuan, Chris Tar,
Yun-Hsuan Sung, Brian Strope, Ray Kurzweil. [Universal Sentence Encoder](https://arxiv.org/abs/1803.11175).
arXiv:1803.11175, 2018.
---------
# 4. [universal-sentence-encoder-xling-en-de@v1](https://aihub.cloud.google.com/p/products%2F5aa67e0e-389a-4ad7-bac6-fe1f705bc689)
## Overview

The Universal Sentence Encoder Cross-lingual (XLING) module is an extension of
the
[Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
that includes training on multiple tasks across languages. The multi-task
training setup is based on the paper "Learning Cross-lingual Sentence
Representations via a Multi-task Dual Encoder" [1].

This specific module is trained on **English and German (en-de)** tasks, and
optimized for greater-than-word length text, such as sentences, phrases or short
paragraphs. It is trained on a variety of data sources and tasks, with the goal
of learning text representations that are useful out-of-the-box for a number of
applications. The input to the module is variable length English or German text
and the output is a 512 dimensional vector. We note that one _does not need to
specify the language_ that the input is in, as the model was trained such that
English and German text with similar meanings will have similar (high dot
product score) embeddings. We also note that this model can be used for
monolingual English (and potentially monolingual German) tasks with comparable
or even better performance than the purely English Universal Sentence Encoder.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

#### Prerequisites

This module relies on the
[SentencePiece library](https://github.com/google/sentencepiece) for input
preprocessing. On [Google Colaboratory](https://colab.research.google.com/), the
SentencePiece library is available by:

```python
!pip3 install sentencepiece
!pip3 install tf-sentencepiece
```

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tf_sentencepiece

# Some texts of different lengths.
english_sentences = ["dog", "Puppies are nice.", "I enjoy taking long walks along the beach with my dog."]
german_sentences = ["Hund", "Welpen sind nett.", "Ich genieße lange Spaziergänge am Strand entlang mit meinem Hund."]

# Set up graph.
g = tf.Graph()
with g.as_default():
  text_input = tf.placeholder(dtype=tf.string, shape=[None])
  en_de_embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-xling/en-de/1")
  embedded_text = en_de_embed(text_input)
  init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()

# Initialize session.
session = tf.Session(graph=g)
session.run(init_op)

# Compute embeddings.
en_result = session.run(embedded_text, feed_dict={text_input: [english_sentences[0]]})
de_result = session.run(embedded_text, feed_dict={text_input: [german_sentences[0]]})

# Compute similarity. Higher score indicates greater similarity.
similarity_score = np.dot(np.squeeze(en_result), np.squeeze(de_result))
```

## References

[1] M. Chidambaram, Y. Yang, D. Cer, S. Yuan, Y.-H. Sung, B. Strope, and R.
Kurzweil. Learning Cross-Lingual Sentence Representations via a Multi-task
Dual-Encoder Model. ArXiv e-prints, October 2018.
---------
# 5. [universal-sentence-encoder-xling-en-es@v1](https://aihub.cloud.google.com/p/products%2F774a1c7d-4426-41da-a964-b152fbe89c54)
## Overview

The Universal Sentence Encoder Cross-lingual (XLING) module is an extension of
the
[Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
that includes training on multiple tasks across languages. The multi-task
training setup is based on the paper "Learning Cross-lingual Sentence
Representations via a Multi-task Dual Encoder" [1].

This specific module is trained on **English and Spanish (en-es)** tasks, and
optimized for greater-than-word length text, such as sentences, phrases or short
paragraphs. It is trained on a variety of data sources and tasks, with the goal
of learning text representations that are useful out-of-the-box for a number of
applications. The input to the module is variable length English or Spanish text
and the output is a 512 dimensional vector. We note that one _does not need to
specify the language_ that the input is in, as the model was trained such that
English and Spanish text with similar meanings will have similar (high dot
product score) embeddings. We also note that this model can be used for
monolingual English (and potentially monolingual Spanish) tasks with comparable
or even better performance than the purely English Universal Sentence Encoder.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

#### Prerequisites

This module relies on the
[SentencePiece library](https://github.com/google/sentencepiece) for input
preprocessing. On [Google Colaboratory](https://colab.research.google.com/), the
SentencePiece library is available by:

```python
!pip3 install sentencepiece
!pip3 install tf-sentencepiece
```

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tf_sentencepiece

# Some texts of different lengths.
english_sentences = ["dog", "Puppies are nice.", "I enjoy taking long walks along the beach with my dog."]
spanish_sentences = ["perro", "Los cachorros son agradables.", "Disfruto de dar largos paseos por la playa con mi perro."]

# Set up graph.
g = tf.Graph()
with g.as_default():
  text_input = tf.placeholder(dtype=tf.string, shape=[None])
  en_es_embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-xling/en-es/1")
  embedded_text = en_es_embed(text_input)
  init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()

# Initialize session.
session = tf.Session(graph=g)
session.run(init_op)

# Compute embeddings.
en_result = session.run(embedded_text, feed_dict={text_input: [english_sentences[0]]})
es_result = session.run(embedded_text, feed_dict={text_input: [spanish_sentences[0]]})

# Compute similarity. Higher score indicates greater similarity.
similarity_score = np.dot(np.squeeze(en_result), np.squeeze(es_result))
```

## References

[1] M. Chidambaram, Y. Yang, D. Cer, S. Yuan, Y.-H. Sung, B. Strope, and R.
Kurzweil. Learning Cross-Lingual Sentence Representations via a Multi-task
Dual-Encoder Model. ArXiv e-prints, October 2018.
---------
# 6. [universal-sentence-encoder-xling-en-fr@v1](https://aihub.cloud.google.com/p/products%2Fd7ba5172-43d6-4860-84b8-daa5165e766b)
## Overview

The Universal Sentence Encoder Cross-lingual (XLING) module is an extension of
the
[Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
that includes training on multiple tasks across languages. The multi-task
training setup is based on the paper "Learning Cross-lingual Sentence
Representations via a Multi-task Dual Encoder" [1].

This specific module is trained on **English and French (en-fr)** tasks, and
optimized for greater-than-word length text, such as sentences, phrases or short
paragraphs. It is trained on a variety of data sources and tasks, with the goal
of learning text representations that are useful out-of-the-box for a number of
applications. The input to the module is variable length English or French text
and the output is a 512 dimensional vector. We note that one _does not need to
specify the language_ that the input is in, as the model was trained such that
English and French text with similar meanings will have similar (high dot
product score) embeddings. We also note that this model can be used for
monolingual English (and potentially monolingual French) tasks with comparable
or even better performance than the purely English Universal Sentence Encoder.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

#### Prerequisites

This module relies on the
[SentencePiece library](https://github.com/google/sentencepiece) for input
preprocessing. On [Google Colaboratory](https://colab.research.google.com/), the
SentencePiece library is available by:

```python
!pip3 install sentencepiece
!pip3 install tf-sentencepiece
```

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tf_sentencepiece

# Some texts of different lengths.
english_sentences = ["dog", "Puppies are nice.", "I enjoy taking long walks along the beach with my dog."]
french_sentences = ["chien", "Les chiots sont gentils.", "J'aime faire de longues promenades sur la plage avec mon chien."]

# Set up graph.
g = tf.Graph()
with g.as_default():
  text_input = tf.placeholder(dtype=tf.string, shape=[None])
  en_fr_embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-xling/en-fr/1")
  embedded_text = en_fr_embed(text_input)
  init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()

# Initialize session.
session = tf.Session(graph=g)
session.run(init_op)

# Compute embeddings.
en_result = session.run(embedded_text, feed_dict={text_input: [english_sentences[0]]})
fr_result = session.run(embedded_text, feed_dict={text_input: [french_sentences[0]]})

# Compute similarity. Higher score indicates greater similarity.
similarity_score = np.dot(np.squeeze(en_result), np.squeeze(fr_result))
```

## References

[1] M. Chidambaram, Y. Yang, D. Cer, S. Yuan, Y.-H. Sung, B. Strope, and R.
Kurzweil. Learning Cross-Lingual Sentence Representations via a Multi-task
Dual-Encoder Model. ArXiv e-prints, October 2018.
---------
# 7. [universal-sentence-encoder-xling-many@v1](https://aihub.cloud.google.com/p/products%2F1c473955-f951-42cc-9191-df4e6dce0ceb)
## Overview

The Universal Sentence Encoder Cross-lingual (XLING) module is an extension of
the
[Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2)
that includes training on multiple tasks across languages. The multi-task
training setup is based on the paper "Learning Cross-lingual Sentence
Representations via a Multi-task Dual Encoder" [1].

This specific module is trained on **English, French, German, Spanish, Italian,
Chinese, Korean, and Japanese** tasks, and optimized for greater-than-word
length text, such as sentences, phrases or short paragraphs. It is trained on a
variety of data sources and tasks, with the goal of learning text
representations that are useful out-of-the-box for a number of applications. The
input to the module is variable length text in any of the eight aforementioned
languages and the output is a 512 dimensional vector. We note that one _does not
need to specify the language_ of the input, as the model was trained such that
text across languages with similar meanings will have embeddings with high dot
product scores.

To learn more about text embeddings, refer to the
[TensorFlow Embeddings](https://www.tensorflow.org/guide/embedding)
documentation.

#### Prerequisites

This module relies on the
[SentencePiece library](https://github.com/google/sentencepiece) for input
preprocessing. On [Google Colaboratory](https://colab.research.google.com/), the
SentencePiece library is available by:

```python
!pip3 install sentencepiece
!pip3 install tf-sentencepiece
```

#### Example use

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tf_sentencepiece

# Some texts of different lengths.
english_sentences = ["dog", "Puppies are nice.", "I enjoy taking long walks along the beach with my dog."]
italian_sentences = ["cane", "I cuccioli sono carini.", "Mi piace fare lunghe passeggiate lungo la spiaggia con il mio cane."]
japanese_sentences = ["犬", "子犬はいいです", "私は犬と一緒にビーチを散歩するのが好きです"]

# Set up graph.
g = tf.Graph()
with g.as_default():
  text_input = tf.placeholder(dtype=tf.string, shape=[None])
  xling_8_embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-xling-many/1")
  embedded_text = xling_8_embed(text_input)
  init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()

# Initialize session.
session = tf.Session(graph=g)
session.run(init_op)

# Compute embeddings.
en_result = session.run(embedded_text, feed_dict={text_input: english_sentences})
it_result = session.run(embedded_text, feed_dict={text_input: italian_sentences})
ja_result = session.run(embedded_text, feed_dict={text_input: japanese_sentences})

# Compute similarity matrix. Higher score indicates greater similarity.
similarity_matrix_it = np.inner(en_result, it_result)
similarity_matrix_ja = np.inner(en_result, ja_result)
```

## References

[1] M. Chidambaram, Y. Yang, D. Cer, S. Yuan, Y.-H. Sung, B. Strope, and R.
Kurzweil. Learning Cross-Lingual Sentence Representations via a Multi-task
Dual-Encoder Model. ArXiv e-prints, October 2018.
---------
