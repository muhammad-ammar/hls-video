#! /usr/bin/env python

import argparse
import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import socket


class VideoRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return os.path.join(self.root_dir, path.strip('/'))

    def end_headers(self):
        """
        This is required by hls.js to play hls videos.
        """
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)


class VideoTCPServer(SocketServer.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


def server(root_dir, port):
    Handler = VideoRequestHandler
    Handler.root_dir = root_dir
    httpd = VideoTCPServer(("", port), Handler)

    print "serving at port", port
    httpd.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=8888, type=int)
    parser.add_argument('--dir', '-d', default=os.getcwd(), type=str)
    args = parser.parse_args()

    server(args.dir, args.port)
