from flask import Flask, request, jsonify
import webbrowser

app = Flask(__name__)

def handle_user_input(user_input):
    if "hello" in user_input:
        print("Hello sir, how are you")
        response = "Hello sir, how are you"
    elif "intro" in user_input:
        print("Hello, I am Home AI, a personal home automation system, developed by team Clumsy Coders.")
        response = "Hello, I am Home AI, a personal home automation system, developed by team Clumsy Coders."
    elif "i am koulik" in user_input or "koulik" in user_input:
        print("Hello, Bokachoda Koulik")
        response = "Hello, Bokachoda Koulik"
    elif "i am ashesh" in user_input or "ashesh" in user_input:
        print("Hello, harami Ashesh")
        response = "Hello, Harami Ashesh"
    elif "i am anirban" in user_input or "anirban" in user_input:
        print("Hello, harami Ashesh")
        response = "Hello, Changra Anirban"
    elif "play" in user_input:
        video_url = "https://youtu.be/dQw4w9WgXcQ"
        webbrowser.open(video_url)
        response = "Playing YouTube video"
    else:
        print("I don't understand.")
        response = "Command not recognized"

    return response

@app.route('/process_input', methods=['GET'])
def process_input():
    user_input = request.args.get('user_input', '')

    if user_input.lower() == "exit":
        response = "Exiting"
    else:
        response = handle_user_input(user_input)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
