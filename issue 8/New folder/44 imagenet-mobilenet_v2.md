# 1. [imagenet-mobilenet\_v2\_035\_128-classification@v3](https://aihub.cloud.google.com/p/products%2F13041a34-cc37-4e4f-bd04-ac0bd5156e68)
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
with a depth multiplier of 0.35 and an input size of
128x128 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_035_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_128/mobilenet_v2_0.35_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 2. [imagenet-mobilenet\_v2\_035\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F41c4959a-226c-4be8-807d-561a836966a2)
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
with a depth multiplier of 0.35 and an input size of
128x128 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_035_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_128/mobilenet_v2_0.35_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 3. [imagenet-mobilenet\_v2\_035\_160-classification@v3](https://aihub.cloud.google.com/p/products%2Fe7ca0182-26a9-431b-897f-48e5cf9f1c1a)
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
with a depth multiplier of 0.35 and an input size of
160x160 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_035_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_160/mobilenet_v2_0.35_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 4. [imagenet-mobilenet\_v2\_035\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fd3e7b6ae-80dd-4bee-97a2-f91fc2d21d6c)
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
with a depth multiplier of 0.35 and an input size of
160x160 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_035_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_160/mobilenet_v2_0.35_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 5. [imagenet-mobilenet\_v2\_035\_192-classification@v3](https://aihub.cloud.google.com/p/products%2F613b1e96-3dcf-4a97-93aa-b491d164c3d9)
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
with a depth multiplier of 0.35 and an input size of
192x192 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_035_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_192/mobilenet_v2_0.35_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 6. [imagenet-mobilenet\_v2\_035\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F16532d4b-ce52-4b18-adad-50416a10922e)
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
with a depth multiplier of 0.35 and an input size of
192x192 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_035_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_192/mobilenet_v2_0.35_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 7. [imagenet-mobilenet\_v2\_035\_224-classification@v3](https://aihub.cloud.google.com/p/products%2F1b4c3f06-200f-4116-a5e3-4cefc5799c63)
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
with a depth multiplier of 0.35 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_035_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_224/mobilenet_v2_0.35_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 8. [imagenet-mobilenet\_v2\_035\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8bc76c00-5f99-4894-92c6-05de3148e7ac)
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
with a depth multiplier of 0.35 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_035_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_224/mobilenet_v2_0.35_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 9. [imagenet-mobilenet\_v2\_035\_96-classification@v3](https://aihub.cloud.google.com/p/products%2F7097ed9b-8957-4b28-a2a9-4bbf22bd0462)
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
with a depth multiplier of 0.35 and an input size of
96x96 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_035_96/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_96/mobilenet_v2_0.35_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 10. [imagenet-mobilenet\_v2\_035\_96-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F9939bd82-37ac-4fc9-809d-d61df1891908)
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
with a depth multiplier of 0.35 and an input size of
96x96 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_035_96/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.35_96/mobilenet_v2_0.35_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 11. [imagenet-mobilenet\_v2\_050\_128-classification@v3](https://aihub.cloud.google.com/p/products%2Fed2f3c46-8251-4160-abce-c9e1e05e6ef1)
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
with a depth multiplier of 0.5 and an input size of
128x128 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_050_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_128/mobilenet_v2_0.5_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 12. [imagenet-mobilenet\_v2\_050\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F916a7fd4-bbac-4e6a-91f6-9e5af3e4afee)
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
with a depth multiplier of 0.5 and an input size of
128x128 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_050_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_128/mobilenet_v2_0.5_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 13. [imagenet-mobilenet\_v2\_050\_160-classification@v3](https://aihub.cloud.google.com/p/products%2Fbb1f7123-166f-4fa5-b71d-0d36045a82f8)
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
with a depth multiplier of 0.5 and an input size of
160x160 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_050_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_160/mobilenet_v2_0.5_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 14. [imagenet-mobilenet\_v2\_050\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F49b83aab-12dd-413e-928f-f85cf8b0ca3c)
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
with a depth multiplier of 0.5 and an input size of
160x160 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_050_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_160/mobilenet_v2_0.5_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 15. [imagenet-mobilenet\_v2\_050\_192-classification@v3](https://aihub.cloud.google.com/p/products%2F98d0512a-3f5a-46ac-b4d9-0e923f9462eb)
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
with a depth multiplier of 0.5 and an input size of
192x192 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_050_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_192/mobilenet_v2_0.5_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 16. [imagenet-mobilenet\_v2\_050\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Ff5db7910-0fcb-44b7-9fb6-d153ee00b8e7)
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
with a depth multiplier of 0.5 and an input size of
192x192 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_050_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_192/mobilenet_v2_0.5_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 17. [imagenet-mobilenet\_v2\_050\_224-classification@v3](https://aihub.cloud.google.com/p/products%2F40682478-2573-40f6-bd1f-4bd3882e9dea)
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
with a depth multiplier of 0.5 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_050_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_224/mobilenet_v2_0.5_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 18. [imagenet-mobilenet\_v2\_050\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F202d7c3a-7d04-4bc9-a72e-42dcced3b0ae)
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
with a depth multiplier of 0.5 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_050_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_224/mobilenet_v2_0.5_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 19. [imagenet-mobilenet\_v2\_050\_96-classification@v3](https://aihub.cloud.google.com/p/products%2Fb8f781b4-7733-4238-a89a-b94c5903d44e)
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
with a depth multiplier of 0.5 and an input size of
96x96 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_050_96/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_96/mobilenet_v2_0.5_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 20. [imagenet-mobilenet\_v2\_050\_96-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Feb7c9518-fb2e-4dbf-934c-95d2af6f257a)
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
with a depth multiplier of 0.5 and an input size of
96x96 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_050_96/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.5_96/mobilenet_v2_0.5_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 21. [imagenet-mobilenet\_v2\_075\_128-classification@v3](https://aihub.cloud.google.com/p/products%2F401734b5-e64d-4a7f-8044-25c8cf8a975a)
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
with a depth multiplier of 0.75 and an input size of
128x128 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_075_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_128/mobilenet_v2_0.75_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 22. [imagenet-mobilenet\_v2\_075\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F88a471da-49a6-46c8-85c3-aaf5c4711d5b)
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
with a depth multiplier of 0.75 and an input size of
128x128 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_075_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_128/mobilenet_v2_0.75_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 23. [imagenet-mobilenet\_v2\_075\_160-classification@v3](https://aihub.cloud.google.com/p/products%2F15f65f21-50d2-4869-baa0-cfced0e744c2)
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
with a depth multiplier of 0.75 and an input size of
160x160 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_075_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_160/mobilenet_v2_0.75_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 24. [imagenet-mobilenet\_v2\_075\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F85a2d4e2-3a0d-49c2-9365-ae12d71b0dad)
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
with a depth multiplier of 0.75 and an input size of
160x160 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_075_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_160/mobilenet_v2_0.75_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 25. [imagenet-mobilenet\_v2\_075\_192-classification@v3](https://aihub.cloud.google.com/p/products%2F0396a9ca-de5c-4a7f-9aa6-4f04aaff118d)
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
with a depth multiplier of 0.75 and an input size of
192x192 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_075_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_192/mobilenet_v2_0.75_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 26. [imagenet-mobilenet\_v2\_075\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F5ca55fc5-e5ce-44bd-a562-d56ce8dc3e4a)
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
with a depth multiplier of 0.75 and an input size of
192x192 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_075_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_192/mobilenet_v2_0.75_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 27. [imagenet-mobilenet\_v2\_075\_224-classification@v3](https://aihub.cloud.google.com/p/products%2Fcb908573-5a9d-44e0-a406-08c6e847d898)
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
with a depth multiplier of 0.75 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_075_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_224/mobilenet_v2_0.75_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 28. [imagenet-mobilenet\_v2\_075\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8bd7f50f-ac56-4f7d-848c-398d316c9838)
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
with a depth multiplier of 0.75 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_075_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_224/mobilenet_v2_0.75_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 29. [imagenet-mobilenet\_v2\_075\_96-classification@v3](https://aihub.cloud.google.com/p/products%2Fe008f1ac-7f58-4ddf-bcc2-aaa396c9f3fc)
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
with a depth multiplier of 0.75 and an input size of
96x96 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_075_96/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_96/mobilenet_v2_0.75_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 30. [imagenet-mobilenet\_v2\_075\_96-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8c7ef4e2-5856-4f0b-b00c-992c4ec9df8f)
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
with a depth multiplier of 0.75 and an input size of
96x96 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_075_96/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_0.75_96/mobilenet_v2_0.75_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 31. [imagenet-mobilenet\_v2\_100\_128-classification@v3](https://aihub.cloud.google.com/p/products%2Fa99e7ea9-4cfb-4789-89aa-375c94c6dcdb)
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
128x128 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_128/mobilenet_v2_1.0_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 32. [imagenet-mobilenet\_v2\_100\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F9ee55fc9-cb7f-4596-9d71-1d15369a60f1)
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
128x128 pixels.


The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_100_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_128/mobilenet_v2_1.0_128.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 33. [imagenet-mobilenet\_v2\_100\_160-classification@v3](https://aihub.cloud.google.com/p/products%2F582ec440-e350-4611-9a72-3bb3b949f457)
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
160x160 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_160/mobilenet_v2_1.0_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 34. [imagenet-mobilenet\_v2\_100\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F02b5212f-978b-4038-9824-a039cc948f0f)
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
160x160 pixels.


The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_100_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_160/mobilenet_v2_1.0_160.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 35. [imagenet-mobilenet\_v2\_100\_192-classification@v3](https://aihub.cloud.google.com/p/products%2Fc122c154-deed-42e6-be7f-558615fa50a6)
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
192x192 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 36. [imagenet-mobilenet\_v2\_100\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fcdf6d95f-fd41-41e4-8cba-0f5762aa4649)
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
192x192 pixels.


The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_100_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 37. [imagenet-mobilenet\_v2\_100\_224-classification@v3](https://aihub.cloud.google.com/p/products%2F5ea70ed9-9bd7-41e5-898f-e1509e8793bd)
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
[`google/imagenet/mobilenet_v2_100_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 38. [imagenet-mobilenet\_v2\_100\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F4c463130-1956-4a25-bed2-cace34d3ff00)
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
[`google/imagenet/mobilenet_v2_100_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 39. [imagenet-mobilenet\_v2\_100\_96-classification@v3](https://aihub.cloud.google.com/p/products%2F48b59149-3590-4994-9256-3fe434a827b3)
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
96x96 pixels.


The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_100_96/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_96/mobilenet_v2_1.0_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 40. [imagenet-mobilenet\_v2\_100\_96-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F4ef65e19-ef56-42a4-87ca-5e4d47bf6027)
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
96x96 pixels.


The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_100_96/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.0_96/mobilenet_v2_1.0_96.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1280.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 96 x 96 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 41. [imagenet-mobilenet\_v2\_130\_224-classification@v3](https://aihub.cloud.google.com/p/products%2F87265e6e-af6c-4071-957f-01b8c9afc719)
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
with a depth multiplier of 1.3 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_130_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.3_224/mobilenet_v2_1.3_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 42. [imagenet-mobilenet\_v2\_130\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8db8dfc9-9a17-4fa2-b82f-e2844a93baf6)
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
with a depth multiplier of 1.3 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_130_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.3_224/mobilenet_v2_1.3_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1664.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 43. [imagenet-mobilenet\_v2\_140\_224-classification@v3](https://aihub.cloud.google.com/p/products%2Ff4500342-7736-49e9-93b2-1535b377109f)
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
with a depth multiplier of 1.4 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v2_140_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.4_224/mobilenet_v2_1.4_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
logits = module(images)  # Logits with shape [batch_size, num_classes].
```

...or using the signature name `image_classification`. The indices into logits
are the `num_classes` = 1001 classes of the classification from
the original training (see above). The mapping from indices to class labels
can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt).

This module can also be used to compute [image feature
vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector),
using the signature name `image_feature_vector`.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 44. [imagenet-mobilenet\_v2\_140\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F0d6b8331-887b-455f-962f-5af5b868002f)
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
with a depth multiplier of 1.4 and an input size of
224x224 pixels.
This implementation of Mobilenet V2 rounds feature depths to multiples of 8
(an optimization *not* described in the paper).
Depth multipliers less than 1.0 are not applied to the last convolutional layer
(from which the module takes the image feature vector).

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v2_140_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v2_1.4_224/mobilenet_v2_1.4_224.ckpt` downloaded
from
[MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1792.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
This requires importing the graph version with tag set `{"train"}`
in order to operate batch normalization in training mode, and setting
`trainable=True`.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving
averages defaults to 0.99 for this module, in order to accelerate training
on small datasets (or with huge batch sizes).
Advanced users can set another value (say, 0.997) by calling this module like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed broken UPDATE_OPS for fine-tuning,
    [GitHub issue 86](https://github.com/tensorflow/hub/issues/86).

#### Version 3

  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
