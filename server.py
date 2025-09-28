from flask import Flask
from code import register_blueprints
from Config import Settings


def create_app() -> object:
    """
    """

    app = Flask(__name__)
    register_blueprints(app)

    return app



def start_server(settings:object):
    """
    """

    app = create_app()
    app.config.from_object(settings)
    
    app.run(port=app.config['PORT'], host=app.config['HOST'])




if __name__ == '__main__':
    start_server(Settings)
