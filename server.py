#!/usr/bin/env python3
"""Local dev server with /save endpoint for in-browser editing."""
import json, os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            data = json.loads(body)
            filename = os.path.basename(data.get('file', 'index.html'))
            filepath = os.path.join(os.path.dirname(__file__), filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(data['html'])
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'saved')
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, fmt, *args):
        if '/save' in (args[0] if args else ''):
            print(f'  💾 saved')
        else:
            super().log_message(fmt, *args)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = 8080
    print(f'Executive Minds dev server → http://localhost:{port}/')
    HTTPServer(('', port), Handler).serve_forever()
