from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "id",
            "title",
            "code",
            "highlight",
            "linenos",
            "language",
            "style",
            "owner",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets", "url"]
