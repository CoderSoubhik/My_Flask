from flask import Flask, request, jsonify
import webbrowser

app = Flask(__name__)

def handle_user_input(user_input):
    if "hello" in user_input:
        print("Hello sir, how are you")
        response = "Hello sir, how are you"
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
