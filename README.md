
# 🌦️ Weather API

A simple Flask-based Weather API that fetches weather data from [Visual Crossing](https://www.visualcrossing.com/weather-api) and caches results using Redis Cloud.

## 🚀 Features

- Real-time weather by city
- Redis caching (12-hour expiration)
- Environment variable support
- Rate limiting
- Clean and lightweight Flask API

## 🔧 Tech Stack

- Python + Flask
- Redis (Cloud)
- Visual Crossing API
- dotenv for config
- `flask-limiter` for rate limiting

## 📦 Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/king-luvaha/weather-api.git
cd weather-api
````

2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask requests python-dotenv redis flask-limiter
```

4. Create a `.env` file:

```env
API_KEY=your_visualcrossing_api_key
REDIS_URL=your_redis_cloud_url
```

5. Run the app:

```bash
python app.py
```

6. Test:

```http
GET http://127.0.0.1:5000/weather?city=Nairobi
```

---

Roadmap Project URL: https://roadmap.sh/projects/weather-api-wrapper-service