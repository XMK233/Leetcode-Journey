## 1. imagenet-amoebanet

**AmoebaNet is a family of convolutional neural networks for image classification; The architectures of its convolutional cells (or layers) have been found by an evolutionary architecture search in the NASNet search space**

### 1.1 [imagenet-amoebanet\_a\_n18\_f448-feature\_vector@1](https://aihub.cloud.google.com/p/products%2F20edefb4-125e-45ac-9639-9786d20007cc)


Module Description: 

* implementation of AmoebaNet-A

*  N = 18 Normal Cells

*  starting with F = 448 convolutional filters


References: 

* *arXiv:1802.01548*

* *Learning Transferable Architectures for Scalable Image Recognition*


Changelog: 

    None

## 2. imagenet-inception\_resnet\_v2

**Inception ResNet V2 is a neural network architecture for image classification**

### 2.1 [imagenet-inception\_resnet\_v2-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F462e23f3-f3c3-4c85-8cdf-7ee1f49524fd)


Module Description: 

* feature vector of size num_features = 1536

*  input images is height x width = 299 x 299 pixels by default


References: 

* *Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 3. imagenet-inception\_v1

**Inception V1 (a.k.a. GoogLeNet) is a neural network architecture for image classification**

### 3.1 [imagenet-inception\_v1-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F1d3a69a4-7546-436e-8e4d-98170906cd44)


Module Description: 

* feature vector of size num_features = 1024

*  size of the input images is height x width = 224 x 224 pixels


References: 

* *Going deeper with convolutions*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 4. imagenet-inception\_v2

**Inception V2 is a neural network architecture for image classification; Inception V2 uses are more powerful architecture made possible by the use of batch normalization**

### 4.1 [imagenet-inception\_v2-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F3fdd6238-9978-48cf-b5ed-4f5c0b2dbec8)


Module Description: 

* feature vector of size num_features = 1024

*  size of the input images is height x width = 224 x 224 pixels


References: 

* *Going deeper with convolutions*

* *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 5. imagenet-inception\_v3

**Inception V3 is a neural network architecture for image classification**

### 5.1 [imagenet-inception\_v3-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F05659cd0-245d-4a76-9a1a-9fc59c56b1bc)


Module Description: 

* feature vector of size num_features = 2048

*  size of the input images is height x width = 299 x 299 pixels


References: 

* *Rethinking the Inception Architecture for Computer Vision*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 6. imagenet-mobilenet\_v1

**MobileNet V1 is a family of neural network architectures for efficient on-device image classification; Mobilenets come in various sizes controlled by a multiplier for the depth (number of features) in the convolutional layers; They can also be trained for various sizes of input images to control inference speed**

### 6.1 [imagenet-mobilenet\_v1\_025\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fbaf42351-a9d6-421d-b521-f01b51494322)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 128x128 pixels

*  feature vector of size num_features = 256

*  size of the input images is height x width = 128 x 128 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.2 [imagenet-mobilenet\_v1\_025\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F256a905e-5af8-48e6-8a92-560ba4257176)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 160x160 pixels

*  feature vector of size num_features = 256

*  size of the input images is height x width = 160 x 160 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.3 [imagenet-mobilenet\_v1\_025\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fac545e36-64f2-4c3a-bffc-7bd059cc4e1c)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 192x192 pixels

*  feature vector of size num_features = 256

*  size of the input images is height x width = 192 x 192 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.4 [imagenet-mobilenet\_v1\_025\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8efa0299-dd99-44f2-839f-9ec99fd11d6d)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 224x224 pixels

*  feature vector of size num_features = 256

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.5 [imagenet-mobilenet\_v1\_050\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Ffca984ef-e43f-40fa-8b51-a08cbd609757)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 128x128 pixels

*  feature vector of size num_features = 512

*  size of the input images is height x width = 128 x 128 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.6 [imagenet-mobilenet\_v1\_050\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F94e358ac-4513-426d-9cb0-168a4c985ba8)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 160x160 pixels

*  feature vector of size num_features = 512

*  size of the input images is height x width = 160 x 160 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.7 [imagenet-mobilenet\_v1\_050\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fc66d9a19-c102-4ed9-a913-cf4165caed13)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 192x192 pixels

*  feature vector of size num_features = 512

