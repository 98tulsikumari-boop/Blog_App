from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    subscribed_on = serializers.DateTimeField(
        format="%d %B %Y, %I %M %p",
        read_only=True
    )

    class Meta:
        model = Subscriber
        fields = "__all__"
        read_only_field = ['subscribed_on']

    def validate_email(self, value):
        if Subscriber.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already subscribed.")
        return value