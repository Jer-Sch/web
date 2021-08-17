import pytest
import factory

from grants.models.cart_activity import CartActivity
from grant_factory import GrantFactory
from dashboard.tests.factories.profile_factory import ProfileFactory


@pytest.mark.django_db
class CartActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartActivity
    
    grant = factory.SubFactory(GrantFactory)
    profile = factory.SubFactory(ProfileFactory)
    metadata = {}
    bulk = True
    latest = True