from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/book/genre', methods = ['GET'])
def get_book():
    book = requests.get('http://service2:5001/get/book').text
    genre = requests.get('http://service3:5002/get/genre').text
    generate = book + '-' + genre
    quote = requests.post ('http://service4:5003/post/quote', data = generate).text
    return render_template('home.html', title='quote generator', book = book, genre=genre, quote=quote)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')