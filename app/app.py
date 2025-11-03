from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)


# Connect to the redis using environment variables
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return jsonify(message="Welcome to the project - Flask + Redis!")


@app.route('/count')
def count():
    # Increment a counter in Redis
    count = r.incr("hits")
    return jsonify(hits=count)

@app.route('/reset')
def reset():
    r.set("hits", 0)
    return jsonify(message="Counter reset to 0!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
