from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/submit_weather", methods=['POST'])
def submit_weather():
    data = request.form
    
    # Extract the form data
    temperatures = {
        't1': data.get('T1'),
        't2': data.get('T2'),
        't3': data.get('T3')
    }
    
    rain_probability = {
        'day1': data.get('R1'),
        'day2': data.get('R2'),
        'day3': data.get('R3')
    }
    
    cloud_type = data.get('cloudType')
    
    # Here you can process the data as needed
    # For now, we'll just return it
    return jsonify({
        'temperatures': temperatures,
        'rain_probability': rain_probability,
        'cloud_type': cloud_type,
        'message': 'Data received successfully'
    })

if __name__ == "__main__":
    app.run(debug=True)