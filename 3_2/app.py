"""A small Docker command reference with an HTTP health endpoint."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

COMMANDS = {
    "List running containers": "docker ps",
    "View container logs": "docker logs CONTAINER",
    "Open a shell": "docker exec -it CONTAINER sh",
    "Build an image": "docker build -t IMAGE .",
    "Publish a local port": "docker run -p 127.0.0.1:8080:8080 IMAGE",
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"}).encode()
            content_type = "application/json"
        elif self.path == "/":
            rows = "".join(f"<tr><td>{label}</td><td><code>{command}</code></td></tr>"
                           for label, command in COMMANDS.items())
            body = ("<!doctype html><html lang='en'><meta charset='utf-8'>"
                    "<title>Docker Quick Reference</title><h1>Docker Quick Reference</h1>"
                    f"<table><tr><th>Task</th><th>Command</th></tr>{rows}</table></html>").encode()
            content_type = "text/html; charset=utf-8"
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
