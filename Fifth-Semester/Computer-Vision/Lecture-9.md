- **Transformers** build upon:
    - **Tokens**: vectores $\to$ for image $\to$ flaten patches turn to vectors
    - **Attention Mechanism**: Finds relevant tokens and combines them in a new representation
        - Each token transformed into three vectors: Query (What looking at), Key (What contains), Value (What information to give)
        - Compare query with all keys to get similarity scores and turn scores to weights to weight vectors\
        - **Self-Attention**: when Query, Key, Value come from the same tokens, every patch can look at every other patch
            - Links distant image regions, models global structure, undrestand relationships and helps with counting, comparison and layout
            - CNN do this slowly through depth but transformers do it in one step
            - **Multi-Head Attention**: multiple attention mechanisms in parallel to capture different relationships (shape,color,texture) and output is combined
    - **Positional Encoding**: Adds information about the position of tokens in the sequence (Transformers are **Permutation equivariant:**) can be learned, sinusoidal or Fourier-based

- **Vision Transformer (ViT)**: Split image into patches, project patches to tokens, add positional encodings, pass through transformer layers (multi-head self-attention + MLP), classify with a special [CLS] classification

- **Transformers**: global context, weak inductive bias, need more data, memory heavy (attention is O(N²)), great for multimodal learning
- **CNNs**: strong inductive bias (locality), work well with less data, efficient, harder to model long-range relations

- **Transformers for video**: Split each frame into patches, add temporal/spatial positional encodings, tokens now represnt space-time chunks
    - Full attention over space and time is expensive so:
    - **Structured Attention**: space-only or time-only attention in alternating layers

- **CNN**: parallel, local, short-range
- **RNN**: sequential, long-range, slow
- **Transformer**: parallel, long-range, flexible, memory-heavy