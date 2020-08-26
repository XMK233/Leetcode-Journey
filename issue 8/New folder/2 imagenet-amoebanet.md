# 1. [imagenet-amoebanet\_a\_n18\_f448-classification@v1](https://aihub.cloud.google.com/p/products%2F689e685a-a1d1-494c-bec8-d7c4b1c6178a)
## Overview

AmoebaNet is a family of convolutional neural networks for image classification.
The architectures of its convolutional cells (or layers) have been found by an
evolutionary architecture search in the NASNet search space.
AmoebaNet and the NASNet search space were published, respectively, by

  * Esteban Real, Alok Aggarwal, Yanping Huang and Quoc V. Le:
    "Regularized Evolution for Image Classifier Architecture Search",
    preprint at [arXiv:1802.01548](https://arxiv.org/abs/1802.01548).
  * Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le:
    ["Learning Transferable Architectures for Scalable Image
    Recognition"](https://arxiv.org/abs/1707.07012), CVPR 2018.

This TF-Hub module uses the open-source implementation of
[AmoebaNet-A](https://github.com/tensorflow/tpu/tree/master/models/official/amoeba_net)
for ImageNet that uses <i>N</i> = 18 Normal Cells,
starting with <i>F</i> = 448 convolutional filters.
It has an input size of 331x331 pixels.

The module contains a trained instance of the network, packaged to do the
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification)
that the network was trained on. If you merely want to transform images into
feature vectors, use module
[`google/imagenet/amoebanet_a_n18_f448/feature_vector/1`](https://tfhub.dev/google/imagenet/amoebanet_a_n18_f448/feature_vector/1)
instead, and save the space occupied by the classification layer.


## Training

The weights for this module were obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("ImageNet") with Inception-style preprocessing
and data augmentation, as described in the AmoebaNet paper.


## Usage

This module implements the common signature for 
[image classification](https://www.tensorflow.org/hub/common_signatures/images#classification).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/amoebanet_a_n18_f448/classification/1")
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
`height` x `width` = 331 x 331 pixels.


## Fine-tuning

In principle, consumers of this module can
[fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.
However, fine-tuning through a large classification might be prone to overfit.

Fine-tuning requires to import the graph version with tag set `{"train"}`
in order to operate batch normalization and dropout in training mode.
The dropout probability in AmoebaNet's path dropout is not scaled with
the training steps of fine-tuning and remains at the final (maximal) value
from the initial training.
---------
# 2. [imagenet-amoebanet\_a\_n18\_f448-feature\_vector@v1](https://aihub.cloud.google.com/p/products%2F20edefb4-125e-45ac-9639-9786d20007cc)
## Overview

AmoebaNet is a family of convolutional neural networks for image classification.
The architectures of its convolutional cells (or layers) have been found by an
evolutionary architecture search in the NASNet search space.
AmoebaNet and the NASNet search space were published, respectively, by

  * Esteban Real, Alok Aggarwal, Yanping Huang and Quoc V. Le:
    "Regularized Evolution for Image Classifier Architecture Search",
    preprint at [arXiv:1802.01548](https://arxiv.org/abs/1802.01548).
  * Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le:
    ["Learning Transferable Architectures for Scalable Image
    Recognition"](https://arxiv.org/abs/1707.07012), CVPR 2018.

This TF-Hub module uses the open-source implementation of
[AmoebaNet-A](https://github.com/tensorflow/tpu/tree/master/models/official/amoeba_net)
for ImageNet that uses <i>N</i> = 18 Normal Cells,
starting with <i>F</i> = 448 convolutional filters.
It has an input size of 331x331 pixels.

The module contains a trained instance of the network, packaged to get
[feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
If you want the full model including the classification it was originally
trained for, use module
[`google/imagenet/amoebanet_a_n18_f448/classification/1`](https://tfhub.dev/google/imagenet/amoebanet_a_n18_f448/classification/1)
instead.


## Training

The weights for this module were obtained by training on the ILSVRC-2012-CLS
dataset for image classification ("ImageNet") with Inception-style preprocessing
and data augmentation, as described in the AmoebaNet paper.


## Usage

This module implements the common signature for computing
[image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector).
It can be used like

```python
module = hub.Module("https://tfhub.dev/google/imagenet/amoebanet_a_n18_f448/feature_vector/1")
height, width = hub.get_expected_image_size(module)
images = ...  # A batch of images with shape [batch_size, height, width, 3].
features = module(images)  # Features with shape [batch_size, num_features].
```

...or using the signature name `image_feature_vector`. The output for each image
in the batch is a feature vector of size `num_features` = 7168.

The input `images` are expected to have color values in the range [0,1],
following the
[common image input](https://www.tensorflow.org/hub/common_signatures/images#input)
conventions.
For this module, the size of the input images is fixed to
`height` x `width` = 331 x 331 pixels.


## Fine-tuning

Consumers of this module can [fine-tune](https://www.tensorflow.org/hub/fine_tuning) it.

Fine-tuning requires to import the graph version with tag set `{"train"}`
in order to operate batch normalization and dropout in training mode.
The dropout probability in AmoebaNet's path dropout is not scaled with
the training steps of fine-tuning and remains at the final (maximal) value
from the initial training.
---------
