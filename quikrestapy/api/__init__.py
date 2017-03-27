import logging
import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Quick REST API',
          description='Quick REST API using Python/Flask')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': str(e)}, 404

@api.errorhandler(IntegrityError)
def database_IntegrityError(e):
    log.warning(traceback.format_exc())
    return {'message': 'Integrity Error Data already exist in the database'}, 404