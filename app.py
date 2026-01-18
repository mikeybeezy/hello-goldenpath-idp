"""
GoldenPath IDP - Hello World Test Application
Lightweight service for end-to-end build and deployment testing.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

VERSION = os.getenv("APP_VERSION", "1.0.0")
ENV = os.getenv("ENV", "local")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._respond(200, {"status": "healthy", "version": VERSION})
        elif self.path == "/ready":
            self._respond(200, {"ready": True})
        else:
            self._respond(200, {
                "message": "Hello from GoldenPath IDP!",
                "version": VERSION,
                "environment": ENV
            })

    def _respond(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"GoldenPath IDP - Hello World we made it here again and agan rr 5555")
    print(f"Version: {VERSION}")
    print(f"Server running on :{port}")
    server.serve_forever()
