from rest_framework.viewsets import ModelViewSet
from support.models import Ticket, Comment
from support.permissions import IsOwnerOrAdminUser
from support.serializers import UserTicketSerializer, AdminTicketSerializer, CommentSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminTicketSerializer
        return UserTicketSerializer

    permission_classes = [IsOwnerOrAdminUser]

    def perform_create(self, serializer):
        serializer.validated_data['username'] = self.request.user
        serializer.save()


class CommentViewSet(ModelViewSet):
    def get_queryset(self):
        ticket_id = self.kwargs['id']
        queryset = Comment.objects.filter(ticket__id=ticket_id)
        return queryset

    permission_classes = [IsOwnerOrAdminUser]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


