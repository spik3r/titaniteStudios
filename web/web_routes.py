from flask import *

web_routes = Blueprint("web_routes",__name__)


@web_routes.route('/')
@web_routes.route('/index')
@web_routes.route('/index.html')
def root():
    return render_template('site/base.html')

@web_routes.route('/about')
@web_routes.route('/about.html')
def about():
    return render_template('site/base.html')

@web_routes.route('/avlinks')
@web_routes.route('/avlinks.html')
def avlinks():
    return render_template('site/base.html')

@web_routes.route('/oldAVlinks')
@web_routes.route('/oldAVLinks.html')
def oldAVLinks():
    return render_template('site/base.html')

@web_routes.route('/api/v1/getHighscores')
def index():
    return "Eric - max lift: 5kg"

