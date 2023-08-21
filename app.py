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
    elif "i am user" in user_input or "user" in user_input:
        print("Hello, User. I am programmed to follow your commands. I am always at your service")
        response = "Hello, User. I am programmed to follow your commands. I am always at your service"
    elif "developer details" in user_input:
        print("This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik.")
        response = "This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik."
    elif "developer" in user_input:
        print("This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik.")
        response = "This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik."
    elif "details" in user_input:
        print("This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik.")
        response = "This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik."
    elif "team" in user_input:
        print("This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik.")
        response = "This AI system is Developed by team Clumsy Coders. There is total 4 members in team. First Harami Ashesh, Second Bokachoda Koulik, Third changra Anirban and Fourth is Innocent Soubhik."
    elif "thank you" in user_input:
        print("Thank you.")
        response = "Thank you."
    #elif "play" in user_input:
        #video_url = "https://youtu.be/dQw4w9WgXcQ"
        #webbrowser.open(video_url)
        #response = "Playing YouTube video"
    else:
        print("I don't understand.")
        response = "Command not recognized"

    return response

@app.route('/process_input', methods=['GET'])
def process_input():
    user_input = request.args.get('user_input', '').lower()

    if user_input.lower() == "exit":
        response = "Exiting"
    else:
        response = handle_user_input(user_input)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
