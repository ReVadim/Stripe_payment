from django.urls import path
from src.marketplace.views import CancelView, SuccessView, ItemLandingPageView
from src.services import CreateCheckoutSessionView


app_name = 'src.marketplace'


urlpatterns = [
    path('buy/', ItemLandingPageView.as_view(), name='landing-page'),

]
