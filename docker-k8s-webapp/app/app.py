import os
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

APP_NAME = os.environ.get("APP_NAME", "docker-k8s-webapp")
APP_ENV = os.environ.get("APP_ENV", "dev")
APP_VERSION = os.environ.get("APP_VERSION", "v1.0.0")
START_TIME = time.time()

@app.get("/")
def index():
    return {
        "app": APP_NAME,
        "env": APP_ENV,
        "version": APP_VERSION,
        "message": "Hello, Engineer Pappy! Your Flask app is running."
    }

@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok", "uptime_s": round(time.time() - START_TIME, 2)})

@app.get("/readyz")
def readyz():
    return jsonify({"ready": True})

@app.get("/compute")
def compute():
    n = int(request.args.get("n", 10000))
    total = 0
    for i in range(n):
        total += (i * i) % 97
    return jsonify({"n": n, "total": total})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
