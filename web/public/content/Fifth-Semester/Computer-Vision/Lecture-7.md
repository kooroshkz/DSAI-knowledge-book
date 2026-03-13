#### Stochastic (Random) Generation

In Image classification we have inputs and one output (label) (Non-stochastic) but in Image generation we have only one input but many possible outputs.

A solution like stochastic generation is needed to generate different outputs for the same input.

**Conditional** models are used to generate images based on some conditions like class labels or text descriptions, **unconditional** models generate images without any specific conditions so we add conditions for creativity.

- **Generative models**
    - **Direct approach**: $G: z \rightarrow x$ where $z$ is random noise (GANs, Diffusion models)
    - **Indirect approach**: $E: x \rightarrow \R$ where we score generated images and find higher score image
- **Autoregressive models**: Generate an image pixel by pixel where predict next pixel **distribution** based on previous pixels and sample 
        - **Without DL**: Copy patch in image and paste it in another place, make texture, doesn't work on complex images
        - **With DL**: Train a next-pixel classifier
- **Generative Adversarial Networks (GANs)**: Two networks (Generator and Discriminator) compete where the generator tries to create realistic images and the discriminator tries to distinguish between real and fake images.
    - **Generator (G)**: Takes random noise as input and generates images train to fool the discriminator.
    - **Discriminator (D)**: Takes an image as input and outputs a probability indicating whether the image is real or fake, trained to classify correctly.
    - **Issues**: unstable training, mode collapse (lack of diversity), hard to control generation -> (Conditional GANs).
    - **Conditional GANs**: Both G and D receive additional information
        - **pix2pix**: Image-to-image translation using paired data which is **Limitation** (e.g., sketches to photos)
            - Loss: L1 loss (structure), GAN loss (realism)
            - Generator: U-Net (encoder–decoder + skip connections)
            - Discriminator: PatchGAN (looks at patches, not whole image)
    - **Unpaired image translation (CycleGAN)**: Learn to translate between two domains without paired examples using cycle consistency loss.
        - Two generators (G: A→B, F: B→A) and two discriminators (D_A, D_B)
        - Loss: Adversarial loss + Cycle consistency loss (F(G(A)) ≈ A, G(F(B)) ≈ B)
        - Issues: Not controlled generation, hallucinations, not perfect

**Why image translation matters**
- colorization
- inpainting
- restoration
- medical imaging
- data augmentation

- **Diffusion models (modern SOTA)**: Generate images by denoising noise step by step.
    - **Based on**: Unet architecture + skip connections, timestep embeddings (tell network how noisy the image is)
    - **Forward diffusion**: start with real image and add noise gradually over T steps until it becomes pure noise.
    - **Reverse diffusion**: start with pure noise and learn to denoise step by step
    - **Cons**: slow and expensive
    - **Pros** (vs GANs): more stable training, better diversity, high-quality images, easier conditioning
    - **Making efficient**:
        - **low resolution** then **upsample**
        - **latent diffusion**: encode image into latent space (embeddings), run diffusion in latent space then decode back to image
    - **Control methods**:
        - **Explicit conditioning**: Give text, image, input to train with condition
        - **Classifier guidance**: use a classifier’s gradients and push generation toward desired class
            - Need classifier trained on noisy images
            - Bad gradients
        - **Classifier-free guidance** (Most common): Train diffusion model with and without conditions then guide generation using difference
            - Like: Stable Diffusion, DALL·E, GLIDE
    - **Image editing with diffusion**
        - **SDEdit**: add noise to an existing image, denoise with prompt and keeps structure, changes content
        - **Prompt-to-Prompt**: modify attention maps, change parts of the image and keep rest fixed

---

| Model          | Strength         | Weakness    |
| -------------- | ---------------- | ----------- |
| Autoregressive | exact likelihood | slow        |
| GAN            | sharp images     | unstable    |
| Diffusion      | best quality     | slow, heavy |
