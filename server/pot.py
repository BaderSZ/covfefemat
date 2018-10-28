'''

@author: Bader Zaidan 
'''
# global Header variables.
# this should be later added in a config file

import flask
from flask import request
import platform
import logging
from pi import Pi


class Pot(object):
    
    server = "covfefemat"
    version = 0.01
    host = 'localhost'
    port = 80
    logging.basicConfig(format='%(asctime)s $(levelname)s: %(message)s')
    logging.info("Initialising: %s/%d %s:%d", server, version, host, port)

    response = flask.Response()
    response.headers['Server'] = server + "/" + str(version) + " Python" + "/" + str(platform.python_version())
    global control
    
    
    def __init__(self, name), gpio_port):
        self.name = name
        self.gpio_port = gpio_port
        control = Pi("Pi") gpio_port)

    def get(self):
        logging.info("GET via %s", request.remote_addr)
        control.brew_status()
        self.response.status_code = 200
        self.response.status = "200 OK Get Stat"
        self.response.add_etag()
        return self.response
 
    def head(self):
        logging.info("HEAD via %s", request.remote_addr)
        control.brew_status()
        self.response.status_code = 200
        self.response.status = "200 OK HEAD"
        self.response.add_etag()
        return self.response

    def brew(self):
        logging.info("BREW via %s", request.remote_addr)
        control.start_brew()
        self.response.status_code = 200
        self.response.status = "200 OK Brew in Progress"
        self.response.add_etag()
        return self.response
        
    def pot(self):
        logging.warn("UNDOCUMENTED POT")
        self.response.status_code = 406
        self.response.status = "406 Not Applicable"
        self.response.add_etag()
        return self.response
        
    def propfind(self):
        logging.warn("UNDOCUMENTED PROPFIND")
        self.response.status_code = 406
        self.response.status = "406 Not Applicable"
        self.response.add_etag()
        return self.response
    
    def teapot(self):
        logging.warn("Not a teapot!")
        self.response = "I am not a teapot!"
        self.response.status_code = 406
        self.response.status = "406 Not applicable"
        self.response.add_etag()
        return self.response
        
    def about(self):
        logging.warn("UNDOCUMENTED ABOUT")
        # header object not callabe
        # define page/data struct to return in compatible way
        return flask.abort(404)
    
    def when(self):
        logging.warn("WHEN method called, no milk on this device")
        self.response.status_code = 406
        self.response.status = "406 Not Applicable"
        self.response.add_etag()
        return self.response


