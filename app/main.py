import time
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", service="agrosugar-ndvi")

@app.get("/ndvi")
def ndvi():
    n = int(request.args.get("size", 1500))
    t0 = time.time()
    nir = np.random.rand(n, n).astype(np.float32)
    red = np.random.rand(n, n).astype(np.float32)
    idx = (nir - red) / (nir + red + 1e-9)
    return jsonify(size=n, ndvi_mean=float(idx.mean()),
                   ms=round((time.time() - t0) * 1000, 1))
