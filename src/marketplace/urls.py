from django.urls import path, include
from src.marketplace.views import CancelView, SuccessView, ItemLandingPageView


app_name = 'src.marketplace'


urlpatterns = [
    path('buy/', include([
        path('cancel/', CancelView.as_view(), name='cancel'),
        path('success/', SuccessView.as_view(), name='success'),
        path('', ItemLandingPageView.as_view(), name='landing-page'),
    ])),
]
