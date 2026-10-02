# one day
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Received GET request")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h1>hello my freind good job </h1>")

server = HTTPServer(("localhost", 8000), MyServer)

print("Server is running on http://localhost:8000")

server.serve_forever()
