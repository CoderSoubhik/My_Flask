from flask import Flask, Response
import pyttsx3
import webbrowser

app = Flask(__name__)

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"AI: {text}.")
    print("")
    engine.say(text)
    engine.runAndWait()

def handle_user_input(user_input):
    if "hello" in user_input:
        speak("Hello, how can I assist you?")
    elif "play" in user_input:
        video_url = "https://youtu.be/dQw4w9WgXcQ"
        webbrowser.open(video_url)
        speak("Playing YouTube video")
    elif "exit" in user_input:
        speak("Exiting")
    else:
        speak("I don't understand that command.")

@app.route('/<user_input>', methods=['GET'])
def process_input(user_input):
    handle_user_input(user_input)
    return Response(status=204)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
