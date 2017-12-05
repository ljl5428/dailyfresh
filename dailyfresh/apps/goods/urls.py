from django.conf.urls import url
from goods.views import index
urlpatterns = [
    url(r'^$', index, name='index'),  # 首页
]
