from django.conf.urls import url
from .views import Home

app_name="Prediction"
urlpatterns = [
    url(r'^$', Home,name="home"),
]
