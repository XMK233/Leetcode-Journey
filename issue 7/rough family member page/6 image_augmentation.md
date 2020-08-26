# 1. [image\_augmentation-crop\_color@v1](https://aihub.cloud.google.com/p/products%2F83bb37d7-5060-4ba7-85e4-6c00a582e789)
## Overview

This module performs dataset augmentation on images by cropping each input image
(keeping at least 60% of the original area), and distorting colors (brightness,
hue, saturation, contrast).

## Example distortions

![Examples of distortions](https://www.gstatic.com/aihub/tfhub/image_augmentation/crop_color.png)

## Usage

This module can be applied to a batch of encoded images, that is, a string
tensor of shape [batch_size]. The output is a batch of decoded and distorted
images with shape [batch_size, height, width, 3] and values of type float32 in
the range [0, 1] as specified by
[common image input](https://www.tensorflow.org/hub/common_signatures/images#image_input)
conventions. It means that the output of this module can be passed directly to
any
[image feature extraction](https://www.tensorflow.org/hub/common_signatures/images#image_feature_vector)
module.

```python
augmentation_module = hub.Module(
    'https://tfhub.dev/google/image_augmentation/crop_color/1')
embedding_module = hub.Module(
    'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/2')
image_size = hub.get_expected_image_size(embedding_module)

features['image'] = augmentation_module({
    'encoded_images': features['image/encoded'],
    'image_size': image_size,
    'augmentation': is_training,
})
features['embedding'] = embedding_module(features['image'])
```

Alternatively, you can use `'from_decoded_images'` signature.

## Changelog

#### Version 1

*   Initial release.
---------
# 2. [image\_augmentation-crop\_rotate\_color@v1](https://aihub.cloud.google.com/p/products%2Fcd9eda73-8cc4-4dbc-aa62-c97e98d657af)
## Overview

This module performs dataset augmentation on images by cropping each input image
(keeping at least 60% of the original area), rotating it (at most 30 degrees),
and distorting colors (brightness, hue, saturation, contrast).

## Example distortions

![Examples of distortions](https://www.gstatic.com/aihub/tfhub/image_augmentation/crop_rotate_color.png)

## Usage

This module can be applied to a batch of encoded images, that is, a string
tensor of shape [batch_size]. The output is a batch of decoded and distorted
images with shape [batch_size, height, width, 3] and values of type float32 in
the range [0, 1] as specified by
[common image input](https://www.tensorflow.org/hub/common_signatures/images#image_input)
conventions. It means that the output of this module can be passed directly to
any
[image feature extraction](https://www.tensorflow.org/hub/common_signatures/images#image_feature_vector)
module.

```python
# The augmentation module uses some ops from tf.contrib.image that needs to be registered.
import tf.contrib.image

augmentation_module = hub.Module(
    'https://tfhub.dev/google/image_augmentation/crop_rotate_color/1')
embedding_module = hub.Module(
    'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/2')
image_size = hub.get_expected_image_size(embedding_module)

features['image'] = augmentation_module({
    'encoded_images': features['image/encoded'],
    'image_size': image_size,
    'augmentation': is_training,
})
features['embedding'] = embedding_module(features['image'])
```

Alternatively, you can use `'from_decoded_images'` signature.

## Changelog

#### Version 1

*   Initial release.
---------
# 3. [image\_augmentation-flipx\_crop\_rotate\_color@v1](https://aihub.cloud.google.com/p/products%2F2012b39c-9bd7-4670-bbc0-190c89405778)
## Overview

This module performs dataset augmentation on images by flipping the input image
(with 50% probability), cropping the image (keeping at least 60% of the original
area), rotating it (at most 30 degrees), and distorting colors (brightness, hue,
saturation, contrast).

## Example distortions

![Examples of distortions](https://www.gstatic.com/aihub/tfhub/image_augmentation/flipx_crop_rotate_color.png)

## Usage

This module can be applied to a batch of encoded images, that is, a string
tensor of shape [batch_size]. The output is a batch of decoded and distorted
images with shape [batch_size, height, width, 3] and values of type float32 in
the range [0, 1] as specified by
[common image input](https://www.tensorflow.org/hub/common_signatures/images#image_input)
conventions. It means that the output of this module can be passed directly to
any
[image feature extraction](https://www.tensorflow.org/hub/common_signatures/images#image_feature_vector)
module.

```python
# The augmentation module uses some ops from tf.contrib.image that needs to be registered.
import tf.contrib.image

augmentation_module = hub.Module(
    'https://tfhub.dev/google/image_augmentation/flipx_crop_rotate_color/1')
embedding_module = hub.Module(
    'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/2')
image_size = hub.get_expected_image_size(embedding_module)

features['image'] = augmentation_module({
    'encoded_images': features['image/encoded'],
    'image_size': image_size,
    'augmentation': is_training,
})
features['embedding'] = embedding_module(features['image'])
```

Alternatively, you can use `'from_decoded_images'` signature.

## Changelog

#### Version 1

*   Initial release.
---------
# 4. [image\_augmentation-nas\_cifar@v1](https://aihub.cloud.google.com/p/products%2F822fa7f1-2207-4645-bcab-b7b916dae368)
## Overview

This module performs dataset augmentation on images by a policy discovered by
AutoAugment algorithm published by: Ekin D. Cubuk, Barret Zoph, Dandelion Mane,
Vijay Vasudevan, Quoc V. Le:
[AutoAugment: Learning Augmentation Policies from Data](https://arxiv.org/pdf/1805.09501.pdf)
(2018).

This module reuses implementation of an image augmentation policy from authors
of the paper.

## Example distortions

![Examples of distortions](https://www.gstatic.com/aihub/tfhub/image_augmentation/nas_cifar.png)

## Usage

This module can be applied to a batch of encoded images, that is, a string
tensor of shape [batch_size]. The output is a batch of decoded and distorted
images with shape [batch_size, height, width, 3] and values of type float32 in
the range [0, 1] as specified by
[common image input](https://www.tensorflow.org/hub/common_signatures/images#image_input)
conventions. It means that the output of this module can be passed directly to
any
[image feature extraction](https://www.tensorflow.org/hub/common_signatures/images#image_feature_vector)
module.

```python
# The augmentation module uses some ops from tf.contrib.image that needs to be registered.
import tf.contrib.image

augmentation_module = hub.Module(
    'https://tfhub.dev/google/image_augmentation/nas_cifar/1')
embedding_module = hub.Module(
    'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/2')
image_size = hub.get_expected_image_size(embedding_module)

features['image'] = augmentation_module({
    'encoded_images': features['image/encoded'],
    'image_size': image_size,
    'augmentation': is_training,
})
features['embedding'] = embedding_module(features['image'])
```

Alternatively, you can use `'from_decoded_images'` signature.

## Changelog

#### Version 1

*   Initial release.
---------
# 5. [image\_augmentation-nas\_imagenet@v1](https://aihub.cloud.google.com/p/products%2Fdaf153b0-cc1b-4f27-a037-5bd3d9fff224)
## Overview

This module performs dataset augmentation on images by a policy discovered by
AutoAugment algorithm published by: Ekin D. Cubuk, Barret Zoph, Dandelion Mane,
Vijay Vasudevan, Quoc V. Le:
[AutoAugment: Learning Augmentation Policies from Data](https://arxiv.org/pdf/1805.09501.pdf)
(2018).

This module reuses implementation of an image augmentation policy from authors
of the paper.

## Example distortions

![Examples of distortions](https://www.gstatic.com/aihub/tfhub/image_augmentation/nas_imagenet.png)

## Usage

This module can be applied to a batch of encoded images, that is, a string
tensor of shape [batch_size]. The output is a batch of decoded and distorted
images with shape [batch_size, height, width, 3] and values of type float32 in
the range [0, 1] as specified by
[common image input](https://www.tensorflow.org/hub/common_signatures/images#image_input)
conventions. It means that the output of this module can be passed directly to
any
[image feature extraction](https://www.tensorflow.org/hub/common_signatures/images#image_feature_vector)
module.

```python
# The augmentation module uses some ops from tf.contrib.image that needs to be registered.
import tf.contrib.image

augmentation_module = hub.Module(
    'https://tfhub.dev/google/image_augmentation/nas_imagenet/1')
embedding_module = hub.Module(
    'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/2')
image_size = hub.get_expected_image_size(embedding_module)

features['image'] = augmentation_module({
    'encoded_images': features['image/encoded'],
    'image_size': image_size,
    'augmentation': is_training,
})
features['embedding'] = embedding_module(features['image'])
```

Alternatively, you can use `'from_decoded_images'` signature.

## Changelog

#### Version 1

*   Initial release.
---------
# 6. [image\_augmentation-nas\_svhn@v1](https://aihub.cloud.google.com/p/products%2F5eef4456-8aa9-47d7-84db-00a7faa6662a)
## Overview

This module performs dataset augmentation on images by a policy discovered by
AutoAugment algorithm published by: Ekin D. Cubuk, Barret Zoph, Dandelion Mane,
Vijay Vasudevan, Quoc V. Le:
[AutoAugment: Learning Augmentation Policies from Data](https://arxiv.org/pdf/1805.09501.pdf)
(2018).

This module reuses implementation of an image augmentation policy from authors
of the paper.

## Example distortions

![Examples of distortions](https://www.gstatic.com/aihub/tfhub/image_augmentation/nas_svhn.png)

## Usage

This module can be applied to a batch of encoded images, that is, a string
tensor of shape [batch_size]. The output is a batch of decoded and distorted
images with shape [batch_size, height, width, 3] and values of type float32 in
the range [0, 1] as specified by
[common image input](https://www.tensorflow.org/hub/common_signatures/images#image_input)
conventions. It means that the output of this module can be passed directly to
any
[image feature extraction](https://www.tensorflow.org/hub/common_signatures/images#image_feature_vector)
module.

```python
# The augmentation module uses some ops from tf.contrib.image that needs to be registered.
import tf.contrib.image

augmentation_module = hub.Module(
    'https://tfhub.dev/google/image_augmentation/nas_svhn/1')
embedding_module = hub.Module(
    'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/2')
image_size = hub.get_expected_image_size(embedding_module)

features['image'] = augmentation_module({
    'encoded_images': features['image/encoded'],
    'image_size': image_size,
    'augmentation': is_training,
})
features['embedding'] = embedding_module(features['image'])
```

Alternatively, you can use `'from_decoded_images'` signature.

## Changelog

#### Version 1

*   Initial release.
---------
