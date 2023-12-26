from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/size/<int:size>')
def game(size):
    global gametable
    gametable = [[0] for i in range (0, size)]
    x = url_for('static', filename='imgs/x.png')
    o = url_for('static', filename='imgs/o.png')
    print(gametable)
    return render_template('game.html', size=size, matrix = gametable, x = x, o = o)

@app.route('/size/draw/<int:id>')
def draw(id):
    
    
    return redirect('/size/' + str(id))

if (__name__ == '__main__'):
    app.run(debug=True)