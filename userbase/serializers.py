from rest_framework import serializers
from userbase.models import PublicKeys
from rest_framework.response import Response
from rest_framework import status

class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    public_key = serializers.CharField(required = True)

    class Meta:
        model=PublicKeys
        fields=['username', 'public_key']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self.Meta, 'read_only_fields', [*self.fields])

    def validate(self, attrs):
        username = attrs.get('username')
        public_key = attrs.get('public_key')
        username_count = PublicKeys.objects.filter(username=username).count()
        public_key_count = PublicKeys.objects.filter(public_key = public_key).count()

        if username_count > 0 or public_key_count > 0:
            return Response("404 Not Found", status=status.HTTP_404_NOT_FOUND)

        PublicKeys.objects.create(username = username, public_key = public_key)
        context = {'username':username,'public_key':public_key}

        return context

