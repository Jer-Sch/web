import pytest
from dashboard.models import Profile
from grants.models.cart_activity import CartActivity
from grants.models.grant import Grant

from .factories.cart_activity_factory import CartActivityFactory


@pytest.mark.django_db
class TestCartActivity:
    def test_creation(self):
        cart_activity = CartActivityFactory()

        assert isinstance(cart_activity, CartActivity)

    def test_cart_activity_belongs_to_grant(self):
        cart_activity = CartActivityFactory()

        assert isinstance(cart_activity.grant, Grant)

    def test_cart_activity_belongs_to_profile(self):
        cart_activity = CartActivityFactory()
        
        assert isinstance(cart_activity.profile, Profile)

    def test_cart_activity_has_action_attribute(self):
        cart_activity = CartActivityFactory()

        assert hasattr(cart_activity, "action")
        assert cart_activity.action == ''

    def test_cart_activity_has_metadata_attribute(self):
        cart_activity = CartActivityFactory()

        assert hasattr(cart_activity, "metadata")
        assert cart_activity.metadata == {}
        assert len(cart_activity.metadata) == 0
    
    def test_cart_activity_has_bulk_attribute(self):
        cart_activity = CartActivityFactory()

        assert hasattr(cart_activity, "bulk")
        assert cart_activity.bulk == False

    def test_cart_activity_has_latest_attribute(self):
        cart_activity = CartActivityFactory()

        assert hasattr(cart_activity, "latest")
        assert cart_activity.latest == False
