- **Temporal filtering**: Gilters work on time, same pixel location across multiple frames. Can: Remove background, Find moving objects, Detect subtle changes
    - **Examples**:
        - **Temporal Median Filter**: For each pixel location, take the median value across a sequence of frames to reduce noise and highlight moving objects.
        - **Temporal Gaussian Filter**: Apply a Gaussian filter over time to smooth out rapid changes while preserving slower movements.
        - **Background Subtraction**
        - **Subtle color change**: Detect slight variations in color over time by analyzing pixel intensity changes across frames.
        - **Motion magnification**: Amplify small motions in a video sequence by applying temporal filtering to enhance subtle movements.
    - **Use cases and tasks**:
        - **Action recognition** $\to$ input video output action label
        - **Action detection**
        - **Action anticipation**
        - **Anomaly detection**
        - **Tracking**
        - **Video Segmentation**

**CNN** fails as by **Single frame** we miss motion and **Multiple frames + averaging** loses motion and order.

We can use CNN but finetune for video by freezing CNN, train classifier only. We can add **weights** to frames based on importance (**Attention**) but still have limitations:
- modeling motion
- understanding direction
- long actions

**Feature fusion**: Instead averaging, concatenate features from multiple frames then MLP but still weak in motion and have fixed temporal window.

- **3D CNN**: Extend 2D convolution to 3D convolution by adding temporal dimension. Convolve in space and time simultaneously. Can capture motion and spatial features together. But having high cost and hard to train.
- **Inflated Convolutions (I3D)**: Copy 2D filter across time (Inflate) and normalize weights.
- **Optical Flow**: Compute pixel displacement between frames to capture motion information. Use as additional input to CNN along with RGB frames.
    - **Optical Flow + CNN**: Compute optical flow and feed flow into CNN using **RGB stream** for appearance or **Flow stream** for motion then **fuse predictions**.

**Aperture problem**: In small window, motion direction is ambiguous. We can use patches and neighbors.

- **RNN**: Process video and keep a hidden state (Memory) to capture temporal dependencies.
    - **Vanilla RNN**: Forget information and gradients vanish/explode, hard to learn long actions.
- **LSTM**: Designed not to forget with memory cells and gates to control information flow. Better for long-term dependencies. Problems: Slow, sequential and not parallelizable, hard to scale and weak motion modeling.

| Model        | Works On                     | Pros                                                                 | Cons                                                                 |
|--------------|-------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| CNN          | Multidimensional grids        | Parallel computation, fast training                                  | Bad for long sequences, needs many layers to see full sequence       |
| RNN          | Ordered sequences             | Good for long sequences, hidden state can see past inputs            | Not parallel, slow, very deep, limited expressive power              |
| Transformer  | Sets of vectors               | Very good for long sequences, full context with self-attention, fast | High memory use, O(N²) without changes                                |
---

- **Distribution shifts**: Training and testing data come from different distributions.
- **Transfer learning**: Pretrain on large dataset, finetune on target dataset. Helps when target dataset is small.
- **Representation**: Features inside network, activations/embedding, weights and biases. Good ones: capture edges,textures,shapes,objects useful across many tasks.
    - **Why important?**: reduce labeling cost, adapt to new tasks and domain, scale better
    - **Test (Linear Probing)**: Freeze network, remove last layer, add a linear classifier, train only classifier on target task.
- **Finetune** for **Dimension missmatch**: Remove last layer, add new ine with correct size (Early layers capture general features, later layers more task specific).
- **Self supervised learning**: turn unlabeled data into a supervised problem by creating labels from the data itself. Usecases:    
    - Denoising autoencoder (Noise $\to$ Clean image)
    - Colorization (Learns object identity and sematics for better autoencoders)
- **Masked Autoencoders (MAE)**: mask a large portion and force samntic undrestanding. Steps: Split image into patches, Randomly mask most patches, Encode only visible patches and mask tokens, predict missing patches, compute pixel loss. If dont predict, can learn representations by computing view similarity (**Contrastive learning**).
- **Contrastive learning**: Learn representations by bringing similar samples closer and pushing dissimilar samples apart in feature space.
    - take image, apply two random augmentations, treat as positive pair, other images as negative samples.
    - **loss**: pulls positives together pushes negatives apart, minimize when same image views are close and different images are far builds invariance and semantic structure.
        - **SimCLR**: Use strong augmentations, contrastive loss and simple architecture making better transfer and closer to supervised learning.

- **MAE** (Most Common): Best avg performance, simple, scalable
- **Contrastive learning**: Better for fine-grained tasks, works well with multilodal data and needs fewer finetuning data.

