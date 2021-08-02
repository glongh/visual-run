import os
import json
from os import walk
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from utils import TraceFile
from utils.lru_cache import CacheLRU

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
        id = ''
        if (len(query)):
            query_components = dict(qc.split("=") for qc in query.split("&"))
            id = query_components.get('id', '')

        # Trace all algorithms
        if '/trace_all' in self.path:
            self._set_headers()
            # 1: Get the file names
            files_to_trace = filenames = next(
                walk("algorithms/"), (None, None, []))[2]
            # 2: Trace the files concurrently
            trace_with_threads = TraceFile(files_to_trace)

            result = trace_with_threads.trace_all()
            data = json.dumps({"results": result})
            self.wfile.write(data.encode())

        # Trace one algorithm
        elif '/trace' in self.path:
            if len(id) > 0:
                os.system('python {}.py'.format(id))
                print(id)
                self.send_response(200)
            self.send_response(404)

        # Return the traces of one algorithm
        elif '/algorithm' in self.path:
            if len(id) > 0:
                self._set_headers()
                data = lru_cache.get(id)
                if not data:
                    with open('output/{}.json'.format(id)) as data_file:
                        data = data_file.read()
                    print('read from file')
                    lru_cache.set(id, data)
                self.wfile.write(data.encode())

        # Return the source code of one algorithms
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
    cache_size = 2
    lru_cache = CacheLRU(cache_size)
    webServer = HTTPServer((HOST, PORT), ServerHandler)
    print("Server started http://%s:%s" % (HOST, PORT))

    webServer.serve_forever()
