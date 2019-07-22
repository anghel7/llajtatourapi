from django.urls import path, include

from django.contrib import admin

from rest_framework import routers

from paquetes.views import PaqueteViewSet

from users.views import ClienteViewSet

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
router = routers.DefaultRouter()
router.register('paquetes', PaqueteViewSet)
router.register('clientes', ClienteViewSet)
router.register('users', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
