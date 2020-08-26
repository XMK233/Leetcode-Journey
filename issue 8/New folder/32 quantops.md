# 1. [imagenet-mobilenet\_v1\_025\_128-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2Fc66937a1-5ef0-4b23-aa9d-7c49097d19c5)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_128/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_128_quant/mobilenet_v1_0.25_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 2. [imagenet-mobilenet\_v1\_025\_128-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Ff5f87ef8-0b36-4d85-9664-8fc6a7e4fc0f)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_128/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_128_quant/mobilenet_v1_0.25_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 3. [imagenet-mobilenet\_v1\_025\_160-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2Fb2c8e4bf-a4aa-404c-8cae-525a9944182a)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_160/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160_quant/mobilenet_v1_0.25_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 4. [imagenet-mobilenet\_v1\_025\_160-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F7d9362ba-5f53-44b2-acdc-131691e23e29)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_160/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160_quant/mobilenet_v1_0.25_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 5. [imagenet-mobilenet\_v1\_025\_192-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F8b75406e-47e4-4261-bd0f-9fdf32ee329d)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_192/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_192_quant/mobilenet_v1_0.25_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 6. [imagenet-mobilenet\_v1\_025\_192-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F4e39382a-955f-438e-b5bd-9c45df0c50d3)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_192/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_192_quant/mobilenet_v1_0.25_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 7. [imagenet-mobilenet\_v1\_025\_224-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F848e4116-1803-49ba-9c74-23365d448428)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_025_224/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224_quant/mobilenet_v1_0.25_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 8. [imagenet-mobilenet\_v1\_025\_224-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F9ad83825-4d7d-4729-9aba-e1657cf82955)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_025`, **instrumented for quantization**,
with a depth multiplier of 0.25 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_025_224/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224_quant/mobilenet_v1_0.25_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 9. [imagenet-mobilenet\_v1\_050\_128-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F0dc0d585-1ff5-4501-b9ce-5a0dd183d41b)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_128/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_128_quant/mobilenet_v1_0.5_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 10. [imagenet-mobilenet\_v1\_050\_128-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F5ca67ec2-8aae-43a1-aa60-c14a7469d50c)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_128/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_128_quant/mobilenet_v1_0.5_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 11. [imagenet-mobilenet\_v1\_050\_160-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2Fefbecded-bb7e-4d95-a784-35c09efb84fc)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_160/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160_quant/mobilenet_v1_0.5_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 12. [imagenet-mobilenet\_v1\_050\_160-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Ff71d5c2a-fc77-44cd-9ec7-b17a68595ac5)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_160/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160_quant/mobilenet_v1_0.5_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 13. [imagenet-mobilenet\_v1\_050\_192-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F558058fe-0d24-4bdc-a4b5-739ca7adb7b5)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_192/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_192_quant/mobilenet_v1_0.5_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 14. [imagenet-mobilenet\_v1\_050\_192-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F1e335893-c2c1-443f-be23-04240fbc7839)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_192/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_192_quant/mobilenet_v1_0.5_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 15. [imagenet-mobilenet\_v1\_050\_224-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F711fda69-6f28-40e7-84bc-bd9f811a1eb8)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_050_224/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224_quant/mobilenet_v1_0.5_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 16. [imagenet-mobilenet\_v1\_050\_224-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fbe53911c-ce9f-4bc0-b229-3783fd7eb516)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_050`, **instrumented for quantization**,
with a depth multiplier of 0.5 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_050_224/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224_quant/mobilenet_v1_0.5_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 17. [imagenet-mobilenet\_v1\_075\_128-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2Fc2480cdc-afac-4f50-b222-0988427d84ed)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_128/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_128_quant/mobilenet_v1_0.75_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 18. [imagenet-mobilenet\_v1\_075\_128-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fb4168dee-fc60-4983-9342-82df37168fef)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_128/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_128_quant/mobilenet_v1_0.75_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 19. [imagenet-mobilenet\_v1\_075\_160-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F83a5c631-0c56-40e7-93f2-d34831f317c1)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_160/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_160_quant/mobilenet_v1_0.75_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 20. [imagenet-mobilenet\_v1\_075\_160-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F30ed3255-649b-4d5d-8eab-4e2d1ea20a90)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_160/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_160_quant/mobilenet_v1_0.75_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 21. [imagenet-mobilenet\_v1\_075\_192-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2Fa455648c-ccd4-46ad-a743-fa6f82d96a5c)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_192/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_192_quant/mobilenet_v1_0.75_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 22. [imagenet-mobilenet\_v1\_075\_192-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F189a3dd7-35ea-4a53-ab2c-746396b884cb)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_192/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_192_quant/mobilenet_v1_0.75_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 23. [imagenet-mobilenet\_v1\_075\_224-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F4a5326c3-a371-4609-b8c7-05d10719b171)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_075_224/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_224_quant/mobilenet_v1_0.75_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 24. [imagenet-mobilenet\_v1\_075\_224-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fa41b9636-3ef7-421a-8594-d46037d1f0d6)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1_075`, **instrumented for quantization**,
with a depth multiplier of 0.75 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_075_224/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_0.75_224_quant/mobilenet_v1_0.75_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 25. [imagenet-mobilenet\_v1\_100\_128-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F527e439e-fc16-4419-bdbb-caf7f247009e)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_128/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_128_quant/mobilenet_v1_1.0_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 26. [imagenet-mobilenet\_v1\_100\_128-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fffd67803-8128-49d5-a310-896ccbfda23b)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
128x128 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_128/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_128_quant/mobilenet_v1_1.0_128_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 128 x 128 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 27. [imagenet-mobilenet\_v1\_100\_160-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2Ffe2a7857-566b-45b9-bc85-22e2f90f8904)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_160/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160_quant/mobilenet_v1_1.0_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 28. [imagenet-mobilenet\_v1\_100\_160-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F16f425f5-53ad-43a4-9fb2-b454e7dd611d)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
160x160 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_160/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160_quant/mobilenet_v1_1.0_160_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 160 x 160 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 29. [imagenet-mobilenet\_v1\_100\_192-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F99959f36-5676-4fcf-af54-42adc89d2cce)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_192/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_192_quant/mobilenet_v1_1.0_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 30. [imagenet-mobilenet\_v1\_100\_192-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fe519e11e-8155-46b6-892e-86e39a9af2cd)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
192x192 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_192/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_192_quant/mobilenet_v1_1.0_192_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 192 x 192 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 31. [imagenet-mobilenet\_v1\_100\_224-quantops-classification@v3](https://aihub.cloud.google.com/p/products%2F0940e0bd-5d4c-44ae-b51b-f48a93109166)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/mobilenet_v1_100_224/quantops/feature_vector/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/quantops/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224_quant/mobilenet_v1_1.0_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/quantops/classification/3")
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

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
# 32. [imagenet-mobilenet\_v1\_100\_224-quantops-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Faaf6a352-ad6b-4769-a4cc-f237465fd989)
## Overview

MobileNet V1 is a family of neural network architectures for efficient
on-device image classification, originally published by

  * Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang,
    Tobias Weyand, Marco Andreetto, Hartwig Adam:
    ["MobileNets: Efficient Convolutional Neural Networks for
    Mobile Vision Applications"](https://arxiv.org/abs/1704.04861), 2017.

Mobilenets come in various sizes controlled by a multiplier for the
depth (number of features) in the convolutional layers. They can also be
trained for various sizes of input images to control inference speed.
This TF-Hub module uses the TF-Slim implementation of
`mobilenet_v1_v1`, **instrumented for quantization**,
with a depth multiplier of 1.0 and an input size of
224x224 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/mobilenet_v1_100_224/quantops/classification/3`](https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/quantops/classification/3)
instead.


## Quantization

This module is meant for use in models whose weights will be quantized to
`uint8` by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)
for deployment to mobile devices.

The trained weights of this module are shipped as `float32` numbers,
but its graph has been augmented by `tf.contrib.quantize` with extra ops
that simulate the effect of quantization already during training,
so that the model can adjust to it.

## Training

The checkpoint exported into this module was `mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224_quant/mobilenet_v1_1.0_224_quant.ckpt` downloaded
from
[MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet"), with simulated quantization.

## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/quantops/feature_vector/3")
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
For this module, the size of the input images is fixed to
`height` x `width` = 224 x 224 pixels.


## Fine-tuning

The current version of this module only provides an inference graph
and cannot be fine-tuned.


## Changelog

#### Version 1

  * Initial release.

#### Version 3

  * Avoids crash in some TFLite/toco versions
    ([GitHub issue 109](https://github.com/tensorflow/hub/issues/109))
    by overestimating quantization boundaries on input image by 0.05%.
  * Requires PIP package `tensorflow-hub>=0.2.0`.
---------
