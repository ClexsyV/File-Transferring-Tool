from .api import api
from .pages import pages


def register_blueprints(app):
    """
    """

    app.register_blueprint(api)
    app.register_blueprint(pages)
