from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def generate_pizdato_meme():
    nachalo = ["Братан,", "Короче,", "Типа,", "Кста,", "Это пиздато,"]
    seredina = ["все будет", "жизнь есть", "деньги придут", "девки текут", "мемы крутят"]
    konec = ["четко", "в натуре", "без леща", "по-пацански", "в топку"]
    
    meme = random.choice(nachalo) + " " + random.choice(seredina) + " " + random.choice(konec)
    return meme

@app.route('/')
def index():
    return render_template('index.html', meme=generate_pizdato_meme())

@app.route('/api/meme')
def api_meme():
    return jsonify({'meme': generate_pizdato_meme()})

if __name__ == '__main__':
    app.run(debug=True)