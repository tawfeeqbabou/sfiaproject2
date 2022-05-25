from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/get/book', methods = ['GET'])
def get_book():
    book = ['Rich Dad, Poor Dad', 'The Chimp Complex', 'The Art Of War', 'Thirty Second Code']
    randomnum = random.randint(0, 3)
    return Response(book[randomnum], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port = 5001, debug = True, host = '0.0.0.0')