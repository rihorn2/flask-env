from .flask_helper import FlaskHelper

class SharedServerBase:
    # A few design options here, can take an optional existing server 
    # app that user passes in. Can have a singleton so calling the 
    # constructor returns the existing one when available
    def __init__(self, *, shared_server, port, ip):
        self.shared_server = shared_server
        if self.shared_server is None:
            self.shared_server = FlaskHelper(port=port, ip=ip)