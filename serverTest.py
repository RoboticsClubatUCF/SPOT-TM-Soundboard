from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import mimetypes

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the requested file path
        if self.path == '/':
            self.path = '/index.html'

        try:
            file_extension = os.path.splitext(self.path)[1]
            if file_extension == '.mp3':
                # Set the appropriate Content-Type header for audio files
                self.send_response(200)
                self.send_header('Content-type', mimetypes.types_map[file_extension])
                self.end_headers()

                # Open and send the audio file
                with open(self.path[1:], 'rb') as file:
                    self.wfile.write(file.read())
            else:
                # For other file types, send the file content as text
                with open(self.path[1:], 'r') as file:
                    file_to_open = file.read()
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(file_to_open, 'utf-8'))
        except Exception as e:
            file_to_open = "File not found"
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
            print(f"Error: {e}")

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")