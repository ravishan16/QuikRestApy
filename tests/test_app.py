#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quikrestapy.app import initapp

__author__ = "Ravi"
__copyright__ = "Ravi"
__license__ = "none"


class TestApp:
    def test_app(self):
        app = initapp()
        assert app.config['SERVER_HOST']