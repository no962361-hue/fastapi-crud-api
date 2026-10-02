from http.server import BaseHTTPRequestHandler, HTTPServer
class MyServer(BaseHTTPRequestHandler):

  def do_POST(self):
    print("Received POST request")
    self.send_response(201)
    self.send_header("Content-type", "application/json")
    self.end_headers()

    self.wfile.write(b'{ "name" :"7mada", "age" :"25"}')
server = HTTPServer(("localhost", 8000), MyServer)
print("Server is running on http://localhost:8000")
server.serve_forever()