*  size of the input images is height x width = 192 x 192 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.8 [imagenet-mobilenet\_v1\_050\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8c43f01d-bf62-4e71-9526-e05d6ed60179)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 224x224 pixels

*  feature vector of size num_features = 512

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.9 [imagenet-mobilenet\_v1\_075\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fdb4f3daf-ccef-4768-9f55-84f50bd13274)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 128x128 pixels

*  feature vector of size num_features = 768

*  size of the input images is height x width = 128 x 128 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.10 [imagenet-mobilenet\_v1\_075\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Ffe8d5ee8-a85d-4412-87db-5b56a0f72315)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 160x160 pixels

*  feature vector of size num_features = 768

*  size of the input images is height x width = 160 x 160 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.11 [imagenet-mobilenet\_v1\_075\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fb35bd7a7-18c4-4a92-9731-f50f6205959c)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 192x192 pixels

*  feature vector of size num_features = 768

*  size of the input images is height x width = 192 x 192 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.12 [imagenet-mobilenet\_v1\_075\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Feec28b3b-0e72-4280-ac48-56e159dc2b36)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 224x224 pixels

*  feature vector of size num_features = 768

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.13 [imagenet-mobilenet\_v1\_100\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F37f37ece-e98b-4283-a370-462e1392c60d)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 128x128 pixels

*  feature vector of size num_features = 1024

*  size of the input images is height x width = 128 x 128 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.14 [imagenet-mobilenet\_v1\_100\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fc071f984-95e4-45fa-9f00-285771a9d590)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 160x160 pixels

*  feature vector of size num_features = 1024

*  size of the input images is height x width = 160 x 160 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.15 [imagenet-mobilenet\_v1\_100\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F20a94dd6-8ea0-45df-a3eb-e0b7059ab706)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 192x192 pixels

*  feature vector of size num_features = 1024

*  size of the input images is height x width = 192 x 192 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 6.16 [imagenet-mobilenet\_v1\_100\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8eca3922-f765-4897-97d3-8a99e8ff14f5)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  feature vector of size num_features = 1024

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 7. imagenet-mobilenet\_v2

**MobileNet V2 is a family of neural network architectures for efficient on-device image classification and related tasks; Mobilenets come in various sizes controlled by a multiplier for the depth (number of features) in the convolutional layers; They can also be trained for various sizes of input images to control inference speed**

