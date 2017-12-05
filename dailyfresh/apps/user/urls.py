from django.conf.urls import url
from apps.user.views import RegisterView, ActiveView, LoginView

urlpatterns = [
    url("^register$", RegisterView.as_view(), name='register'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
]
