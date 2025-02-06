from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Example temperature data - you can replace this with real data later
    temperatures = {
        'temp1': '25°C',
        'temp2': '22°C',
        'temp3': '28°C',
        'temp4': '20°C',
        'temp5': '24°C'
    }
    return render_template('index.html', temperatures=temperatures)

if __name__ == '__main__':
    app.run(debug=True)
