# 1. [biggan-128@v2](https://aihub.cloud.google.com/p/products%2Fe39eb6e3-a782-4384-95f7-a8fa9a42f3f0)
## Overview

This is the 128x128 *BigGAN* image generator described in [1], corresponding to
Row 3 in Table 2 (res. 128).

#### Example use
```python
# Load BigGAN 128 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-128/2')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.02, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 120])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 128, 128, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in
generative adversarial networks for image generation.
We are releasing the pre-trained generator to allow our work to be
verified, which is standard practice in academia.
It does not include the discriminator to minimize the potential for
exploitation.

## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed race condition causing batch statistics for previous truncation value
    to be used on the first run call for a new truncation value.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.
---------
# 2. [biggan-256@v2](https://aihub.cloud.google.com/p/products%2Feac50b05-4c5f-43d4-ab0e-4ea51f3952c6)
## Overview

This is the 256x256 *BigGAN* image generator described in [1], corresponding to
Row 4 in Table 2 (res. 256).

#### Example use
```python
# Load BigGAN 256 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-256/2')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.02, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 140])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 256, 256, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in
generative adversarial networks for image generation.
We are releasing the pre-trained generator to allow our work to be
verified, which is standard practice in academia.
It does not include the discriminator to minimize the potential for
exploitation.

## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed race condition causing batch statistics for previous truncation value
    to be used on the first run call for a new truncation value.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.
---------
# 3. [biggan-512@v2](https://aihub.cloud.google.com/p/products%2F88f5be54-5705-4795-8413-2f078f1375b1)
## Overview

This is the 512x512 *BigGAN* image generator described in [1], corresponding to
Row 5 in Table 2 (res. 512).

#### Example use
```python
# Load BigGAN 512 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-512/2')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.02, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 128])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 512, 512, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in
generative adversarial networks for image generation.
We are releasing the pre-trained generator to allow our work to be
verified, which is standard practice in academia.
It does not include the discriminator to minimize the potential for
exploitation.

## Changelog

#### Version 1

  * Initial release.

#### Version 2

  * Fixed race condition causing batch statistics for previous truncation value
    to be used on the first run call for a new truncation value.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.
---------
