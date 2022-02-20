import game_of_life
from flask import Flask, render_template, request

LifeGame = Flask(__name__)


@LifeGame.route('/', methods=['get', 'post'])
def main_page():
    game_width = 30
    game_height = 17
    if request.method == 'POST':
        game_width = int(request.form.get('width'))
        game_height = int(request.form.get('height'))
    game_of_life.GameOfLife(game_width, game_height)
    return render_template('index.html')


@LifeGame.route('/live')
def live():
    z = game_of_life.GameOfLife()
    if z.counter > 0:
        z.form_new_generation()
    z.counter += 1
    return render_template('live.html', live=z)


if __name__ == '__main__':
    LifeGame.run(debug=True)
