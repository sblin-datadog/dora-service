"""
Dora Service - Simple Python service for DORA metrics demo
"""

import os
from flask import Flask

app = Flask(__name__)

SERVICE_NAME = os.getenv("DD_SERVICE", "dora-service")
VERSION = os.getenv("DD_VERSION", "1.0.0")
ENV = os.getenv("DD_ENV", "dev")


@app.route("/dora", methods=["GET"])
def dora():
    """Main endpoint."""
    return "hi from dora-service"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    print(f"Starting {SERVICE_NAME} v{VERSION} ({ENV}) on port {port}")
    app.run(host="0.0.0.0", port=port)

