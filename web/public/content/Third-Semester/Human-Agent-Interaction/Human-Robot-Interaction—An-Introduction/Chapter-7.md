### **Chapter 7: Verbal Interaction**

### **7.1 Human-Human Verbal Interaction**

- **Speech Functions**:
  - Conveying information
  - Creating shared reality and joint attention: It allows people to synchronize their thoughts or actions, making communication more meaningful and collaborative.
  - Complex and context-dependent (intonation(The way you say something), emphasis, and prosody((the rhythm and tone of how something is said)) affect meaning)
  
  
- **Components of Speech**:
  - **Utterance**: smallest unit of spoken language like full sentence, a phrase, or even just a word, informal and may contain conversational fillers or incomplete grammar.
  - **Words**: Smallest units conveying meaning.
  - **Phonemes**: Smallest sound units that make up words. Example: "pat" = [p] [a] [t].
  - **Conversational Fillers**: Uh-huh, uhm, used to maintain conversation flow.
  - **Paralinguistic Information**: Non-verbal signals (intonation, gestures, gaze) that add meaning to verbal communication.
#### **7.2 Speech Recognition**

- **Automatic Speech Recognition (ASR)**: Converts spoken language into written text (speech-to-text).
  - **Challenges in HRI**: Noise, diverse accents, distance from the microphone, and noisy environments.
  - **Speech Recognition Process**:
    - Speech recorded in the **time domain** and converted to the **frequency domain** for analysis.
      - While the time domain shows how loud the speech is at any given time, the frequency domain breaks down the speech into its individual frequencies, which is much more useful for understanding the specific sounds (phonemes) being produced.
    - Deep learning and **sequence-to-sequence models** (since 2010) have greatly improved ASR performance, replacing older models like Gaussian Mixture and Hidden Markov Models.
    - Cloud-based ASR is more accurate but requires an internet connection.
  
- **McGurk Effect**: Shows how visual cues (like lip movements) influence what we hear. For example, if you hear "ba" but see someone saying "fa," your brain might interpret the sound as "fa.", demonstrating **multimodal perception** in speech.

- **Limitations of ASR**:
  - Struggles with dialects, non-native speakers, noisy environments.
  - Proper nouns and specific names are often misrecognized.
  
- **Voice Activity Detection (VAD)**: Recognizes when someone is speaking but doesn’t transcribe. Useful for detecting when a robot should start listening.

- **Artificial Languages**:
  - **Engineered Languages**: Designed for **logic, philosophy, or linguistics** experiments (e.g., **Loglan**, **ROILA**).
    - **ROILA**: Developed for **HRI** to improve **speech-recognition accuracy**. Words are designed to sound distinct for better recognition by robots. Like "Go forward" = **kanek koloke**, "Go back" = **kanek nole**.
  - **Auxiliary Languages**: Created to **bridge natural languages** or serve as an **international medium** (e.g., **Esperanto**).
  - **Artistic Languages**: Made for **fictional worlds** (e.g., **Klingon**, **Elfish**, **Dothraki**).

---

### **7.3 Interacting Using Language**

- **Speech Recognition ≠ Understanding**:
  - ASR transcribes words but does not "understand" meaning.

- **Extracting Meaning**:
  - **Sentiment Analysis**: Determines the emotional tone of spoken text (positive or negative).
  - **Intent Recognition**: Identifying the user’s goals or commands from speech (e.g., setting reminders).

- **Chatbots in HRI**:
  - Two types:
    1. **Goal-specific chatbots**: Limited to specific domains (e.g., customer service).
    2. **General-purpose chatbots**: Can respond to a wide range of topics using LLMs.
  - Issues with chatbots: Sometimes they learn inappropriate responses (e.g., Microsoft’s Tay).
  - **Multimodal Input**: Robots, unlike chatbots, use multiple sensors (vision, sound) to process more than just text.

#### **7.4 Dialogue Management in HRI**

- **Dialogue Management (DM)**:
  - Manages back-and-forth conversations between users and robots.
  - Can be:
    - **System-initiative**: The robot leads the conversation.
    - **User-initiative**: The user leads.
    - **Mixed-initiative**: Both take turns leading.
  
- **Finite State Machines (FSM)**:
  - Basic DM structures that follow linear dialogue flows.
  
- **Event-based DMs**:
  - More advanced, allowing for dynamic conversation changes based on user input (e.g., interruptions).

#### **7.5 Speech Production**

- Older Text-to-Speech (TTS) systems (e.g., Stephen Hawking’s speech synthesizer) were basic and unnatural. Modern systems (like **WaveNet**) are much more human-like.
  
- **Parametric TTS**: Uses a model of speech generation, flexible but less natural.
  
- **Neural Vocoders**: Deep learning-based systems trained on large speech datasets. They produce highly natural speech.
  
- **TTS Challenges**:
  - **Emotion in speech**: Current models don't modulate emotion well.
  - TTS sounds more like text being read than a natural conversation.

