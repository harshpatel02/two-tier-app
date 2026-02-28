from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (default localhost:6379)
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

@app.route("/")
def home():
    # Increment page visit counter
    r.incr("visits")
    
    # Get current visit count
    visits = r.get("visits").decode("utf-8")
    
    print("working!")
    return f"Hello! This page has been visited {visits} times."

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)