import logging

from flask import request
from flask_restplus import Resource
from quikrestapy.api import api
from quikrestapy.models.usermodel import User
from quikrestapy.api.apimodel import user
from quikrestapy.models import db

log = logging.getLogger(__name__)

user_ns = api.namespace('user/v1', description='Operations related to Users')

@user_ns.route('/list')
class UsersList(Resource):
    @api.marshal_list_with(user)
    @api.response(200, 'List of All User.')
    def get(self):
        """
        Returns list of Users.
        """
        print "Iam Here"
        user = User.query.all()
        return user,200

@user_ns.route('/create')
class UsersCreate(Resource):
    @api.response(201, 'Category successfully created.')
    @api.expect(user)
    @api.marshal_list_with(user)
    def post(self):
        """
        Creates a new User.
        """
        data = request.json
        user = User(data.get('username'), data.get('email'))
        db.session.add(user)
        db.session.commit()
        return user, 201

@user_ns.route('/fetch/<string:email>')
class UsersID(Resource):
    @api.marshal_list_with(user)
    @api.response(200, 'List of All User.')
    @api.response(404, 'User not found')
    # @user_ns.param('email', 'The task identifier')
    def get(self,email):
        """
        Returns One Users.
        """
        print "Iam Here",email
        userOne = User.query.filter(User.email == email).one()
        return userOne