import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, there seems to be a network error.")
            return ""

def main():
    speak("Hello, I am your voice assistant. How can I help you?")

    print("\n🧠 You can ask me things like:\n")
    print("🧩 Basic Questions:")
    print(" - Hello")
    print(" - What's your name")
    print(" - How are you")
    print(" - Tell me a joke")
    print(" - Love You")
    print(" - What is voice assistant")

    print("\n🧠 NLP and Deep Learning Questions:")
    print(" - What is NLP")
    print(" - What is tokenization")
    print(" - What is deep learning")
    print(" - What is a neural network")
    print(" - What is sentiment analysis")

    print("\n🎯 Voice Assistant Interview Questions:")
    print(" - What is a voice assistant")
    print(" - How does a voice assistant work")
    print(" - Give examples of voice assistants")
    print(" - What are intents and entities")
    print(" - What is speech recognition")
    print(" - Difference between speech recognition and NLP")
    print(" - Challenges in building a voice assistant")

    print("\n⛔ To stop the assistant, just say 'stop' or 'exit'.\n")
    
    speak("Now you can start asking your questions.")
    
    
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hi there! How can I help you today?")
        elif "your name" in command:
            speak("I'm your friendly voice assistant!")
        elif "how are you" in command:
            speak("I'm doing great, thanks for asking!")
        
        elif "tell me a joke" in command:
            speak("Why did the computer show up at work late? Because it had a hard drive!")
        
        elif "i love you" in command or "love you" in command:
            speak("Aww, I love you too! ❤️")


        elif "Do you know what is voice assistant" in command:
            speak("A voice assistant is a software agent that can perform tasks or services based on voice commands.")
         # NLP and Deep Learning Questions
        elif "what is nlp" in command:
            speak("Natural Language Processing is a branch of AI that helps computers understand, interpret, and respond to human language.")
        
        elif "what is tokenization" in command:
            speak("Tokenization is the process of breaking text into smaller parts like words or sentences.")
        
        elif "what is deep learning" in command:
            speak("Deep learning is a type of machine learning that uses neural networks with many layers to learn from large amounts of data.")
        
        elif "what is a neural network" in command:
            speak("A neural network is a system of algorithms that attempts to recognize relationships in data, similar to how a human brain works.")
        
        elif "what is sentiment analysis" in command:
            speak("Sentiment analysis is a technique in NLP to determine if the text expresses a positive, negative, or neutral emotion.")
        # Voice Assistant Role Interview Questions
        elif "what is a voice assistant" in command:
            speak("A voice assistant is a digital assistant that uses voice recognition, speech synthesis, and natural language processing to provide services to users.")

        elif "how does a voice assistant work" in command:
            speak("A voice assistant works by capturing the user’s voice, processing it using NLP, understanding the intent, and providing a spoken response.")

        elif "give examples of voice assistants" in command:
            speak("Some examples are Amazon Alexa, Apple Siri, Google Assistant, and Microsoft Cortana.")

        elif "what are intents and entities" in command:
            speak("Intents are the purpose behind a user’s input, and entities are specific pieces of information in the input.")

        elif "what is speech recognition" in command:
            speak("Speech recognition is the ability of a machine to identify and process spoken language into text.")

        elif "difference between speech recognition and NLP" in command:
            speak("Speech recognition converts voice to text, while NLP understands the meaning of that text.")

        elif "challenges in building a voice assistant" in command:
            speak("Challenges include handling accents, background noise, language variations, and understanding context.")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
