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
    
    # Extract and convert temperatures to integers
    t1 = int(data.get('T1'))
    t2 = int(data.get('T2'))
    t3 = int(data.get('T3'))
    
    # Calculate average temperature
    avg_temp = (t1 + t2 + t3) / 3
    
    # Check if temperature is possible
    if avg_temp > 134.1:
        return jsonify({
            'error': 'Temperature is not possible in this current day',
            'average': int(avg_temp)
        })
    
    # Count rainy vs non-rainy days
    rain_count = 0
    no_rain_count = 0
    
    # Process rain data
    for day in ['R1', 'R2', 'R3']:
        if data.get(day).lower() == 'y':
            rain_count += 1
        elif data.get(day).lower() == 'n':
            no_rain_count += 1
    
    # Process cloud type
    cloud_type = int(data.get('cloudType'))
    if cloud_type == 1:
        no_rain_count += 1
    elif cloud_type == 2:
        rain_count += 1
    elif cloud_type == 3:
        no_rain_count += 2
    
    # Determine prediction
    prediction = "rain day" if rain_count > no_rain_count else "no rain day"
    
    return jsonify({
        'temperatures': {
            't1': t1,
            't2': t2,
            't3': t3
        },
        'average_temperature': int(avg_temp),
        'rain_probability': {
            'day1': data.get('R1'),
            'day2': data.get('R2'),
            'day3': data.get('R3')
        },
        'cloud_type': cloud_type,
        'prediction': prediction,
        'message': 'Data processed successfully'
    })

if __name__ == "__main__":
    app.run(debug=True)