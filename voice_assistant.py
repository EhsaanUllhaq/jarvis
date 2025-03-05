import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import pyautogui

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Make the program speak."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice command."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def execute_command(command):
    """Execute tasks based on the command."""
    if "open notepad" in command:
        os.system("notepad.exe")
        speak("Opening Notepad.")
    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    elif "search for" in command:
        query = command.split("search for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}.")
    elif "play music" in command:
        speak("Playing music.")
        pyautogui.hotkey('playpause')  # Play/pause media
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()  # Exit the program
    else:
        speak("Sorry, I don't know how to do that.")

# Main program loop
speak("Hello! I am your personal assistant. How can I help you?")
while True:  # Keep the program running
    try:
        command = listen()
        if command:
            execute_command(command)
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong. Let's try again.")