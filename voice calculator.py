import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("Voice Calculator")
print("Speak your calculation (example: five plus three)")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("User Input:", text)

    expression = text.replace("plus","+").replace("minus","-") \
                     .replace("into","*").replace("multiply","*") \
                     .replace("divide","/")

    result = eval(expression)

    print("Output:", result)

    engine.say("The result is " + str(result))
    engine.runAndWait()

except:
    print("Could not recognize speech")