"""
GoldenPath IDP - Hello World Test Application
Lightweight service for end-to-end build and deployment testing.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

VERSION = os.getenv("APP_VERSION", "1.0.0")
ENV = os.getenv("ENV", "local")


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>GoldenPath IDP</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            transition: background-color 0.3s, color 0.3s;
        }}
        .light {{ background-color: #ffffff; color: #1a1a1a; }}
        .dark {{ background-color: #1a1a1a; color: #ffffff; }}
        h1 {{ font-size: 2.5rem; margin-bottom: 1rem; }}
        .info {{ opacity: 0.7; margin-bottom: 2rem; }}
        .buttons {{ display: flex; gap: 1rem; }}
        button {{
            padding: 1rem 2rem;
            font-size: 1.1rem;
            border: 2px solid currentColor;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.2s;
        }}
        button:hover {{ transform: scale(1.05); }}
        .btn-white {{ background: #ffffff; color: #1a1a1a; }}
        .btn-black {{ background: #1a1a1a; color: #ffffff; }}
    </style>
</head>
<body class="light">
    <h1>Hello from GoldenPath IDP!</h1>
    <p class="info">Version: {version} | Environment: {env}</p>
    <div class="buttons">
        <button class="btn-white" onclick="document.body.className='light'">White</button>
        <button class="btn-black" onclick="document.body.className='dark'">Black</button>
    </div>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._respond_json(200, {"status": "healthy", "version": VERSION})
        elif self.path == "/ready":
            self._respond_json(200, {"ready": True})
        elif self.path == "/api":
            self._respond_json(200, {
                "message": "Hello from GoldenPath IDP!",
                "version": VERSION,
                "environment": ENV
            })
        else:
            self._respond_html()

    def _respond_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())

    def _respond_html(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html = HTML_PAGE.format(version=VERSION, env=ENV)
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"GoldenPath IDP - Hello World")
    print(f"Version: {VERSION}")
    print(f"Server running on :{port}")
    server.serve_forever()
