* **Benchmark Datasets**
  * **MNIST**: 28×28 grayscale images of handwritten digits (60k train, 10k test)
  * **CIFAR-10**: 32×32 RGB images, 10 classes, 50k train, 10k test (Dogs, Cats, Cars, etc.)
  * **CIFAR-100**: Similar to CIFAR-10 but with 100 classes, 600 images per class.
  * **ImageNet**: Large dataset with 1.2 million images, 1000 classes (e.g., animals, objects).
* **Naïve Approach**: Fully Connected Network on Flattened Images (N, 1)

* **Stride**: How much the filter (kernel) moves at each step (usually 1 pixel).
- **Padding**: Padding adds zeros around image edges. Prevents loss of information at borders.
* **Output feature map**: Result of applying filter to input.
* For multi-channel images (RGB), apply filter to each channel separately and sum results.
* Multiple filters learn multiple features simultaneously.
* **Pooling**: Reduces size of feature maps, retains important information, and remove noise. (Like kernel but take max or average in a window)
  * **Max pooling:** Take max value in window.
  * **Average pooling:** Take average value.
* For **non-linearity**, use activation functions like ReLU Helps CNNs learn complex patterns.
- **CNN Examples:** Famous Architectures
  * **LeNet-5 (1989):** First successful CNN, for handwritten digit recognition.
  * **AlexNet (2012):** Won ImageNet challenge, popularized deep CNNs.
  * **VGG (2014):** Very deep CNNs with simple 3×3 filters.
- **Vanishing Gradient Problem**: Deeper CNNs can suffer tiny gradients in early layers. $\to$ Solution: **Residual Networks (ResNet)** $\to$ ResNet uses **skip connections** (shortcut paths) to allow gradients to flow directly.