### 7.1 [imagenet-mobilenet\_v2\_035\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F41c4959a-226c-4be8-807d-561a836966a2)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 128x128 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_035_128/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.35_128/mobilenet_v2_0.35_128.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.2 [imagenet-mobilenet\_v2\_035\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fd3e7b6ae-80dd-4bee-97a2-f91fc2d21d6c)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 160x160 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_035_160/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.35_160/mobilenet_v2_0.35_160.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_160/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.3 [imagenet-mobilenet\_v2\_035\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F16532d4b-ce52-4b18-adad-50416a10922e)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 192x192 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_035_192/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.35_192/mobilenet_v2_0.35_192.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_192/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.4 [imagenet-mobilenet\_v2\_035\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8bc76c00-5f99-4894-92c6-05de3148e7ac)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 224x224 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_035_224/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.35_224/mobilenet_v2_0.35_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.5 [imagenet-mobilenet\_v2\_035\_96-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F9939bd82-37ac-4fc9-809d-d61df1891908)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 96x96 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_035_96/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.35_96/mobilenet_v2_0.35_96.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_035_96/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 96 x 96 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.6 [imagenet-mobilenet\_v2\_050\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F916a7fd4-bbac-4e6a-91f6-9e5af3e4afee)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 128x128 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_050_128/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.5_128/mobilenet_v2_0.5_128.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_128/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.7 [imagenet-mobilenet\_v2\_050\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F49b83aab-12dd-413e-928f-f85cf8b0ca3c)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 160x160 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_050_160/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.5_160/mobilenet_v2_0.5_160.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_160/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.8 [imagenet-mobilenet\_v2\_050\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Ff5db7910-0fcb-44b7-9fb6-d153ee00b8e7)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 192x192 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_050_192/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.5_192/mobilenet_v2_0.5_192.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_192/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.9 [imagenet-mobilenet\_v2\_050\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F202d7c3a-7d04-4bc9-a72e-42dcced3b0ae)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 224x224 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_050_224/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.5_224/mobilenet_v2_0.5_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_224/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.10 [imagenet-mobilenet\_v2\_050\_96-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Feb7c9518-fb2e-4dbf-934c-95d2af6f257a)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 96x96 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_050_96/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.5_96/mobilenet_v2_0.5_96.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_050_96/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 96 x 96 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.11 [imagenet-mobilenet\_v2\_075\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F88a471da-49a6-46c8-85c3-aaf5c4711d5b)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 128x128 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_075_128/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.75_128/mobilenet_v2_0.75_128.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_128/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.12 [imagenet-mobilenet\_v2\_075\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F85a2d4e2-3a0d-49c2-9365-ae12d71b0dad)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 160x160 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_075_160/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.75_160/mobilenet_v2_0.75_160.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_160/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.13 [imagenet-mobilenet\_v2\_075\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F5ca55fc5-e5ce-44bd-a562-d56ce8dc3e4a)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 192x192 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_075_192/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.75_192/mobilenet_v2_0.75_192.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_192/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.14 [imagenet-mobilenet\_v2\_075\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8bd7f50f-ac56-4f7d-848c-398d316c9838)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 224x224 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_075_224/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.75_224/mobilenet_v2_0.75_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_224/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.15 [imagenet-mobilenet\_v2\_075\_96-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8c7ef4e2-5856-4f0b-b00c-992c4ec9df8f)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 96x96 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_075_96/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_0.75_96/mobilenet_v2_0.75_96.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_075_96/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 96 x 96 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.16 [imagenet-mobilenet\_v2\_100\_128-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F9ee55fc9-cb7f-4596-9d71-1d15369a60f1)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 128x128 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_100_128/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.0_128/mobilenet_v2_1.0_128.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.17 [imagenet-mobilenet\_v2\_100\_160-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F02b5212f-978b-4038-9824-a039cc948f0f)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 160x160 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_100_160/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.0_160/mobilenet_v2_1.0_160.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_160/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.18 [imagenet-mobilenet\_v2\_100\_192-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fcdf6d95f-fd41-41e4-8cba-0f5762aa4649)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 192x192 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_100_192/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.0_192/mobilenet_v2_1.0_192.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_192/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.19 [imagenet-mobilenet\_v2\_100\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F4c463130-1956-4a25-bed2-cace34d3ff00)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_100_224/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.20 [imagenet-mobilenet\_v2\_100\_96-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F4ef65e19-ef56-42a4-87ca-5e4d47bf6027)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 96x96 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_100_96/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.0_96/mobilenet_v2_1.0_96.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1280

*  size of the input images is fixed to height x width = 96 x 96 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.21 [imagenet-mobilenet\_v2\_130\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F8db8dfc9-9a17-4fa2-b82f-e2844a93baf6)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.3 and an input size of 224x224 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_130_224/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.3_224/mobilenet_v2_1.3_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1664

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 7.22 [imagenet-mobilenet\_v2\_140\_224-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F0d6b8331-887b-455f-962f-5af5b868002f)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.4 and an input size of 224x224 pixels

*  feature vector).  The module contains a trained instance of the network, packaged to get [feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v2_140_224/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/3) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.4_224/mobilenet_v2_1.4_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1792

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 8. imagenet-nasnet

**NASNet-A is a family of convolutional neural networks for image classification. The architecture of its convolutional cells (or layers) has been found by Neural Architecture Search (NAS); NASNets come in various sizes**

### 8.1 [imagenet-nasnet\_large-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fe3caa896-0626-4fc0-b8ad-2a28bdd694eb)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation nasnet_large of NASNet-A for ImageNet that uses 18 Normal Cells, starting with 168 convolutional filters (after the "ImageNet stem"). It has an input size of 331x331 pixels

*  feature vector of size num_features = 4032

*  size of the input images is fixed to height x width = 331 x 331 pixels


References: 

* *Neural Architecture Search with Reinforcement Learning*

* *Learning Transferable Architectures for Scalable Image Recognition*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 8.2 [imagenet-nasnet\_mobile-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F2ecbe2f7-e391-426f-b591-54978231ff14)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation nasnet_mobile of NASNet-A for ImageNet that uses 12 Normal Cells, starting with 44 convolutional filters (after the "ImageNet stem"). It has an input size of 224x224 pixels

