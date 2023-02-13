from django.test import TestCase
from .models import Item
from config.wsgi import *


class ItemTestCase(TestCase):
    def testItem(self):
        item = Item(name='Tesla', description='Electrical car', price=1200)
        self.assertEqual(item.name, 'Tesla')
        self.assertEqual(item.description, 'Electrical car')
        self.assertEqual(item.price, 1200)