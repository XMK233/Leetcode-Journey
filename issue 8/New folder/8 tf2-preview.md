# 1. [tf2-preview-gnews-swivel-20dim@v1](https://aihub.cloud.google.com/p/products%2F6b1c1b14-d974-44d8-a131-4c132be4b26d)
## Overview
This module is in the **SavedModel 2.0** format and was created to help preview
TF2.0 functionalities.

Text embedding based on Swivel co-occurrence matrix factorization[1] with
pre-built OOV. Maps from text to 20-dimensional embedding vectors.

#### Example use
The saved model can be loaded directly:

```
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

It can also be used within Keras:

```
hub_layer = hub.KerasLayer("https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1", output_shape=[20],
                           input_shape=[], dtype=tf.string)

model = keras.Sequential()
model.add(hub_layer)
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
```

## Details
Created using Swivel matrix factorization method.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Vocabulary
Vocabulary contains 20,000 tokens and 1 out of vocabulary bucket for unknown
tokens.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Noam Shazeer, Ryan Doherty, Colin Evans, Chris Waterson.
[Swivel: Improving Embeddings by Noticing What's Missing](https://arxiv.org/abs/1602.02215).
---------
# 2. [tf2-preview-gnews-swivel-20dim-with-oov@v1](https://aihub.cloud.google.com/p/products%2F18fdd467-ce81-48d8-aa41-058bccff5432)
## Overview
This module is in the **SavedModel 2.0** format and was created to help preview
TF2.0 functionalities.

Text embedding based on Swivel co-occurrence matrix factorization[1] with
pre-built OOV. Maps from text to 20-dimensional embedding vectors.

#### Example use
The saved model can be loaded directly:

```
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim-with-oov/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

It can also be used within Keras:

```
hub_layer = hub.KerasLayer("https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim-with-oov/1", output_shape=[20],
                           input_shape=[], dtype=tf.string)

model = keras.Sequential()
model.add(hub_layer)
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
```

## Details
Created using Swivel matrix factorization method.

#### Input
The module takes **a batch of sentences in a 1-D tensor of strings** as input.

#### Preprocessing
The module preprocesses its input by **splitting on spaces**.

#### Vocabulary
The vocabulary contains 20,000 tokens with small fraction of the least frequent
tokens and embeddings (~2.5%) **replaced by hash buckets**. Each hash bucket is
initialized using the remaining embedding vectors that hash to the same bucket.

#### Sentence embeddings
Word embeddings are combined into sentence embedding using the `sqrtn` combiner
(see [tf.nn.embedding_lookup_sparse](https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/embedding_lookup_sparse)).

