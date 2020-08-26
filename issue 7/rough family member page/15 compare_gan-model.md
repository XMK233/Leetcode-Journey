# 1. [compare\_gan-model\_10\_lsun\_bedroom\_resnet19@v1](https://aihub.cloud.google.com/p/products%2Ff04e83f1-e973-4f18-ba27-6469e5e05679)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: LSUN Bedroom
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.281e-04, beta1=0.711, beta2=0.979)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: Layer normalization
* Discriminator regularization: WGAN Gradient Penalty (lambda=0.145)

#### Scores

* FID: 40.36
* Inception: 3.92
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_10_lsun_bedroom_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 2. [compare\_gan-model\_11\_cifar10\_resnet\_cifar@v1](https://aihub.cloud.google.com/p/products%2F91ffd6ce-87b0-46e6-bbc8-44ba219a3db0)
## Overview

ResNet CIFAR generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CIFAR-10
* Model: Non-saturating GAN
* Architecture: ResNet CIFAR
* Optimizer: Adam (lr=2.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 28.12
* Inception: 7.57
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_11_cifar10_resnet_cifar/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 3. [compare\_gan-model\_12\_cifar10\_resnet\_cifar@v1](https://aihub.cloud.google.com/p/products%2F7f95f54f-7afc-4319-8b0b-5ea08a46542b)
## Overview

ResNet CIFAR generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CIFAR-10
* Model: Non-saturating GAN
* Architecture: ResNet CIFAR
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 30.08
* Inception: 7.47
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_12_cifar10_resnet_cifar/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 4. [compare\_gan-model\_13\_cifar10\_resnet\_cifar@v1](https://aihub.cloud.google.com/p/products%2F9cde4ff0-9430-4fdd-9595-e1b0e85716ff)
## Overview

ResNet CIFAR generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CIFAR-10
* Model: Non-saturating GAN
* Architecture: ResNet CIFAR
* Optimizer: Adam (lr=2.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: Spectral normalization
* Discriminator regularization: none

#### Scores

* FID: 22.91
* Inception: 7.74
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_13_cifar10_resnet_cifar/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 5. [compare\_gan-model\_14\_cifar10\_resnet\_cifar@v1](https://aihub.cloud.google.com/p/products%2F5f7d0558-d96c-4351-866c-aaeaf2a7ebb0)
## Overview

ResNet CIFAR generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CIFAR-10
* Model: Non-saturating GAN
* Architecture: ResNet CIFAR
* Optimizer: Adam (lr=2.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: Spectral normalization
* Discriminator regularization: none

#### Scores

* FID: 23.22
* Inception: 7.74
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_14_cifar10_resnet_cifar/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 6. [compare\_gan-model\_15\_cifar10\_resnet\_cifar@v1](https://aihub.cloud.google.com/p/products%2F450b5a4e-523c-459d-aa99-ddb678086189)
## Overview

ResNet CIFAR generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CIFAR-10
* Model: Non-saturating GAN
* Architecture: ResNet CIFAR
* Optimizer: Adam (lr=2.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: Spectral normalization
* Discriminator regularization: WGAN Gradient Penalty (lambda=1.000)

#### Scores

* FID: 22.73
* Inception: 7.70
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_15_cifar10_resnet_cifar/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 7. [compare\_gan-model\_1\_celebahq128\_resnet19@v1](https://aihub.cloud.google.com/p/products%2F5cb333a1-c350-4432-b72c-227e755715b0)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CelebA HQ
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=3.381e-05, beta1=0.375, beta2=0.998)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 34.29
* Inception: 2.38
* MS-SSIM: 0.32

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_1_celebahq128_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 8. [compare\_gan-model\_2\_celebahq128\_resnet19@v1](https://aihub.cloud.google.com/p/products%2F7580183a-c070-444d-82b0-b24792718d84)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CelebA HQ
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 35.85
* Inception: 2.59
* MS-SSIM: 0.29

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_2_celebahq128_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 9. [compare\_gan-model\_3\_lsun\_bedroom\_resnet19@v1](https://aihub.cloud.google.com/p/products%2F5fecd953-1595-4bdc-9da4-0c5c9e765e16)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: LSUN Bedroom
* Model: Least-squares GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=3.220e-05, beta1=0.585, beta2=0.990)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 102.74
* Inception: 4.23
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_3_lsun_bedroom_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 10. [compare\_gan-model\_4\_lsun\_bedroom\_resnet19@v1](https://aihub.cloud.google.com/p/products%2F7c9cedff-bef9-4d61-8ee3-c0653110ec9e)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: LSUN Bedroom
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.927e-05, beta1=0.195, beta2=0.882)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: none
* Discriminator regularization: none

#### Scores

* FID: 112.92
* Inception: 4.10
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_4_lsun_bedroom_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 11. [compare\_gan-model\_5\_celebahq128\_resnet19@v1](https://aihub.cloud.google.com/p/products%2Fb07d9220-7f65-4039-b19a-60f2ea77197a)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CelebA HQ
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: Layer normalization
* Discriminator regularization: none

#### Scores

* FID: 30.02
* Inception: 2.38
* MS-SSIM: 0.29

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_5_celebahq128_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 12. [compare\_gan-model\_6\_celebahq128\_resnet19@v1](https://aihub.cloud.google.com/p/products%2F7c5e0934-232d-41a3-9b4b-4603bd519934)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CelebA HQ
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: Layer normalization
* Discriminator regularization: none

#### Scores

* FID: 32.05
* Inception: 2.54
* MS-SSIM: 0.28

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_6_celebahq128_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 13. [compare\_gan-model\_7\_lsun\_bedroom\_resnet19@v1](https://aihub.cloud.google.com/p/products%2Fc027f898-e89d-4924-b6f3-9a235ddb51fb)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: LSUN Bedroom
* Model: Least-squares GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=2.000e-04, beta1=0.500, beta2=0.999)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: Spectral normalization
* Discriminator regularization: none

#### Scores

* FID: 41.60
* Inception: 3.64
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_7_lsun_bedroom_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 14. [compare\_gan-model\_8\_lsun\_bedroom\_resnet19@v1](https://aihub.cloud.google.com/p/products%2Faa753b2b-595c-4321-b4c1-ee6d4d43418d)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: LSUN Bedroom
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=2.851e-04, beta1=0.102, beta2=0.998)
* Discriminator iterations per generator iteration: 1
* Discriminator normalizaton: Spectral normalization
* Discriminator regularization: none

#### Scores

* FID: 42.51
* Inception: 3.58
* MS-SSIM: N/A

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_8_lsun_bedroom_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
# 15. [compare\_gan-model\_9\_celebahq128\_resnet19@v1](https://aihub.cloud.google.com/p/products%2Fbcc3bd27-2216-4d41-be27-f61d95d2437d)
## Overview

ResNet19 generator and discriminator.

For the details of the setup, please refer to [1].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).
View all available compare_gan modules in the [Colab notebook](https://colab.research.google.com/github/google/compare_gan/blob/v2/compare_gan/src/tfhub_models.ipynb).

#### Details

* Dataset: CelebA HQ
* Model: Non-saturating GAN
* Architecture: ResNet19
* Optimizer: Adam (lr=1.000e-04, beta1=0.500, beta2=0.900)
* Discriminator iterations per generator iteration: 5
* Discriminator normalizaton: Layer normalization
* Discriminator regularization: DRAGAN Gradient Penalty (lambda=1.000)

#### Scores

* FID: 29.13
* Inception: 2.34
* MS-SSIM: 0.30

#### Example use
```python
# Declare the module
gan = hub.Module("https://tfhub.dev/google/compare_gan/model_9_celebahq128_resnet19/1")

# Use the generator signature
z_values = tf.random_uniform(minval=-1, maxval=1, shape=[64, 128])
images = gan(z_values, signature="generator")

# Use the discriminator signature
logits = gan(images, signature="discriminator")

# Drive execution with tf.Session
session.run([images, logits])
```

## References

[1] Karol Kurach*, Mario Lucic*, Xiaohua Zhai, Marcin Michalski, Sylvain Gelly.
[The GAN Landscape: Losses, Architectures, Regularization, and Normalization](https://arxiv.org/abs/1807.04720).
---------
