import unittest

from flask import current_app

from app import create_app, db
from app.models import Order
from db_backup import load_data


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()
        load_data.load(db)

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_order(self):
        orders = Order.query.filter_by(customer_id="87").all()
        self.assertTrue(len(orders) == 5)
