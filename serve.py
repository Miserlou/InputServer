import BaseHTTPServer
import threading
import time

HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9999 # Maybe set this to 9000.

input_buffer = ''
continue_input = True

def get_input():
    global input_buffer
    global continue_input
    while continue_input:
        input_value = raw_input('$ ')
        input_buffer = input_buffer + input_value + "\n"

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()

        global input_buffer
        s.wfile.write(input_buffer)
        input_buffer = ''

    def log_message(self, a, b, c, d):
        return

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), RequestHandler)

    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)

    thread = threading.Thread(target=get_input)
    thread.start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        continue_input = False
        pass
    httpd.server_close()

    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
