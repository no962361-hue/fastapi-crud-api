from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Received GET request")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if self.path == "/users/5":
            self.wfile.write(b'{"users": [{"name": "mohammed fawzy", "age": 25}, {"name": "ahmed ali", "age": 30}]}')
        elif self.path == "/products":
            self.wfile.write(b'{"products": [{"name": "laptop", "price": 1000}, {"name": "phone", "price": 500}]}')

server = HTTPServer(("localhost", 8000), MyServer)

print("Server is running on http://localhost:8000/users")
print("Server is running on http://localhost:8000/products")

server.serve_forever()
