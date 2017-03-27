import logging

from flask import request
from flask_restplus import Resource
from quikrestapy.api import api
from quikrestapy.models.usermodel import User
from quikrestapy.api.serializer import user
from quikrestapy.models import db

log = logging.getLogger(__name__)

user_ns = api.namespace('user/list', description='Operations related to Users')

@user_ns.route('/')
class Users(Resource):
    @api.marshal_list_with(user)
    def get(self):
        """
        Returns list of Users.
        """
        print "Iam Here"
        user = User.query.all()
        return user


    @api.response(201, 'Category successfully created.')
    @api.expect(user)
    @api.marshal_list_with(user)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        user = User(data.get('username'), data.get('email'))
        db.session.add(user)
        db.session.commit()
        return user, 201