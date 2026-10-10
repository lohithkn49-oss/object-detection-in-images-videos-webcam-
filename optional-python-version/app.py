"""Run:  python app.py   (no installs needed, uses only Python's built-in modules)"""
import http.server
import os
import socketserver
import threading
import webbrowser

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # serve the folder this file is in


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):   # keep the console quiet
        pass


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as server:
    url = f"http://127.0.0.1:{PORT}"
    print(f"Detector running at {url}")
    print("Press Ctrl+C to stop.")
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")
