# For WiCS UWaterloo 2018 CTF

from argparse import ArgumentParser
from jinja2 import Template
import cherrypy
import os


PATH = os.path.abspath(os.path.dirname(__file__))


class Root(object):
    pass


class Challenge(object):
    @cherrypy.expose
    def index(self):
        with open('index.html', 'r') as f:
            return f.read()

    @cherrypy.expose
    def page(self, page_num=1):
        try:
            pgint = int(page_num)
        except ValueError:
            pgint = -1

        # They should get a chance to see that page 5 is _different_
        if pgint == 5:
            with open('page5.html', 'r') as f:
                return f.read()

        if pgint > 0 and pgint < 5:
            with open('pageview.j2.html', 'r') as f:
                pv = Template(f.read())
            return pv.render(num=pgint)

        with open('index.html', 'r') as f:
            return f.read()


if __name__ == '__main__':
    ap = ArgumentParser(
        description='The web server for the Inchuun Challenge CTF question.'
        )
    ap.add_argument('--port', '-p',
        type=int, help='The port number for the web'
        'server to run on.', default=8080)
    args = ap.parse_args()

    cherrypy.tree.mount(Root(), '/', config={
            '/': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': PATH,
                    'tools.staticdir.index': 'index.html',
                },
        })
    cherrypy.tree.mount(Challenge(), '/exam')

    cherrypy.config.update({
        'server.socket_port': args.port,
        'server.socket_host': '0.0.0.0',
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
