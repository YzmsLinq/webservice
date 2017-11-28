import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("",PORT),handler)
#httpd = socketserver.TCPServer(("127.0.0.1",PORT),handler)

print("HTTP server is at : http://127.0.0.1:%d/" % PORT)
httpd.serve_forever()
