from hotqueue import HotQueue
from bottle import route, run, debug, request, ServerAdapter, abort
import time

queue = HotQueue("myqueue", host="localhost", port=6379, db=0)

@route('/certs/create', method='POST')
def create():
	name = request.POST['name']
	if name == None: abort(404, 'No name given')
	
	img_path = "cert_%d.jpg" % int(time.time())
	p = {}
	p['name']=name
	p['img_path']=img_path
	queue.put(p)
	return img_path


class GEventServerAdapter(ServerAdapter):
    def run(self, handler):
        from gevent import monkey
        monkey.patch_socket()
        from gevent.wsgi import WSGIServer
        WSGIServer((self.host, self.port), handler).serve_forever()

run(host='localhost', port=12000, server=GEventServerAdapter)
