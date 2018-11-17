from flask import Flask, send_from_directory, request, Response, flash, stream_with_context, jsonify, \
    render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import json


class Web(object):
    def __init__(self, scraper):
        self.site = Flask(__name__)
        self.env = Environment(
                loader=PackageLoader('frontEnd', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
        )
        scraper.generate_stats()
        self.routes()

    def stream_template(self, template_name, **context):
        self.site.update_template_context(context)
        t = self.site.jinja_env.get_template(template_name)
        rv = t.stream(context)
        rv.enable_buffering(5)
        return rv

    def getResults(self):
        return 'name'

    def routes(self):
        @self.site.route("/")
        def index():
            context = self.getResults()
            return Response(self.stream_template('index.html'))


