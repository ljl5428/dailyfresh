from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('apps.user.urls', namespace='user')), # 用户模块
    url(r'^cart/', include('apps.cart.urls', namespace='cart')), # 购物车模块
    url(r'^order/', include('apps.order.urls', namespace='order')), # 订单模块
    url(r'^', include('apps.goods.urls', namespace='goods')), # 商品模块

]
