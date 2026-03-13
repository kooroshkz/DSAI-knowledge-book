### **CNN Dataset Loading**

**Normalize in transformation** helps model to compute less and converge faster by normalizing the input data from [0, 255] to [-1, 1] in image classification tasks.

Formula for normalization:
$x' = \frac{x - \mu}{\sigma}$

```python
transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), # First tuple is mean and second is std deviation
```
---

```python
train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
```

**Batch size** is the number of samples passed through the network at once. The larger the batch size need more memory.

**Shuffle** is used to shuffle the data at every epoch to prevent the model from learning the order of the data.

---

### **CNN Implementation**

```python
self.conv_layer1 = nn.Sequential(
    nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
    nn.BatchNorm2d(64),
    nn.ReLU(),
)  # 3 input channels, 64 output channels
```
- **3** is the number of input channels (RGB) and **64** is the number of output channels, feature maps that represent different patterns detected in the image like edges, textures, or shapes.
- **Kernel** filter applied to the input image. The kernel size is 3x3, which means the filter will be 3 pixels wide and 3 pixels tall.
    - Kernal can be like

$$\begin{bmatrix} 1 & 0 & -1 \\ 1 & 0 & -1 \\ 1 & 0 & -1 \end{bmatrix}$$

for edge detection.
- **Stride** is the number of pixels by which the filter moves across the image. A stride of 1 means the filter moves one pixel at a time.
- **Padding** adds extra pixels (typically zeros) around the input image before applying the convolution which ensures that the edge pixels are not lost after the convolution operation.
- **BatchNorm2d** normalizes the output of the convolutional layer.

### Max Pooling

Max pooling reduces the size of the feature map and helps with computational efficiency while keeping the most important features.

- `stride=2`: The window (kernel with size 2x2) moves 2 steps at a time, halving the size of the output feature map.

<img src="https://www.bouvet.no/bouvet-deler/understanding-convolutional-neural-networks-part-1/_/attachment/inline/dc21d536-4088-4318-9e19-52142537ae76:f9a0fe3d64373139b3158fde9a65b0b0f21039a4/Screenshot%202019-07-01%20at%2013.42.55.png" width="400px">
<img src="https://media.licdn.com/dms/image/v2/C5112AQFli1PZInreVg/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1582176329742?e=1749686400&v=beta&t=GtoBP34w59E5l_A3XTGjekZc4rUNSOHeKKPsl-yTt8U" width="400px">

---

### **CNN Train**

- **Gradients** how much the loss (error) changes when the model's parameters (weights) change. Tell the model how to adjust its weights to make better predictions.

- **Backpropagation** is the process of calculating the error, finding out how each weight contributed to the error, and updating the weights to reduce that error.
