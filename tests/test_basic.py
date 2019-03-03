# -*- coding: utf-8 -*-
"""
    :author: TingTuShuo (听图说)
    :url: http://tingtushuo.com
    :copyright: © 2018 TingTuShuo <tingtushuo@hotmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app

from tests.base import BaseTestCase


class BasicTestCase(BaseTestCase):

    def test_app_exist(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_404_error(self):
        response = self.client.get('/foo')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn('404 Error', data)