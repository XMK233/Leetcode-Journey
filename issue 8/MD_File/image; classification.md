## 1. imagenet-amoebanet

**AmoebaNet is a family of convolutional neural networks for image classification; The architectures of its convolutional cells (or layers) have been found by an evolutionary architecture search in the NASNet search space**

### 1.1 [imagenet-amoebanet\_a\_n18\_f448-classification@1](https://aihub.cloud.google.com/p/products%2F689e685a-a1d1-494c-bec8-d7c4b1c6178a)


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

### 2.1 [imagenet-inception\_resnet\_v2-classification@3](https://aihub.cloud.google.com/p/products%2F09208f7a-acf0-4ade-ab03-9b050e7a5a05)


Module Description: 

* 1001 classes of the classification from the original training

*  size of the input images is height x width = 299 x 299 pixels by default


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

### 3.1 [imagenet-inception\_v1-classification@3](https://aihub.cloud.google.com/p/products%2F7fecf7df-1263-4a82-bf39-ca3022b2d43e)


Module Description: 

* num_classes = 1001 classes of the classification from the original training

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

### 4.1 [imagenet-inception\_v2-classification@3](https://aihub.cloud.google.com/p/products%2F38e02e43-d7b5-4ff8-98c2-ec174f69e218)


Module Description: 

* num_classes = 1001 classes of the classification from the original training

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

### 5.1 [imagenet-inception\_v3-classification@3](https://aihub.cloud.google.com/p/products%2Fb96c2a1f-9304-49f2-8556-544cf5542ef0)


Module Description: 

* num_classes = 1001 classes of the classification from the original training

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

### 6.1 [imagenet-mobilenet\_v1\_025\_128-classification@3](https://aihub.cloud.google.com/p/products%2F2e357bad-a058-4de8-b239-7a5f1058dabb)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.2 [imagenet-mobilenet\_v1\_025\_160-classification@3](https://aihub.cloud.google.com/p/products%2Faf498bc9-9b4f-4919-ae40-193d3e6f7203)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.3 [imagenet-mobilenet\_v1\_025\_192-classification@3](https://aihub.cloud.google.com/p/products%2Fb23c2250-dee1-4459-9ac6-8c327ca92fdc)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.4 [imagenet-mobilenet\_v1\_025\_224-classification@3](https://aihub.cloud.google.com/p/products%2F93839d48-c253-4ea8-83a3-d54547092bfb)


Module Description: 

