My First Voice Assistant
This is a simple Voice Assistant project built using Python that can interact with the user through voice commands. It responds to a variety of questions about **Voice Assistants**, **Natural Language Processing (NLP)**, **Deep Learning**, and even answers **Voice Assistant role interview questions**!
Features
- **Voice Recognition**: The assistant listens to the user and converts speech into text.
- **Predefined Commands**: The assistant responds to commands like "Hello", "What's your name?", "Tell me a joke", and many more.
- **NLP and Deep Learning Q&A**: It can answer basic questions related to **NLP** and **Deep Learning**.
- **Voice Assistant Interview Q&A**: It answers interview questions related to voice assistants.
- **Customizable**: You can easily add more questions and responses to improve the assistant.
Requirements
- **Python 3.x**
- **PyAudio**: For speech recognition (see installation instructions below).
- **SpeechRecognition**: To capture and process voice commands.
- **gTTS (Google Text-to-Speech)**: For text-to-speech functionality.
- **pyaudio**: Used for speech input via microphone.
- **pyttsx3**: For text-to-speech output.
Installation
To get started, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/kapperasrisailam2001/my-first-voice-assistant.git
cd my-first-voice-assistant
```

2. Install the required libraries:

```bash
pip install SpeechRecognition pyttsx3 pyaudio gTTS
```

3. **(Windows users)** If you encounter issues with PyAudio installation, you may need to install Microsoft C++ Build Tools.
How to Use
1. Run the `voice_assistant.py` file:

```bash
python voice_assistant.py
```

2. The assistant will greet you and list available questions you can ask.
3. Say commands like:
    - "Hello"
    - "What's your name?"
    - "Tell me a joke"
    - "What is NLP?"
    - "What is deep learning?"
    - "I love you"

4. To stop the assistant, just say "Stop" or "Exit".
Example Commands
- **Basic Questions:**
    - "Hello"
    - "What's your name?"
    - "How are you?"
    - "Tell me a joke"
    - "What is voice assistant?"

- **NLP & Deep Learning Questions:**
    - "What is NLP?"
    - "What is tokenization?"
    - "What is deep learning?"
    - "What is a neural network?"
    - "What is sentiment analysis?"

- **Voice Assistant Interview Questions:**
    - "What is a voice assistant?"
    - "How does a voice assistant work?"
    - "Give examples of voice assistants"
    - "What are intents and entities?"
    - "What is speech recognition?"
    - "Difference between speech recognition and NLP"
    - "Challenges in building a voice assistant"
Future Enhancements
- Add more questions and responses.
- Improve the assistant's ability to understand various accents and speech patterns.
- Integrate with more services (e.g., weather updates, reminders, etc.).
- Add a graphical interface for easier interaction.
License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Author
- [kapperasrisailam](https://github.com/kapperasrisailam2001)