*  feature vector of size num_features = 1056

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Neural Architecture Search with Reinforcement Learning*

* *Learning Transferable Architectures for Scalable Image Recognition*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 9. imagenet-pnasnet

**PNASNet-5 is a family of convolutional neural networks for image classification; The architecture of its convolutional cells (or layers) has been found by Progressive Neural Architecture Search; PNASNet reuses several techniques from is precursor NASNet, including regularization by path dropout**

### 9.1 [imagenet-pnasnet\_large-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F352a1ce8-4289-4130-8e5b-0b6a978a3691)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation pnasnet_large of PNASNet-5 for ImageNet that uses 12 cells (plus 2 for the "ImageNet stem"), starting with 216 convolutional filters (after the stem). It has an input size of 331x331 pixels

*  feature vector of size num_features = 4320

*  size of the input images is fixed to height x width = 331 x 331 pixels


References: 

* *Progressive Neural Architecture Search*

* *Learning Transferable Architectures for Scalable Image Recognition*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed broken UPDATE_OPS for fine-tuning,

        <a href="https://github.com/tensorflow/hub/issues/86">GitHub issue 86</a>.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 10. imagenet-resnet\_v1

**ResNet (later renamed ResNet V1) is a family of network architectures for image classification with a variable number of layers**

### 10.1 [imagenet-resnet\_v1\_101-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Faf07f374-03bf-487e-bc2d-6e5596d9213f)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v1_101 with 101 layers

*  feature vector of size num_features = 2048

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *Deep Residual Learning for Image Recognition*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 10.2 [imagenet-resnet\_v1\_152-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F64fa952d-d1e1-4ba6-9b81-a061c33a8ad7)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v1_152 with 152 layers

*  feature vector of size num_features = 2048

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *Deep Residual Learning for Image Recognition*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 10.3 [imagenet-resnet\_v1\_50-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fb4e108ed-8450-426f-94fc-bffe396e4a1d)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v1_50 with 50 layers

*  feature vector of size num_features = 2048

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *Deep Residual Learning for Image Recognition*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 11. imagenet-resnet\_v2

**ResNet V2 is a family of network architectures for image classification with a variable number of layers. It builds on the ResNet architecture; The key difference compared to ResNet V1 is the use of batch normalization before every weight layer**

### 11.1 [imagenet-resnet\_v2\_101-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F4dd7a845-66db-4ac0-a4b6-b1933b1dc281)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v2_101 with 101 layers

*  feature vector of size num_features = 2048

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *Deep Residual Learning for Image Recognition*

* *Identity Mappings in Deep Residual Networks*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 11.2 [imagenet-resnet\_v2\_152-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fdb11b3e9-446e-455a-877c-9d812fe96585)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v2_152 with 152 layers

*  feature vector of size num_features = 2048

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *Deep Residual Learning for Image Recognition*

* *Identity Mappings in Deep Residual Networks*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 11.3 [imagenet-resnet\_v2\_50-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fa350eeeb-87ff-4335-9dc3-b2b7ec1db794)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v2_50 with 50 layers

*  feature vector of size num_features = 2048

*  size of the input images is height x width = 224 x 224 pixels by default


References: 

* *Deep Residual Learning for Image Recognition*

* *Identity Mappings in Deep Residual Networks*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Support for variable input size.</li>

    <li>Fine-tuning: change default batch norm momentum to 0.99 and

        make it configurable.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 12. quantops

**MobileNet V1 is a family of neural network architectures for efficient on-device image classification; Mobilenets come in various sizes controlled by a multiplier for the depth (number of features) in the convolutional layers; They can also be trained for various sizes of input images to control inference speed; The implementation is instrumented for quantization**

