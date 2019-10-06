from rest_framework import serializers

from ..models import Issue


class IssueSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=255)
    category = serializers.CharField(required=True, max_length=255)

    def __init__(self, instance=None, data=None, many=False):
        super().__init__(instance=instance, data=data, many=many)

    def create(self, validated_data):
        validation_error = {}
        if Issue.objects.filter(title=validated_data['title']).exists():
            validation_error['title'] = [" Issue with this title already exists. "]
        if validated_data['category'] not in dict(Issue.ISSUE_CHOICES):
            validation_error['category'] = [" Invalid Category. "]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        validated_data['object_type'] = 'issue'
        issue = Issue.objects.create(**validated_data)
        return issue

    def update(self, instance, validated_data):
        issue = instance
        validation_error = {}
        if Issue.objects.filter(title=validated_data['title']).exclude(id=instance.id).exists():
            validation_error['title'] = [" Issue with this title already exists. "]
        if validated_data['category'] not in dict(Issue.ISSUE_CHOICES):
            validation_error['category'] = [" Invalid Category. "]
        if validation_error:
            raise serializers.ValidationError(validation_error)

        issue.title = validated_data['title']
        issue.category = validated_data['category']
        issue.save()
        return issue

    class Meta:
        model = Issue
        fields = ('title', 'category')
