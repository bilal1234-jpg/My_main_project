from violent import voi_list
import speech_recognition as sr



class voice_detect:
    def __init__(self):
        
        self.recognizer = sr.Recognizer()

    
    def recognize_from_microphone(self):
        with sr.Microphone() as source:
            print("Listening...")
           
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            
            
            try:
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=3)
                text = self.recognizer.recognize_google(audio)
                
                if any(word in text for word in voi_list):
                    return text
                
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass



# v = voice_detect()

# while True:
#     try:
#         t = threading.Thread(v.recognize_from_microphone())
#         t.start()
#     except: 
#         print("Timeout error")
        
        