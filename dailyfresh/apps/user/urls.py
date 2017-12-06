from django.conf.urls import url
from apps.user.views import RegisterView, ActiveView, LoginView, UserInfoView,UserOrderView, AddressView, LogoutView,IndexView

urlpatterns = [
    url("^register$", RegisterView.as_view(), name='register'),
    url(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    url(r'^index$', IndexView.as_view(), name='index'),
    url(r'^order$', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    url(r'^address$', AddressView.as_view(), name='address'),  # 用户中心-地址页
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 退出登录
]
