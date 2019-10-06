from rest_framework import serializers

from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True, max_length=1024)

    def __init__(self, instance=None, data=None, many=False):
        super().__init__(instance=instance, data=data, many=many)

    def create(self, validated_data):
        validation_error = {}
        if Product.objects.filter(title=validated_data['title']).exists():
            validation_error['title'] = [" Product with this title already exists. "]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        validated_data['object_type'] = 'product'
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        product = instance
        validation_error = {}
        if Product.objects.filter(title=validated_data['title']).exclude(id=instance.id).exists():
            validation_error['title'] = [" Product with this title already exists. "]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        product.title = validated_data['title']
        product.description = validated_data['description']
        product.save()
        return product

    class Meta:
        model = Product
        fields = ('title', 'description')
