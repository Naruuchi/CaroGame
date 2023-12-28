from flask import Flask, render_template, url_for, redirect
from minimax import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

gametable = []

@app.route('/resize/<int:n>')
def resize(n):
    global gametable
    gametable = [[0 for i in range (0, n)] for i in range (0, n)]
    return redirect('/size/' + str(n))


@app.route('/size/<int:size>')
def game(size):
    x = url_for('static', filename='imgs/x.png')
    o = url_for('static', filename='imgs/o.png')
    return render_template('game.html', size=size, matrix = gametable, x = x, o = o)

@app.route('/size/draw/<string:id>')
def draw(id):
    index = id.split('.')
    global gametable

    print(index)
    if len(index) == 2:
        gametable[0][int(id)] = -1
    elif len(index) > 2:
        
        gametable[int(index[1])][int(index[2])] = -1
        gametable = nextBestMove(gametable, int(index[0]))
    
    return redirect('/size/' + index[0])

if (__name__ == '__main__'):
    app.run(debug=True)