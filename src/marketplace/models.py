from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Item(models.Model):
    """ Simple product model, include: name, description and price
    """
    name = models.CharField(
        max_length=150,
        verbose_name=_('item name')
    )
    description = models.CharField(
        max_length=2000,
        verbose_name=_('description')
    )
    price: int = models.IntegerField(
        default=0,
        verbose_name=_('price'),
        validators=[MinValueValidator(0)]
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return f'Item {self.name}: {self.price}'

    def get_real_price(self):
        return "{0:.2f}".format(self.price / 100)


class OrderItem(models.Model):
    """ Intermediate model for content information about the product and quantity in the buyer's cart
    """

    order_item = models.ForeignKey(
        Item, on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('items')
    )
    quantity = models.PositiveIntegerField(
        default=1
    )
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='buyer',
        verbose_name=_('buyer')
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def get_total_items_price(self):
        return self.quantity * self.order_item.price

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.buyer} item: {self.order_item}'


class Order(models.Model):
    """ An Order model in which you can combine several Items and make a payment in Stripe
            for the contents of an OrderItem with the total cost of all Items
        """

    class Status(models.TextChoices):
        """ choice OrderItem status
        """
        DRAFT = 'DF', 'Draft'
        PAYED = 'PD', 'Payed'

    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='order_buyer',
        verbose_name=_('buyer')
    )
    items = models.ManyToManyField(OrderItem)

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    status = models.CharField(
        max_length=2,
        verbose_name=_('status'),
        choices=Status.choices,
        default=Status.DRAFT
    )

    def __str__(self):
        return f'{self.buyer} created at {self.created}. Status {self.status}'

    def total_price(self):
        """ Calculate total price in cart
        """
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_items_price()
        return total

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]