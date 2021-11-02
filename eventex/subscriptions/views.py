from django.views.generic import DetailView

from subscriptions.forms import SubscriptionForm
from subscriptions.mixins import EmailCreateView
from subscriptions.models import Subscription

new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')

detail = DetailView.as_view(model=Subscription)
