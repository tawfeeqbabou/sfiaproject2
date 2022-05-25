from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/quote', methods=['POST'])
def post_quote():
    generate = request.data.decode('utf-8')
    final_task = generate.split('-')
    if final_task[0] == 'Rich Dad, Poor Dad' and final_task[1] == 'Business':
        quote  = 'Read Rich Dad Poor Dad it will teach you about business'
    elif final_task[0] == 'Rich Dad, Poor Dad' and final_task[1] == 'Self-improvement':
        quote = 'Read Rich Dad Poor Dad it will teach you about self-improvement'
    elif final_task[0] == 'Rich Dad, Poor Dad' and final_task[1] == 'Strategy':
        quote = 'Read Rich Dad Poor Dad it will teach you about strategy'
    elif final_task[0] == 'Rich Dad, Poor Dad' and final_task[1] == 'Programming':
        quote = 'Read Rich Dad Poor Dad it will teach you about programming'
    elif final_task[0] == 'The Chimp Complex' and final_task[1] == 'Self-improvement':
        quote = 'Read The Chimp Complex it will teach you about self-improvement'
    elif final_task[0] == 'The Chimp Complex' and final_task[1] == 'Business':
        quote = 'Read The Chimp Complex it will teach you about business'
    elif final_task[0] == 'The Chimp Complex' and final_task[1] == 'Strategy':
        quote = 'Read The Chimp Complex it will teach you about strategy'
    elif final_task[0] == 'The Chimp Complex' and final_task[1] == 'Programming':
        quote = 'Read The Chimp Complex it will teach you about programming'
    elif final_task[0] == 'The Art Of War' and final_task[1] == 'Strategy':
        quote = 'Read The Art Of War it will teach you about strategy'
    elif final_task[0] == 'The Art Of War' and final_task[1] == 'Business':
        quote = 'Read The Art Of War it will teach you about business'
    elif final_task[0] == 'The Art Of War' and final_task[1] == 'Self-improvement':
        quote = 'Read The Art Of War it will teach you about self-improvement'
    elif final_task[0] == 'The Art Of War' and final_task[1] == 'Programming':
        quote = 'Read The Art Of War it will teach you about programming'
    elif final_task[0] == 'Thirty Second Code' and final_task[1] == 'Programming':
        quote = 'Read Thirty Second Code it will teach you about programming'
    elif final_task[0] == 'Thirty Second Code' and final_task[1] == 'Business':
        quote = 'Read Thirty Second Code it will teach you about business'
    elif final_task[0] == 'Thirty Second Code' and final_task[1] == 'Self-improvement':
        quote = 'Read Thirty Second Code it will teach you about self-improvement'
    elif final_task[0] == 'Thirty Second Code' and final_task[1] == 'Strategy':
        quote = 'Read Thirty Second Code it will teach you about strategy'
    else:
        quote = "You've reached the end of the quote generator"

    return Response(quote, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')