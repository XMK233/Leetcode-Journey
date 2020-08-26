# 1. [compare\_gan-s3gan\_20\_128x128@v1](https://aihub.cloud.google.com/p/products%2F7fd7121a-a84e-4d35-bb83-21e035cd16b2)
## Overview

S3GAN generator and discriminator.

For the details of the setup, please refer to [2].
The code used to train these models is available on
[GitHub](https://github.com/google/compare_gan).

#### Scores

* FID: 6.9
* Inception: 98

#### Example use

```python
# Load module.
module = hub.Module("https://tfhub.dev/google/compare_gan/s3gan_20_128x128/1")

batch_size = 8
z_dim = 120

# Sample random noise (z) and ImageNet label (y) inputs.
z = tf.random.normal([batch_size, z_dim])  # noise sample
labels = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
inputs = dict(z=z, labels=labels)

samples = module(inputs)
```

## References

[1] Mario Lucic*, Michael Tschannen*, Marvin Ritter*, Xiaohua Zhai, Olivier
Bachem, Sylvain Gelly
[High-Fidelity Image Generation With Fewer Labels](https://arxiv.org/abs/1903.02271)
---------
# 2. [compare\_gan-s3gan\_2\_5\_128x128@v1](https://aihub.cloud.google.com/p/products%2F65e3632b-f995-43f5-be9f-c555f21d8cc6)
## Overview

S3GAN generator and discriminator.

For the details of the setup, please refer to [2]. The code used to train these
models is available on [GitHub](https://github.com/google/compare_gan).

#### Scores

*   FID: 12.6
*   Inception: 48

#### Example use

```python
# Load module.
module = hub.Module("https://tfhub.dev/google/compare_gan/s3gan_20_128x128/1")

batch_size = 8
z_dim = 120

# Sample random noise (z) and ImageNet label (y) inputs.
z = tf.random.normal([batch_size, z_dim])  # noise sample
labels = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
inputs = dict(z=z, labels=labels)

samples = module(inputs)
```

## References

[1] Mario Lucic*, Michael Tschannen*, Marvin Ritter*, Xiaohua Zhai, Olivier
Bachem, Sylvain Gelly
[High-Fidelity Image Generation With Fewer Labels](https://arxiv.org/abs/1903.02271)
---------
# 3. [compare\_gan-s3gan\_5\_128x128@v1](https://aihub.cloud.google.com/p/products%2F86cec259-af18-479a-bc0a-d57db391a323)
## Overview

S3GAN generator and discriminator.

For the details of the setup, please refer to [2]. The code used to train these
models is available on [GitHub](https://github.com/google/compare_gan).

#### Scores

*   FID: 8.4
*   Inception: 74

#### Example use

```python
# Load module.
module = hub.Module("https://tfhub.dev/google/compare_gan/s3gan_20_128x128/1")

batch_size = 8
z_dim = 120

# Sample random noise (z) and ImageNet label (y) inputs.
z = tf.random.normal([batch_size, z_dim])  # noise sample
labels = tf.random.uniform([batch_size], maxval=1000, dtype=tf.int32)
inputs = dict(z=z, labels=labels)

samples = module(inputs)
```

## References

[1] Mario Lucic*, Michael Tschannen*, Marvin Ritter*, Xiaohua Zhai, Olivier
Bachem, Sylvain Gelly
[High-Fidelity Image Generation With Fewer Labels](https://arxiv.org/abs/1903.02271)
---------
