import pytest
from grants.models.cart_activity import CartActivity

from .factories import CartActivityFactory


@pytest.mark.django_db
class TestCartActivity:
    def test_creation(self):
        cart_activity = CartActivityFactory()

        assert isinstance(cart_activity, CartActivity)

    def test_cart_activity_has_add_remove_and_clear_actions(self):
        ACTIONS = (
            ('ADD_ITEM', 'Add item to cart'),
            ('REMOVE_ITEM', 'Remove item to cart'),
            ('CLEAR_CART', 'Clear cart')
        )
        cart_activity = CartActivityFactory()

        assert cart_activity.ACTIONS == ACTIONS

    def test_cart_activity_belongs_to_profile(self):
        cart_activity = CartActivityFactory()
        
        assert cart_activity.profile.id != None

    def test_cart_activity_has_metadata(self):
        cart_activity = CartActivityFactory()

        assert cart_activity.metadata == {}
    
    def test_cart_activity_has_bulk_attribute(self):
        cart_activity = CartActivityFactory()

        assert cart_activity.bulk == True

    