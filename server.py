from http import server

class HTTPServer(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        self.send_header("Cross-Origin-Embedder-Policy-Report-Only", "unsafe-none")
        self.send_header("Cross-Origin-Opener-Policy-Report-Only", "unsafe-none")

if __name__ == '__main__':
    server_address = ('', 8080)  # Listen on all available network interfaces
    httpd = server.HTTPServer(server_address, HTTPServer)
    print("Server running on port 8080")
    httpd.serve_forever()
