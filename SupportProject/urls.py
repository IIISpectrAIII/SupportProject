from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from support.views import TicketViewSet, CommentViewSet

router = SimpleRouter()

router.register(r'ticket', TicketViewSet)
router.register(r'ticket/(?P<id>\d+)/comments', CommentViewSet, basename='Comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^auth/', include('djoser.urls')),
    path(r'^auth/', include('djoser.urls.jwt')),
]

urlpatterns += router.urls
