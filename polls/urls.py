from django.conf.urls import url, include
from rest_framework import routers

from polls.views import UserView
from . import views


router= routers.SimpleRouter()
router.register(r'^users',UserView)


urlpatterns = [
    url(r'', include(router.urls)),
]