#### References
[1] Noam Shazeer, Ryan Doherty, Colin Evans, Chris Waterson.
[Swivel: Improving Embeddings by Noticing What's Missing](https://arxiv.org/abs/1602.02215).
---------
# 3. [tf2-preview-inception\_v3-classification@v4](https://aihub.cloud.google.com/p/products%2Fe58473e0-fbf7-40bd-9cea-917e3471ce2b)
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

Inception V3 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens,
    Zbigniew Wojna: ["Rethinking the Inception Architecture for Computer
    Vision"](https://arxiv.org/abs/1512.00567), 2015.

This TF-Hub module uses the TF-Slim implementation of `inception_v3`.
The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/tf2-preview/inception_v3/feature_vector/4`](https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `inception_v3_2016_08_28/inception_v3.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/classification/4", output_shape=[1001])
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output is a batch of logits vectors. The indices into the logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 299 x 299 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Calling it while trainable automatically updates the moving averages of
batch normalization.)

However, fine-tuning through a large classification might be prone to overfit.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed missing default `trainable=False`.
  * Fixed broken regularization_losses.

#### Version 3

  * Provides proper names for variables, fixing crash in `Model.save()`
    ([GitHub issue #287](https://github.com/tensorflow/hub/issues/287)).

#### Version 4

  * Adds back missing update ops for batch norm that were lost in version 3,
    ([GitHub issue #304](https://github.com/tensorflow/hub/issues/304)).
---------
# 4. [tf2-preview-inception\_v3-feature\_vector@v4](https://aihub.cloud.google.com/p/products%2Fe62c7c51-d7bc-4611-8208-0afc7742a3fc)
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

Inception V3 is a neural network architecture for image classification,
originally published by

  * Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens,
    Zbigniew Wojna: ["Rethinking the Inception Architecture for Computer
    Vision"](https://arxiv.org/abs/1512.00567), 2015.

This TF-Hub module uses the TF-Slim implementation of `inception_v3`.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/tf2-preview/inception_v3/classification/4`](https://tfhub.dev/google/tf2-preview/inception_v3/classification/4)
instead.


## Training

The checkpoint exported into this module was `inception_v3_2016_08_28/inception_v3.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4", output_shape=[2048],
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 299, 299, 3])  # Batch input shape.
```

The output of the module is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 2048. The feature
vectors can then be used further, e.g., for classification as above.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 299 x 299 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Note that this automatically updates the moving averages of
batch normalization.)


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed missing default `trainable=False`.
  * Fixed broken regularization_losses.

#### Version 3

  * Provides proper names for variables, fixing crash in `Model.save()`
    ([GitHub issue #287](https://github.com/tensorflow/hub/issues/287)).

#### Version 4

  * Adds back missing update ops for batch norm that were lost in version 3,
    ([GitHub issue #304](https://github.com/tensorflow/hub/issues/304)).
---------
# 5. [tf2-preview-mobilenet\_v2-classification@v4](https://aihub.cloud.google.com/p/products%2Fea5d2e6b-5ebe-4c14-a38a-5b9c10f542d2)
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

MobileNet V2 is a family of neural network architectures for efficient
on-device image classification and related tasks, originally published by

  * Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov,
    Liang-Chieh Chen: ["Inverted Residuals and Linear Bottlenecks:
    Mobile Networks for Classification, Detection and
    Segmentation"](https://arxiv.org/abs/1801.04381), 2018.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.

This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v2`
with a depth multiplier of 1.0 and an input size of
224x224 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/tf2-preview/mobilenet_v2/feature_vector/4`](https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4", output_shape=[1001])
])
m.build([None, 224, 224, 3])  # Batch input shape.
```

The output is a batch of logits vectors. The indices into the logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Calling it while trainable automatically updates the moving averages of
batch normalization.)

However, fine-tuning through a large classification might be prone to overfit.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed missing default `trainable=False`.
  * Fixed broken regularization_losses.

#### Version 3

  * Provides proper names for variables, fixing crash in `Model.save()`
    ([GitHub issue #287](https://github.com/tensorflow/hub/issues/287)).

#### Version 4

  * Adds back missing update ops for batch norm that were lost in version 3,
    ([GitHub issue #304](https://github.com/tensorflow/hub/issues/304)).
---------
# 6. [tf2-preview-mobilenet\_v2-feature\_vector@v4](https://aihub.cloud.google.com/p/products%2Fbf481eb3-6f51-40f8-8a59-3b68c36bf54a)
## TensorFlow 2.0 Preview

This module uses the SavedModel 2.0 format and was created to help
preview TensorFlow 2.0 functionality. Using it requires the (currently
experimental) library versions TensorFlow 2.0 and TensorFlow Hub 0.3.0.

## Overview

MobileNet V2 is a family of neural network architectures for efficient
on-device image classification and related tasks, originally published by

  * Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov,
    Liang-Chieh Chen: ["Inverted Residuals and Linear Bottlenecks:
    Mobile Networks for Classification, Detection and
    Segmentation"](https://arxiv.org/abs/1801.04381), 2018.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.

This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v2`
with a depth multiplier of 1.0 and an input size of
224x224 pixels.


The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/tf2-preview/mobilenet_v2/classification/4`](https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module can be used with the `hub.KerasLayer` as follows:

```python
m = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4", output_shape=[1280],
                   trainable=False),  # Can be True, see below.
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
m.build([None, 224, 224, 3])  # Batch input shape.
```

The output of the module is a batch of feature vectors. For each input image,
the feature vector has size `num_features` = 1280. The feature
vectors can then be used further, e.g., for classification as above.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it
by passing `trainable=True` to `hub.KerasLayer`.
(Note that this automatically updates the moving averages of
batch normalization.)


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed missing default `trainable=False`.
  * Fixed broken regularization_losses.

#### Version 3

  * Provides proper names for variables, fixing crash in `Model.save()`
    ([GitHub issue #287](https://github.com/tensorflow/hub/issues/287)).

#### Version 4

  * Adds back missing update ops for batch norm that were lost in version 3,
    ([GitHub issue #304](https://github.com/tensorflow/hub/issues/304)).
---------
# 7. [tf2-preview-nnlm-en-dim128@v1](https://aihub.cloud.google.com/p/products%2F89613833-f812-4e13-adb9-7e1078904f3e)
## Overview
This module is in the **SavedModel 2.0** format and was created to help preview
TF2.0 functionalities. It is based on [https://tfhub.dev/google/nnlm-en-dim128/1](https://tfhub.dev/google/nnlm-en-dim128/1).

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 128-dimensional embedding vectors.

#### Example use
The saved model can be loaded directly:

```
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/tf2-preview/nnlm-en-dim128/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

It can also be used within Keras:

```
hub_layer = hub.KerasLayer("https://tfhub.dev/google/tf2-preview/nnlm-en-dim128/1", output_shape=[128], 
                           input_shape=[], dtype=tf.string)

model = keras.Sequential()
model.add(hub_layer)
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
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
# 8. [tf2-preview-nnlm-en-dim50@v1](https://aihub.cloud.google.com/p/products%2Ff0382a1c-6527-4e76-9231-267ad3d34206)
## Overview
This module is in the **SavedModel 2.0** format and was created to help preview
TF2.0 functionalities. It is based on [https://tfhub.dev/google/nnlm-en-dim50/1](https://tfhub.dev/google/nnlm-en-dim50/1).

Text embedding based on feed-forward Neural-Net Language Models[1] with
pre-built OOV. Maps from text to 50-dimensional embedding vectors.

#### Example use
The saved model can be loaded directly:

```
import tensorflow_hub as hub

embed = hub.load("https://tfhub.dev/google/tf2-preview/nnlm-en-dim50/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
```

It can also be used within Keras:

```
hub_layer = hub.KerasLayer("https://tfhub.dev/google/tf2-preview/nnlm-en-dim50/1", output_shape=[50], 
                           input_shape=[], dtype=tf.string)

model = keras.Sequential()
model.add(hub_layer)
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
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