### 12.1 [imagenet-mobilenet\_v1\_025\_128-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Ff5f87ef8-0b36-4d85-9664-8fc6a7e4fc0f)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 128x128 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_025_128/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.25_128_quant/mobilenet_v1_0.25_128_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_128/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 256

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.2 [imagenet-mobilenet\_v1\_025\_160-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F7d9362ba-5f53-44b2-acdc-131691e23e29)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 160x160 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_025_160/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160_quant/mobilenet_v1_0.25_160_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_160/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 256

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.3 [imagenet-mobilenet\_v1\_025\_192-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F4e39382a-955f-438e-b5bd-9c45df0c50d3)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 192x192 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_025_192/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.25_192_quant/mobilenet_v1_0.25_192_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_192/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 256

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.4 [imagenet-mobilenet\_v1\_025\_224-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F9ad83825-4d7d-4729-9aba-e1657cf82955)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 224x224 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_025_224/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224_quant/mobilenet_v1_0.25_224_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_025_224/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 256

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.5 [imagenet-mobilenet\_v1\_050\_128-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F5ca67ec2-8aae-43a1-aa60-c14a7469d50c)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 128x128 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_050_128/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.5_128_quant/mobilenet_v1_0.5_128_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_128/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 512

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.6 [imagenet-mobilenet\_v1\_050\_160-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Ff71d5c2a-fc77-44cd-9ec7-b17a68595ac5)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 160x160 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_050_160/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160_quant/mobilenet_v1_0.5_160_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 512

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.7 [imagenet-mobilenet\_v1\_050\_192-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F1e335893-c2c1-443f-be23-04240fbc7839)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 192x192 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_050_192/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.5_192_quant/mobilenet_v1_0.5_192_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_192/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 512

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.8 [imagenet-mobilenet\_v1\_050\_224-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fbe53911c-ce9f-4bc0-b229-3783fd7eb516)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 224x224 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_050_224/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224_quant/mobilenet_v1_0.5_224_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_050_224/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 512

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.9 [imagenet-mobilenet\_v1\_075\_128-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fb4168dee-fc60-4983-9342-82df37168fef)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 128x128 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_075_128/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.75_128_quant/mobilenet_v1_0.75_128_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_128/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 768

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.10 [imagenet-mobilenet\_v1\_075\_160-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F30ed3255-649b-4d5d-8eab-4e2d1ea20a90)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 160x160 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_075_160/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.75_160_quant/mobilenet_v1_0.75_160_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_160/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 768

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.11 [imagenet-mobilenet\_v1\_075\_192-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F189a3dd7-35ea-4a53-ab2c-746396b884cb)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 192x192 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_075_192/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.75_192_quant/mobilenet_v1_0.75_192_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_192/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 768

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.12 [imagenet-mobilenet\_v1\_075\_224-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fa41b9636-3ef7-421a-8594-d46037d1f0d6)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 224x224 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_075_224/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_0.75_224_quant/mobilenet_v1_0.75_224_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_075_224/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 768

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.13 [imagenet-mobilenet\_v1\_100\_128-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fffd67803-8128-49d5-a310-896ccbfda23b)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 128x128 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_100_128/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_1.0_128_quant/mobilenet_v1_1.0_128_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_128/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1024

*  size of the input images is fixed to height x width = 128 x 128 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.14 [imagenet-mobilenet\_v1\_100\_160-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2F16f425f5-53ad-43a4-9fb2-b454e7dd611d)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 160x160 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_100_160/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160_quant/mobilenet_v1_1.0_160_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_160/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1024

*  size of the input images is fixed to height x width = 160 x 160 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.15 [imagenet-mobilenet\_v1\_100\_192-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Fe519e11e-8155-46b6-892e-86e39a9af2cd)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 192x192 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_100_192/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_1.0_192_quant/mobilenet_v1_1.0_192_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_192/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1024

*  size of the input images is fixed to height x width = 192 x 192 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

### 12.16 [imagenet-mobilenet\_v1\_100\_224-quantops-feature\_vector@3](https://aihub.cloud.google.com/p/products%2Faaf6a352-ad6b-4769-a4cc-f237465fd989)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/imagenet/mobilenet_v1_100_224/quantops/classification/3](https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/quantops/classification/3) instead.   ## Quantization  This module is meant for use in models whose weights will be quantized to uint8 by [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) for deployment to mobile devices.  The trained weights of this module are shipped as float32 numbers, but its graph has been augmented by tf.contrib.quantize with extra ops that simulate the effect of quantization already during training, so that the model can adjust to it.  ## Training  The checkpoint exported into this module was mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224_quant/mobilenet_v1_1.0_224_quant.ckpt downloaded from [MobileNet pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet"), with simulated quantization.  ## Usage  This module implements the common signature for computing [image feature vectors](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). It can be used like  python module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/quantops/feature_vector/3") height, width = hub.get_expected_image_size(module) images = ...  # A batch of images with shape [batch_size, height, width, 3]. features = module(images)  # Features with shape [batch_size, num_features].   ...or using the signature name image_feature_vector. The output for each image in the batch is a feature vector of size num_features = 1024

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Avoids crash in some TFLite/toco versions

        (<a href="https://github.com/tensorflow/hub/issues/109">GitHub issue 109</a>)

        by overestimating quantization boundaries on input image by 0.05%.</li>

    <li>Requires PIP package <code>tensorflow-hub&gt;=0.2.0</code>.</li>

    </ul>

