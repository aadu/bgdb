from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .game.views import GameViewSet, MechanicViewSet, SubcategoryViewSet
from .user.views import UserCreateViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'games', GameViewSet)
router.register(r'mechanics', MechanicViewSet)
router.register(r'subcategories', SubcategoryViewSet)

schema_view = get_schema_view(title='BGDB API')

urlpatterns = [
    path(r'schema/', schema_view),
    path(r'admin/', admin.site.urls),
    path(r'api/v1/', include(router.urls)),
    path(r'api-token-auth/', views.obtain_auth_token),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
