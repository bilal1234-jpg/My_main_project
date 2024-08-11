# import speech_recognition as sr
import threading
from violent import voi_list
# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to recognize speech from microphone
# def recognize_from_microphone():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#         try:
#             # Recognize speech using Google Web Speech API
#             text = recognizer.recognize_google(audio)
#             print("Recognized text:", text)
#         except sr.UnknownValueError:
#             print("Google Web Speech API could not understand the audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Web Speech API; {e}")

# while True:
#     t = threading.Thread(recognize_from_microphone())
#     t.start()


import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to recognize speech from microphone
def recognize_from_microphone():
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise for a shorter duration (e.g., 0.5 seconds)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Listen with a timeout and phrase_time_limit to limit how long it listens
        audio = recognizer.listen(source, timeout=1, phrase_time_limit=3)
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            
            if any(word in text for word in voi_list):
                print("Recognized text violence:", text)
            
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

while True:
    try:
        t = threading.Thread(recognize_from_microphone())
        t.start()
    except: 
        print("Timeout error")
        


    