* TF-Slim implementation of mobilenet_v1_025 with a depth multiplier of 0.25 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.5 [imagenet-mobilenet\_v1\_050\_128-classification@3](https://aihub.cloud.google.com/p/products%2F80eba1e9-cab6-4bc4-8618-59ed39f539fb)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.6 [imagenet-mobilenet\_v1\_050\_160-classification@3](https://aihub.cloud.google.com/p/products%2F3b2b0bb1-3328-4391-999d-99da1adc16f3)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.7 [imagenet-mobilenet\_v1\_050\_192-classification@3](https://aihub.cloud.google.com/p/products%2Fc4b35f6b-82d8-4e76-aba2-9f9e18fe6c06)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.8 [imagenet-mobilenet\_v1\_050\_224-classification@3](https://aihub.cloud.google.com/p/products%2F7578eb13-6458-4796-80fa-86d68e4cc092)


Module Description: 

* TF-Slim implementation of mobilenet_v1_050 with a depth multiplier of 0.5 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.9 [imagenet-mobilenet\_v1\_075\_128-classification@3](https://aihub.cloud.google.com/p/products%2F34c8ee65-d4fe-4234-a3f4-7d18c404c479)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.10 [imagenet-mobilenet\_v1\_075\_160-classification@3](https://aihub.cloud.google.com/p/products%2Feb982d0a-f086-4408-875c-dce5d8272fab)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.11 [imagenet-mobilenet\_v1\_075\_192-classification@3](https://aihub.cloud.google.com/p/products%2F2d0403f6-c7bf-4f87-a8aa-fd04c96d17c3)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.12 [imagenet-mobilenet\_v1\_075\_224-classification@3](https://aihub.cloud.google.com/p/products%2Fe3a910da-c3bd-4bc8-94fb-f941e9fa0e50)


Module Description: 

* TF-Slim implementation of mobilenet_v1_075 with a depth multiplier of 0.75 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.13 [imagenet-mobilenet\_v1\_100\_128-classification@3](https://aihub.cloud.google.com/p/products%2Ffb69f59b-0dfa-4fda-a8f0-66b0e4c9fd7b)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.14 [imagenet-mobilenet\_v1\_100\_160-classification@3](https://aihub.cloud.google.com/p/products%2Fc7a49fbc-5f83-49a4-beb3-a726efc7cc69)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.15 [imagenet-mobilenet\_v1\_100\_192-classification@3](https://aihub.cloud.google.com/p/products%2Ffcd3da5a-fe3d-4a6a-a56f-f476f7449bb4)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 6.16 [imagenet-mobilenet\_v1\_100\_224-classification@3](https://aihub.cloud.google.com/p/products%2Fff23bf1c-5c35-40b0-95cb-86b7cc6f15e6)


Module Description: 

* TF-Slim implementation of mobilenet_v1 with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.1 [imagenet-mobilenet\_v2\_035\_128-classification@3](https://aihub.cloud.google.com/p/products%2F13041a34-cc37-4e4f-bd04-ac0bd5156e68)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.2 [imagenet-mobilenet\_v2\_035\_160-classification@3](https://aihub.cloud.google.com/p/products%2Fe7ca0182-26a9-431b-897f-48e5cf9f1c1a)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.3 [imagenet-mobilenet\_v2\_035\_192-classification@3](https://aihub.cloud.google.com/p/products%2F613b1e96-3dcf-4a97-93aa-b491d164c3d9)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.4 [imagenet-mobilenet\_v2\_035\_224-classification@3](https://aihub.cloud.google.com/p/products%2F1b4c3f06-200f-4116-a5e3-4cefc5799c63)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.5 [imagenet-mobilenet\_v2\_035\_96-classification@3](https://aihub.cloud.google.com/p/products%2F7097ed9b-8957-4b28-a2a9-4bbf22bd0462)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.35 and an input size of 96x96 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.6 [imagenet-mobilenet\_v2\_050\_128-classification@3](https://aihub.cloud.google.com/p/products%2Fed2f3c46-8251-4160-abce-c9e1e05e6ef1)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.7 [imagenet-mobilenet\_v2\_050\_160-classification@3](https://aihub.cloud.google.com/p/products%2Fbb1f7123-166f-4fa5-b71d-0d36045a82f8)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.8 [imagenet-mobilenet\_v2\_050\_192-classification@3](https://aihub.cloud.google.com/p/products%2F98d0512a-3f5a-46ac-b4d9-0e923f9462eb)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.9 [imagenet-mobilenet\_v2\_050\_224-classification@3](https://aihub.cloud.google.com/p/products%2F40682478-2573-40f6-bd1f-4bd3882e9dea)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.10 [imagenet-mobilenet\_v2\_050\_96-classification@3](https://aihub.cloud.google.com/p/products%2Fb8f781b4-7733-4238-a89a-b94c5903d44e)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.5 and an input size of 96x96 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.11 [imagenet-mobilenet\_v2\_075\_128-classification@3](https://aihub.cloud.google.com/p/products%2F401734b5-e64d-4a7f-8044-25c8cf8a975a)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.12 [imagenet-mobilenet\_v2\_075\_160-classification@3](https://aihub.cloud.google.com/p/products%2F15f65f21-50d2-4869-baa0-cfced0e744c2)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.13 [imagenet-mobilenet\_v2\_075\_192-classification@3](https://aihub.cloud.google.com/p/products%2F0396a9ca-de5c-4a7f-9aa6-4f04aaff118d)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.14 [imagenet-mobilenet\_v2\_075\_224-classification@3](https://aihub.cloud.google.com/p/products%2Fcb908573-5a9d-44e0-a406-08c6e847d898)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.15 [imagenet-mobilenet\_v2\_075\_96-classification@3](https://aihub.cloud.google.com/p/products%2Fe008f1ac-7f58-4ddf-bcc2-aaa396c9f3fc)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 0.75 and an input size of 96x96 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.16 [imagenet-mobilenet\_v2\_100\_128-classification@3](https://aihub.cloud.google.com/p/products%2Fa99e7ea9-4cfb-4789-89aa-375c94c6dcdb)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.17 [imagenet-mobilenet\_v2\_100\_160-classification@3](https://aihub.cloud.google.com/p/products%2F582ec440-e350-4611-9a72-3bb3b949f457)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.18 [imagenet-mobilenet\_v2\_100\_192-classification@3](https://aihub.cloud.google.com/p/products%2Fc122c154-deed-42e6-be7f-558615fa50a6)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.19 [imagenet-mobilenet\_v2\_100\_224-classification@3](https://aihub.cloud.google.com/p/products%2F5ea70ed9-9bd7-41e5-898f-e1509e8793bd)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.20 [imagenet-mobilenet\_v2\_100\_96-classification@3](https://aihub.cloud.google.com/p/products%2F48b59149-3590-4994-9256-3fe434a827b3)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 96x96 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.21 [imagenet-mobilenet\_v2\_130\_224-classification@3](https://aihub.cloud.google.com/p/products%2F87265e6e-af6c-4071-957f-01b8c9afc719)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.3 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 7.22 [imagenet-mobilenet\_v2\_140\_224-classification@3](https://aihub.cloud.google.com/p/products%2Ff4500342-7736-49e9-93b2-1535b377109f)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.4 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 8.1 [imagenet-nasnet\_large-classification@3](https://aihub.cloud.google.com/p/products%2F2f3d31d4-66ef-4fb9-8d48-075f462ffe9b)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation nasnet_large of NASNet-A for ImageNet that uses 18 Normal Cells, starting with 168 convolutional filters (after the "ImageNet stem"). It has an input size of 331x331 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 8.2 [imagenet-nasnet\_mobile-classification@3](https://aihub.cloud.google.com/p/products%2F368aeea6-767b-43a7-a531-13a95b5bd895)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation nasnet_mobile of NASNet-A for ImageNet that uses 12 Normal Cells, starting with 44 convolutional filters (after the "ImageNet stem"). It has an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 9.1 [imagenet-pnasnet\_large-classification@3](https://aihub.cloud.google.com/p/products%2F46974972-0006-4fd5-8dc8-2f68ab53a378)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation pnasnet_large of PNASNet-5 for ImageNet that uses 12 cells (plus 2 for the "ImageNet stem"), starting with 216 convolutional filters (after the stem). It has an input size of 331x331 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 10.1 [imagenet-resnet\_v1\_101-classification@3](https://aihub.cloud.google.com/p/products%2Ff3cabfdf-b54d-47b4-8e89-036ef39658fa)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v1_101 with 101 layers

*  num_classes = 1001 classes of the classification from the original training

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

### 10.2 [imagenet-resnet\_v1\_152-classification@3](https://aihub.cloud.google.com/p/products%2F76a23fa7-e450-46c0-8a7a-deb0b6d0d8af)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v1_152 with 152 layers

*  num_classes = 1001 classes of the classification from the original training

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

### 10.3 [imagenet-resnet\_v1\_50-classification@3](https://aihub.cloud.google.com/p/products%2F67033c91-b2ee-43cc-9c7a-fbe0550b88d8)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v1_50 with 50 layers

*  num_classes = 1001 classes of the classification from the original training

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

### 11.1 [imagenet-resnet\_v2\_101-classification@3](https://aihub.cloud.google.com/p/products%2F4d580b21-7dce-4d2a-a240-f61cb76a75cb)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v2_101 with 101 layers

*  num_classes = 1001 classes of the classification from the original training

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

### 11.2 [imagenet-resnet\_v2\_152-classification@3](https://aihub.cloud.google.com/p/products%2F30e3d1be-cece-4c09-9a7c-03c6841a5f41)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v2_152 with 152 layers

*  num_classes = 1001 classes of the classification from the original training

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

### 11.3 [imagenet-resnet\_v2\_50-classification@3](https://aihub.cloud.google.com/p/products%2F9f12fca3-c88a-4548-9c29-d875af05f22b)


Module Description: 

* This TF-Hub module uses the TF-Slim implementation of resnet_v2_50 with 50 layers

*  num_classes = 1001 classes of the classification from the original training

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

### 12.1 [imagenet-mobilenet\_v1\_025\_128-quantops-classification@3](https://aihub.cloud.google.com/p/products%2Fc66937a1-5ef0-4b23-aa9d-7c49097d19c5)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.2 [imagenet-mobilenet\_v1\_025\_160-quantops-classification@3](https://aihub.cloud.google.com/p/products%2Fb2c8e4bf-a4aa-404c-8cae-525a9944182a)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.3 [imagenet-mobilenet\_v1\_025\_192-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F8b75406e-47e4-4261-bd0f-9fdf32ee329d)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.4 [imagenet-mobilenet\_v1\_025\_224-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F848e4116-1803-49ba-9c74-23365d448428)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_025, instrumented for quantization, with a depth multiplier of 0.25 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.5 [imagenet-mobilenet\_v1\_050\_128-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F0dc0d585-1ff5-4501-b9ce-5a0dd183d41b)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.6 [imagenet-mobilenet\_v1\_050\_160-quantops-classification@3](https://aihub.cloud.google.com/p/products%2Fefbecded-bb7e-4d95-a784-35c09efb84fc)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.7 [imagenet-mobilenet\_v1\_050\_192-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F558058fe-0d24-4bdc-a4b5-739ca7adb7b5)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.8 [imagenet-mobilenet\_v1\_050\_224-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F711fda69-6f28-40e7-84bc-bd9f811a1eb8)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_050, instrumented for quantization, with a depth multiplier of 0.5 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.9 [imagenet-mobilenet\_v1\_075\_128-quantops-classification@3](https://aihub.cloud.google.com/p/products%2Fc2480cdc-afac-4f50-b222-0988427d84ed)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.10 [imagenet-mobilenet\_v1\_075\_160-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F83a5c631-0c56-40e7-93f2-d34831f317c1)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.11 [imagenet-mobilenet\_v1\_075\_192-quantops-classification@3](https://aihub.cloud.google.com/p/products%2Fa455648c-ccd4-46ad-a743-fa6f82d96a5c)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.12 [imagenet-mobilenet\_v1\_075\_224-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F4a5326c3-a371-4609-b8c7-05d10719b171)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1_075, instrumented for quantization, with a depth multiplier of 0.75 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.13 [imagenet-mobilenet\_v1\_100\_128-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F527e439e-fc16-4419-bdbb-caf7f247009e)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 128x128 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.14 [imagenet-mobilenet\_v1\_100\_160-quantops-classification@3](https://aihub.cloud.google.com/p/products%2Ffe2a7857-566b-45b9-bc85-22e2f90f8904)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 160x160 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.15 [imagenet-mobilenet\_v1\_100\_192-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F99959f36-5676-4fcf-af54-42adc89d2cce)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 192x192 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 12.16 [imagenet-mobilenet\_v1\_100\_224-quantops-classification@3](https://aihub.cloud.google.com/p/products%2F0940e0bd-5d4c-44ae-b51b-f48a93109166)


Module Description: 

* TF-Slim implementation of mobilenet_v1_v1, instrumented for quantization, with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

### 13.1 [tf2-preview-inception\_v3-classification@4](https://aihub.cloud.google.com/p/products%2Fe58473e0-fbf7-40bd-9cea-917e3471ce2b)


Module Description: 

* num_classes = 1001 classes of the classification from the original training

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

### 14.1 [tf2-preview-mobilenet\_v2-classification@4](https://aihub.cloud.google.com/p/products%2Fea5d2e6b-5ebe-4c14-a38a-5b9c10f542d2)


Module Description: 

* TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 224x224 pixels

*  num_classes = 1001 classes of the classification from the original training

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

