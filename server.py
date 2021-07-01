import os, json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


PORT = 8080
HOST = '127.0.0.1'


class ServerHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):

        # Get the algorithm ID
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        id = query_components.get('id', '')

        if '/trace' in self.path:
            if len(id) > 0:
                os.system('python {}.py'.format(id))
                print(id)
                self.send_response(200)
            self.send_response(404)

        elif '/algorithm' in self.path:
            if len(id) > 0:
                self._set_headers()
                with open('output/{}.json'.format(id)) as data_file:
                    data = data_file.read()
                self.wfile.write(data.encode())
        elif '/file' in self.path:
            if len(id) > 0:
                self._set_headers()
                with open('{}.py'.format(id)) as data_file:
                    data = data_file.read()
                data = json.dumps({"file": data})
                self.wfile.write(data.encode())
        else:
            self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((HOST, PORT), ServerHandler)
    print("Server started http://%s:%s" % (HOST, PORT))

    webServer.serve_forever()
