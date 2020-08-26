# 1. [biggan-deep-128@v1](https://aihub.cloud.google.com/p/products%2F6c2d2087-5133-4d3d-936b-538ef36da6ca)
## Overview

This is the 128x128 *BigGAN-deep* image generator described in [1],
corresponding to Row 6 in Table 2 (res. 128).

#### Example use

```python
# Load BigGAN-deep 128 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-deep-128/1')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.0, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 128])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 128, 128, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in generative
adversarial networks for image generation. We are releasing the pre-trained
generator to allow our work to be verified, which is standard practice in
academia. It does not include the discriminator to minimize the potential for
exploitation.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.
---------
# 2. [biggan-deep-256@v1](https://aihub.cloud.google.com/p/products%2Fe7c0f3f6-319b-4e67-b812-7b362d4a9bcd)
## Overview

This is the 256x256 *BigGAN-deep* image generator described in [1],
corresponding to Row 7 in Table 2 (res. 256).

#### Example use

```python
# Load BigGAN-deep 256 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-deep-256/1')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.0, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 128])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 256, 256, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in generative
adversarial networks for image generation. We are releasing the pre-trained
generator to allow our work to be verified, which is standard practice in
academia. It does not include the discriminator to minimize the potential for
exploitation.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.
---------
# 3. [biggan-deep-512@v1](https://aihub.cloud.google.com/p/products%2F023a13aa-3380-433f-bbfd-d3508aa8ec2b)
## Overview

This is the 512x512 *BigGAN-deep* image generator described in [1],
corresponding to Row 8 in Table 2 (res. 512).

#### Example use

```python
# Load BigGAN-deep 512 module.
module = hub.Module('https://tfhub.dev/deepmind/biggan-deep-512/1')

# Sample random noise (z) and ImageNet label (y) inputs.
batch_size = 8
truncation = 0.5  # scalar truncation value in [0.0, 1.0]
z = truncation * tf.random.truncated_normal([batch_size, 128])  # noise sample
y_index = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
y = tf.one_hot(y_index, 1000)  # one-hot ImageNet label

# Call BigGAN on a dict of the inputs to generate a batch of images with shape
# [8, 512, 512, 3] and range [-1, 1].
samples = module(dict(y=y, z=z, truncation=truncation))
```

#### Note from the authors

This work was conducted to advance the state of the art in generative
adversarial networks for image generation. We are releasing the pre-trained
generator to allow our work to be verified, which is standard practice in
academia. It does not include the discriminator to minimize the potential for
exploitation.

## References

[1] Andrew Brock, Jeff Donahue, and Karen Simonyan.
[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096).
*arxiv:1809.11096*, 2018.
---------
