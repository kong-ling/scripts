import http.server
import socketserver
from tkinter import *

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class WebServer:
    def __init__(self):
        print('start server...')
        root = Tk()
        root.title('Simple web server')
        Label(root, text='Port:').grid(row=0, column=0)
        port_entry = Entry(root, justify=CENTER)
        port_entry.grid(row=0, column=1)
        port_entry.insert(0, '8000')
        self.port = int(port_entry.get())
        print('port is {}'.format(self.port))
        start_button = Button(root, text='Start', command=self.start, bg='yellow', fg='red')
        start_button.grid(row=1, column=0)

        root.mainloop()

    def start(self):
        print('start clicked')
        with socketserver.TCPServer(('', self.port), Handler) as httpd:
            print('servering at port {}'.format(self.port))
            httpd.serve_forever()


if __name__ == '__main__':
    print('run module')
    web = WebServer()
