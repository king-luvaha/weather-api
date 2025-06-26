from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from weather_api import get_weather
from cache import cache_get, cache_set
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)

@app.route('/')
def home():
    return {"message": "Welcome to the Weather API!"}

@app.route('/weather')
@limiter.limit("10/minute")  # Rate limit
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    cached = cache_get(city)
    if cached:
        return jsonify({"source": "cache", "data": cached})

    try:
        data = get_weather(city)
        cache_set(city, data, ex=43200)  # 12 hours = 43200 seconds
        return jsonify({"source": "api", "data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
