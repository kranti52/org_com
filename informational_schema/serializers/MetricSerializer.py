from rest_framework import serializers

from ..models import Metric


class MetricSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True, max_length=1024)

    def __init__(self, instance=None, data=None, many=False):
        super().__init__(instance=instance, data=data, many=many)

    def create(self, validated_data):
        validation_error = {}
        if Metric.objects.filter(title=validated_data['title']).exists():
            validation_error['title'] = [" Metric with this title already exists. "]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        validated_data['object_type'] = 'metric'
        metric = Metric.objects.create(**validated_data)
        return metric

    def update(self, instance, validated_data):
        metric = instance
        validation_error = {}
        if Metric.objects.filter(title=validated_data['title']).exclude(id=instance.id).exists():
            validation_error['title'] = [" Metric with this title already exists. "]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        metric.title = validated_data['title']
        metric.description = validated_data['description']
        metric.save()
        return metric

    class Meta:
        model = Metric
        fields = ('title', 'description')
