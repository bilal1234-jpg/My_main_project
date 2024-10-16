import threading
from violent import voi_list

import speech_recognition as sr



class voice_detect:
    def __init__(self):
        
        self.recognizer = sr.Recognizer()

    # Function to recognize speech from microphone
    def recognize_from_microphone(self):
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise for a shorter duration (e.g., 0.5 seconds)
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            # Listen with a timeout and phrase_time_limit to limit how long it listens
            audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=3)
            try:
                # Recognize speech using Google Web Speech API
                text = self.recognizer.recognize_google(audio)
                
                if any(word in text for word in voi_list):
                    print("Recognized text violence:", text)
                
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Web Speech API; {e}")



# v = voice_detect()

# while True:
#     try:
#         t = threading.Thread(v.recognize_from_microphone())
#         t.start()
#     except: 
#         print("Timeout error")
        
        