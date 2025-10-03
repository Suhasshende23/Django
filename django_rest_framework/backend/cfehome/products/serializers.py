from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["pk","url","title","content","price","sale_price","get_discount"]

        url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
            read_only=True
              )


    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()