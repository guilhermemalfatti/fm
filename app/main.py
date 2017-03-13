from flask import Flask, render_template
from app import logger
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    """
    Initial method, responsible to redner the web application
    """
    logger.info('start render')
    try:
        return render_template('layout.html')
    except Exception as err:
        logger.error('ERROR' + str(err))
        return {'message': err}, 500

if __name__ == '__main__':
    logger.info("Application started.")
    app.run()
