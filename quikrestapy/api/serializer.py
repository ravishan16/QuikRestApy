from flask_restplus import fields
from quikrestapy.api import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of user'),
    'username': fields.String(required=True, description='username'),
    'email': fields.String(required=True, description='Email'),
})