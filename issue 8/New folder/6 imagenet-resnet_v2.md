# 1. [imagenet-resnet\_v2\_101-classification@v3](https://aihub.cloud.google.com/p/products%2F4d580b21-7dce-4d2a-a240-f61cb76a75cb)
## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_101`
with 101 layers.
The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/resnet_v2_101/feature_vector/3`](https://tfhub.dev/google/imagenet/resnet_v2_101/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `resnet_v2_101_2017_04_14/resnet_v2_101.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_101/classification/3")
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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_101/classification/3",
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
# 2. [imagenet-resnet\_v2\_101-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2F4dd7a845-66db-4ac0-a4b6-b1933b1dc281)
## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_101`
with 101 layers.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/resnet_v2_101/classification/3`](https://tfhub.dev/google/imagenet/resnet_v2_101/classification/3)
instead.


## Training

The checkpoint exported into this module was `resnet_v2_101_2017_04_14/resnet_v2_101.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_101/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 2048.

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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_101/feature_vector/3",
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
# 3. [imagenet-resnet\_v2\_152-classification@v3](https://aihub.cloud.google.com/p/products%2F30e3d1be-cece-4c09-9a7c-03c6841a5f41)
## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_152`
with 152 layers.
The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/resnet_v2_152/feature_vector/3`](https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `resnet_v2_152_2017_04_14/resnet_v2_152.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/3")
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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/classification/3",
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
# 4. [imagenet-resnet\_v2\_152-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fdb11b3e9-446e-455a-877c-9d812fe96585)
## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_152`
with 152 layers.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/resnet_v2_152/classification/3`](https://tfhub.dev/google/imagenet/resnet_v2_152/classification/3)
instead.


## Training

The checkpoint exported into this module was `resnet_v2_152_2017_04_14/resnet_v2_152.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 2048.

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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_152/feature_vector/3",
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
# 5. [imagenet-resnet\_v2\_50-classification@v3](https://aihub.cloud.google.com/p/products%2F9f12fca3-c88a-4548-9c29-d875af05f22b)
## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_50`
with 50 layers.
The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/resnet_v2_50/feature_vector/3`](https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/3)
instead, and save the space occupied by the classification layer.


## Training

The checkpoint exported into this module was `resnet_v2_50_2017_04_14/resnet_v2_50.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_50/classification/3")
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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_50/classification/3",
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
# 6. [imagenet-resnet\_v2\_50-feature\_vector@v3](https://aihub.cloud.google.com/p/products%2Fa350eeeb-87ff-4335-9dc3-b2b7ec1db794)
## Overview

ResNet V2 is a family of network architectures for image classification
with a variable number of layers. It builds on the ResNet architecture
originally published by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Deep Residual Learning
    for Image Recognition"](https://arxiv.org/abs/1512.03385), 2015.

The full preactivation 'V2' variant of ResNet used in this module was
introduced by

  * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: ["Identity Mappings in
    Deep Residual Networks"](https://arxiv.org/abs/1603.05027), 2016.

The key difference compared to ResNet V1 is the use of batch normalization
before every weight layer.

This TF-Hub module uses the TF-Slim implementation of `resnet_v2_50`
with 50 layers.
The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/resnet_v2_50/classification/3`](https://tfhub.dev/google/imagenet/resnet_v2_50/classification/3)
instead.


## Training

The checkpoint exported into this module was `resnet_v2_50_2017_04_14/resnet_v2_50.ckpt` downloaded
from
[TF-Slim's pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/README.md#pre-trained-models).
Its weights were originally obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("Imagenet").


## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/3")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 2048.

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
module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/3",
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
