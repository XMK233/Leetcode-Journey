# 1. [imagenet-mobilenet\_v1\_025\_128-classification@v3](https://aihub.cloud.google.com/p/products%2F2e357bad-a058-4de8-b239-7a5f1058dabb)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_128/mobilenet_v1_0.25_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/classification/3")
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
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 2. [imagenet-mobilenet\_v1\_025\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fbaf42351-a9d6-421d-b521-f01b51494322)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_128/mobilenet_v1_0.25_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 256.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 3. [imagenet-mobilenet\_v1\_025\_160-classification@v3](https://aihub.cloud.google.com/p/products%2Faf498bc9-9b4f-4919-ae40-193d3e6f7203)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160/mobilenet_v1_0.25_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/classification/3")
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
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 4. [imagenet-mobilenet\_v1\_025\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F256a905e-5af8-48e6-8a92-560ba4257176)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160/mobilenet_v1_0.25_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 256.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 5. [imagenet-mobilenet\_v1\_025\_192-classification@v3](https://aihub.cloud.google.com/p/products%2Fb23c2250-dee1-4459-9ac6-8c327ca92fdc)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_192/mobilenet_v1_0.25_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/classification/3")
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
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 6. [imagenet-mobilenet\_v1\_025\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fac545e36-64f2-4c3a-bffc-7bd059cc4e1c)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_192/mobilenet_v1_0.25_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 256.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 7. [imagenet-mobilenet\_v1\_025\_224-classification@v3](https://aihub.cloud.google.com/p/products%2F93839d48-c253-4ea8-83a3-d54547092bfb)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224/mobilenet_v1_0.25_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/classification/3")
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
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 8. [imagenet-mobilenet\_v1\_025\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8efa0299-dd99-44f2-839f-9ec99fd11d6d)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_025`
with a depth multiplier of 0.25 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224/mobilenet_v1_0.25_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 256.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 9. [imagenet-mobilenet\_v1\_050\_128-classification@v3](https://aihub.cloud.google.com/p/products%2F80eba1e9-cab6-4bc4-8618-59ed39f539fb)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_128/mobilenet_v1_0.5_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/classification/3")
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
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 10. [imagenet-mobilenet\_v1\_050\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Ffca984ef-e43f-40fa-8b51-a08cbd609757)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_128/mobilenet_v1_0.5_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 512.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 11. [imagenet-mobilenet\_v1\_050\_160-classification@v3](https://aihub.cloud.google.com/p/products%2F3b2b0bb1-3328-4391-999d-99da1adc16f3)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160/mobilenet_v1_0.5_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/classification/3")
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
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 12. [imagenet-mobilenet\_v1\_050\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F94e358ac-4513-426d-9cb0-168a4c985ba8)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160/mobilenet_v1_0.5_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 512.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 13. [imagenet-mobilenet\_v1\_050\_192-classification@v3](https://aihub.cloud.google.com/p/products%2Fc4b35f6b-82d8-4e76-aba2-9f9e18fe6c06)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_192/mobilenet_v1_0.5_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/classification/3")
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
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 14. [imagenet-mobilenet\_v1\_050\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fc66d9a19-c102-4ed9-a913-cf4165caed13)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_192/mobilenet_v1_0.5_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 512.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 15. [imagenet-mobilenet\_v1\_050\_224-classification@v3](https://aihub.cloud.google.com/p/products%2F7578eb13-6458-4796-80fa-86d68e4cc092)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224/mobilenet_v1_0.5_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/classification/3")
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
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 16. [imagenet-mobilenet\_v1\_050\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8c43f01d-bf62-4e71-9526-e05d6ed60179)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_050`
with a depth multiplier of 0.5 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224/mobilenet_v1_0.5_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 512.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 17. [imagenet-mobilenet\_v1\_075\_128-classification@v3](https://aihub.cloud.google.com/p/products%2F34c8ee65-d4fe-4234-a3f4-7d18c404c479)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_128/mobilenet_v1_0.75_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/classification/3")
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
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 18. [imagenet-mobilenet\_v1\_075\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fdb4f3daf-ccef-4768-9f55-84f50bd13274)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_128/mobilenet_v1_0.75_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 768.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 19. [imagenet-mobilenet\_v1\_075\_160-classification@v3](https://aihub.cloud.google.com/p/products%2Feb982d0a-f086-4408-875c-dce5d8272fab)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_160/mobilenet_v1_0.75_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/classification/3")
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
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 20. [imagenet-mobilenet\_v1\_075\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Ffe8d5ee8-a85d-4412-87db-5b56a0f72315)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_160/mobilenet_v1_0.75_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 768.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 21. [imagenet-mobilenet\_v1\_075\_192-classification@v3](https://aihub.cloud.google.com/p/products%2F2d0403f6-c7bf-4f87-a8aa-fd04c96d17c3)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_192/mobilenet_v1_0.75_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/classification/3")
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
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 22. [imagenet-mobilenet\_v1\_075\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fb35bd7a7-18c4-4a92-9731-f50f6205959c)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_192/mobilenet_v1_0.75_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 768.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 23. [imagenet-mobilenet\_v1\_075\_224-classification@v3](https://aihub.cloud.google.com/p/products%2Fe3a910da-c3bd-4bc8-94fb-f941e9fa0e50)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_224/mobilenet_v1_0.75_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/classification/3")
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
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 24. [imagenet-mobilenet\_v1\_075\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Feec28b3b-0e72-4280-ac48-56e159dc2b36)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_075`
with a depth multiplier of 0.75 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_224/mobilenet_v1_0.75_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 768.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 25. [imagenet-mobilenet\_v1\_100\_128-classification@v3](https://aihub.cloud.google.com/p/products%2Ffb69f59b-0dfa-4fda-a8f0-66b0e4c9fd7b)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_128/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_128/mobilenet_v1_1.0_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/classification/3")
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
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 26. [imagenet-mobilenet\_v1\_100\_128-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F37f37ece-e98b-4283-a370-462e1392c60d)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_128/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_128/mobilenet_v1_1.0_128.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1024.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 128 x 128 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 27. [imagenet-mobilenet\_v1\_100\_160-classification@v3](https://aihub.cloud.google.com/p/products%2Fc7a49fbc-5f83-49a4-beb3-a726efc7cc69)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_160/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160/mobilenet_v1_1.0_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/classification/3")
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
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 28. [imagenet-mobilenet\_v1\_100\_160-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fc071f984-95e4-45fa-9f00-285771a9d590)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_160/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160/mobilenet_v1_1.0_160.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1024.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 160 x 160 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 29. [imagenet-mobilenet\_v1\_100\_192-classification@v3](https://aihub.cloud.google.com/p/products%2Ffcd3da5a-fe3d-4a6a-a56f-f476f7449bb4)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_192/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_192/mobilenet_v1_1.0_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/classification/3")
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
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 30. [imagenet-mobilenet\_v1\_100\_192-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F20a94dd6-8ea0-45df-a3eb-e0b7059ab706)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_192/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_192/mobilenet_v1_1.0_192.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1024.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 192 x 192 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 31. [imagenet-mobilenet\_v1\_100\_224-classification@v3](https://aihub.cloud.google.com/p/products%2Fff23bf1c-5c35-40b0-95cb-86b7cc6f15e6)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_224/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224/mobilenet_v1_1.0_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/3")
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
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/3",
                    trainable=True, tags={"train"})
logits = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                signature="image_classification_with_bn_hparams")
```

...or analogously for signature `image_feature_vector_with_bn_hparams`.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 32. [imagenet-mobilenet\_v1\_100\_224-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F8eca3922-f765-4897-97d3-8a99e8ff14f5)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device  image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1`
with a depth multiplier of 1.0 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_224/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/3)
instead.


## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224/mobilenet_v1_1.0_224.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 1024.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
The expected size of the input images is
`height` x `width` = 224 x 224 pixels
by default, but other input sizes are possible (within limits).


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
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/feature_vector/3",
                    trainable=True, tags={"train"})
features = module(inputs=dict(images=images, batch_norm_momentum=0.997),
                  signature="image_feature_vector_with_bn_hparams")
```


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Support for variable input size.
  * Fine-tuning: change default batch norm momentum to 0.99 and
    make it configurable.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
