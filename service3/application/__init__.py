from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/get/genre', methods=['GET'])
def get_genre():
    genre = ['Business', 'Self-improvement', 'Strategy', 'Programming']
    randomnum = random.randint(0, 3)
    return Response(genre[randomnum], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')