from django.conf import settings
from ..marketplace.models import Item


class Cart(object):
    """ Class Cart for managing shopping cart
    """
    def __init__(self, request):
        """ The cart needs to be initialized using the request object
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """ Sorting through items in the basket and getting products from the database
        """
        product_ids = self.cart.keys()
        products = Item.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """ Counting all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        """ Updating the cart session
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        # Mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        """ Adds the product to the cart or updates its quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """ Removing an item from the shopping cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """ deleting a shopping cart from a session
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        """ Calculating the cost of all items in the shopping cart
        """
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())
