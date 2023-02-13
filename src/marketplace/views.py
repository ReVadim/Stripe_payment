from django.views.generic import TemplateView
import os
from src.marketplace.models import Item
import stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class SuccessView(TemplateView):
    """ Redirects to the success URL
    """
    template_name = "marketplace/success.html"


class CancelView(TemplateView):
    """ Redirects to the Cancellation URL
    """
    template_name = "marketplace/cancel.html"


class ItemLandingPageView(TemplateView):
    """
    A product landing page that will display some information about our product, as well as offer the visitor to buy it
    """
    template_name = "marketplace/landing.html"

    def get_context_data(self, **kwargs):
        product = Item.objects.get(id=kwargs['item_id'])
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": os.getenv('STRIPE_PUBLIC_KEY')
        })

        return context
