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
    price = models.PositiveSmallIntegerField(
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


class Order(models.Model):
    """ An Order model in which you can combine several Items and make a payment in Stripe
        for the contents of an Order with the total cost of all Items
    """
    class Status(models.TextChoices):
        """ choice Order status
        """
        DRAFT = 'DF', 'Draft'
        PAYED = 'PD', 'Payed'

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
    status = models.CharField(
        max_length=2,
        verbose_name=_('status'),
        choices=Status.choices,
        default=Status.DRAFT
    )

    def total_cost(self):
        """ Calculates the total cost of the order
        """
        pass

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.buyer} created at {self.created}. Status {self.status}'
