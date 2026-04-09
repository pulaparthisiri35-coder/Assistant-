import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Function to listen for microphone input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Main logic
if __name__ == "__main__":
    speak("Hello, how can I help you today?")
    
    while True:
        query = take_command()

        if 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"Current Time: {strTime}")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
          output:
      Listening...
Recognizing...
User said: Open Google

Listening...
Recognizing...
User said: Tell me the time
Current Time: 14:30:05

Listening...
Recognizing...
User said: Exit
