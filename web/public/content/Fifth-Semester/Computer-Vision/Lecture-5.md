- **Key Ideas:**
    - Nearby pixels are related
    - Same patterns appear everywhere (edges, corners)
    - **Sparse connections**: Not fully connected and have **local connectivity**
    - **Weight sharing**: Reuse the same wights (Numbers in matrix) of filters (Kernels) across the image
        - **Local Connected networks**: Have sparse connections but do not share weights but **CNN** have both
        - We have multiple filters to learn different features but each filter has its own weights shared across the image
        - **Stride**: How much we move the filter at each step (Usually 1, stride make **downsampling** and skip pixels)
            - We can replace by **Pooling** for downsampling
        - **Dilated convolution**: We add 0 between filter weights to increase receptive field without pooling which reduces details
    - **Pooling**: Downsampling to reduce dimensions and computation
    - **Padding**: Without padding image shrinks after each conv, so we often use **zero padding** to keep spatial size

### Composing layers
- **Convolutional layer**: Apply multiple filters to input to produce feature maps
- **Activation function**: Non-linearity like ReLU after conv layer
- **Pooling layer**: Downsample feature maps (Max pooling, Average pooling)
    - **Max pooling**: Take max value in each region
    - **Mean pooling**: Take average value in each region
- **Fully connected layer**: At the end to make final predictions

If we do only `conv + ReLU` the networks sees local patterns but not global patterns. By **Pooling + downsampling** and stacking **multiple conv** layers, the network can learn hierarchical features from local to global which helps **generalization**.

Order is usually: `[Conv -> ReLU -> Downsample] x N -> [FC -> ReLU] x M -> Output Layer`

**Dropout** removes random neurons during training to prevent overfitting and other neuron learn better features.


1x1 convolutions reduce channels.

- **History**:
    - **LeNet**: Early CNN for digit recognition on MNIST, with backpropagation, FC, pooling and sigmoid/tanh activations
    - **AlexNet**: Deeper CNN with ReLU, dropout, used GPU, trained on ImageNet, pooling, 3 FC 5 Conv -> pool,pool,conv,conv,pool,FC,FC,FC
        - **ImageNet**: Large dataset with 1.2M images, 1000 classes
    - **VGG**: Very deep CNN with 16-19 layers, small 3x3 filters, more depth improves performance

- **Deep Networks Problem**:
    - **Vanishing gradients**: Gradients get smaller in deep networks, making training hard
    - **Unstable training**
    - **Solution**: 
        - **Weight initialization**:
            - Xavier initialization: For tanh/sigmoid activations, keep variance of activations same across layers
                - Xavier with ReLU: Kills half the variance and shrink it
            - Kaiming (He) initialization: For ReLU activations, keep variance of activations same across layers $\to$ used in modern CNNs
            - Random initialization: For ReLU activations, use He initialization to keep variance
        - **Normalization**
            - Makes different layers have same train speed
            - Stabilizes training
            - Let us use higher learning rates
            - Force activation to have mean = 0 and variance = 1
            - Done during training
                - **Batch Normalization**: Normalize across batch dimension, Normalize per feature
        - **Residual connections**: Skip connections to help gradients flow better (ResNet) because deeper nets perform worst
            - **Basic Block**: 2 conv layers with ReLU and a skip connection
            - **Bottleneck Block**: 1x1, 2x2, 3x3 conv layers with skip connection to reduce computation

- **Practical details**
    - **Rectangular images**: Resize and crop centered
    - **Data augmentation**: flipping, cropping, noise