from rest_framework.serializers import ModelSerializer
from support.models import Ticket, Comment


class CommentSerializer(ModelSerializer):
    """Сериалайзер для комментариев"""

    class Meta:
        model = Comment
        fields = '__all__'


class UserTicketSerializer(ModelSerializer):
    """Ticket сериалайзер для пользователя"""

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('status',)


class AdminTicketSerializer(ModelSerializer):
    """Ticket сериалайзер для админа"""

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('username', 'issue', 'description',)