## 13. tf2-preview-inception\_v3

**SavedModel 2.0 format; help preview TensorFlow 2.0 functionality; Inception V3 is a neural network architecture for image classification**

### 13.1 [tf2-preview-inception\_v3-feature\_vector@4](https://aihub.cloud.google.com/p/products%2Fe62c7c51-d7bc-4611-8208-0afc7742a3fc)


Module Description: 

* feature vector has size num_features = 2048

*  size of the input images is fixed to height x width = 299 x 299 pixels


References: 

* *Rethinking the Inception Architecture for Computer Vision*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed missing default <code>trainable=False</code>.</li>

    <li>Fixed broken regularization_losses.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Provides proper names for variables, fixing crash in <code>Model.save()</code>

        (<a href="https://github.com/tensorflow/hub/issues/287">GitHub issue #287</a>).</li>

    </ul>

    <h4>Version 4</h4>

    <ul>

    <li>Adds back missing update ops for batch norm that were lost in version 3,

        (<a href="https://github.com/tensorflow/hub/issues/304">GitHub issue #304</a>).</li>

    </ul>

## 14. tf2-preview-mobilenet\_v2

**SavedModel 2.0 format; help preview TensorFlow 2.0 functionality; MobileNet V2 is a family of neural network architectures for efficient on-device image classification and related tasks; Mobilenets come in various sizes controlled by a multiplier for the depth (number of features) in the convolutional layers; They can also be trained for various sizes of input images to control inference speed**

### 14.1 [tf2-preview-mobilenet\_v2-feature\_vector@4](https://aihub.cloud.google.com/p/products%2Fbf481eb3-6f51-40f8-8a59-3b68c36bf54a)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  feature vectors from images](https://www.tensorflow.org/hub/common_signatures/images#feature-vector). If you want the full model including the classification it was originally trained for, use module [google/tf2-preview/mobilenet_v2/classification/4](https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4) instead.   ## Training  The checkpoint exported into this module was mobilenet_v2_1.0_224/mobilenet_v2_1.0_224.ckpt downloaded from [MobileNet V2 pre-trained models](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md). Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").  ## Usage  This module can be used with the hub.KerasLayer as follows:  python m = tf.keras.Sequential([     hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4", output_shape=[1280],                    trainable=False),  # Can be True, see below.     tf.keras.layers.Dense(num_classes, activation='softmax') ]) m.build([None, 224, 224, 3])  # Batch input shape.   The output of the module is a batch of feature vectors. For each input image, the feature vector has size num_features = 1280

*  size of the input images is fixed to height x width = 224 x 224 pixels


References: 

* *Inverted Residuals and Linear Bottlenecks: Mobile Networks for Classification, Detection and Segmentation*


Changelog: 

    <h4>Version 1</h4>

    <ul>

    <li>Initial release.</li>

    </ul>

    <h4>Version 2</h4>

    <ul>

    <li>Fixed missing default <code>trainable=False</code>.</li>

    <li>Fixed broken regularization_losses.</li>

    </ul>

    <h4>Version 3</h4>

    <ul>

    <li>Provides proper names for variables, fixing crash in <code>Model.save()</code>

        (<a href="https://github.com/tensorflow/hub/issues/287">GitHub issue #287</a>).</li>

    </ul>

    <h4>Version 4</h4>

    <ul>

    <li>Adds back missing update ops for batch norm that were lost in version 3,

        (<a href="https://github.com/tensorflow/hub/issues/304">GitHub issue #304</a>).</li>

    </ul>

