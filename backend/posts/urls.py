from django.urls import path
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


# Used with viewsets
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls


# Used with generics views
# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
# ]
