from flask import *
from web.web_routes import web_routes


application = Flask(__name__)

application.register_blueprint(web_routes)

@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    application.run()
