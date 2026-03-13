**Chapter 15: Chatbots & Dialogue Systems**

### 1. **Introduction to Dialogue Systems**:
   - **Task-oriented dialogue systems**: Used for specific tasks like booking flights or controlling appliances. They rely on structured **frames** with slots (e.g., time, date) to gather information from users.
   - **Chatbots**: Designed for more general, open-ended conversations, mimicking human-human interaction (e.g., ChatGPT). Modern chatbots often blend both unstructured conversations and task-oriented goals.

### 2. **ELIZA (Weizenbaum, 1966)**

   Chatbots using **pattern-matching rule** which raised human emotions.

### 3. **Properties of Human Conversation**:
   - **Turn-taking**: Conversation flows with participants taking turns. Systems must detect when a user has finished speaking and respond without awkward delays.
   - **Speech Acts**: e.g., asking, answering, promising
   - **Grounding**: Ensuring mutual understanding in conversation, often through feedback like "OK" or repeating important information.

### 4. **Dialogue Structure**:
   - **Adjacency pairs**: Certain types of utterances expect a specific response (e.g., a question expects an answer).
   - **Subdialogues**: Conversations can deviate from the main topic for clarification or corrections (e.g., interruptions to ask for clarification).

### 5. **Frame-Based Dialogue Systems**:
   - These systems use **frames** to structure conversations around tasks. Each frame has **slots** (e.g., origin city, departure date) that need to be filled to complete a task.
   - Dialogue systems use **domain classification** and **intent determination** to figure out what the user wants and how to fill the slots.

### 6. **Dialogue Acts and Dialogue State**:
   - Dialogue acts represent the function of an utterance (e.g., inform, request, confirm).
   - **Dialogue-state tracking**: Keeps track of the current state of the conversation (e.g., what information has been provided, what slots need filling).

### 7. **Chatbots**:
   - Chatbots are conversational agents designed to engage in extended, unstructured dialogue.
   - **Neural chatbots** (e.g., ChatGPT) are trained on large datasets, including conversations, to predict and generate the next response in a conversation.

### 8. **Training and Fine-Tuning**:
   - Chatbots are trained on **large datasets**, including dialogue-specific data.
   - **Fine-tuning** improves performance by using specific datasets for dialogue quality and safety, such as crowdsourced conversational data or safety-focused dialogues.

### 9. **Ethical Issues**:
   - **Privacy**: Chatbots often overhear sensitive information, which can raise privacy concerns.
   - **Bias and Abuse**: Chatbots can learn harmful behaviors from biased data (e.g., Microsoft's Tay chatbot). Systems need methods to prevent and respond to toxic or biased language.
   - **Safety**: In critical contexts (e.g., medical advice), chatbot errors can cause harm, necessitating careful safety measures.

### 10. **Evaluation**:
   - Chatbots are typically evaluated by humans on various factors like **engagingness**, **fluency**, and **safety**. Tools like **Likert scales** or specific metrics help assess conversational quality.