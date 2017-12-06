from django.shortcuts import render
from django.views.generic import View
from goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner

from django_redis import get_redis_connection

# Create your views here.
# Create your views here.
class IndexView(View):
    def get(self, request):
        types = GoodsType.objects.all()

        index_banner = IndexGoodsBanner.objects.all().order_by("index")

        promotion_banner = IndexPromotionBanner.objects.all().order_by('index')

        for type in types:
            title_banner = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

            image_banner = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')

            type.title_banner = title_banner
            type.image_banner = image_banner


        user = request.user

        cart_count = 0

        if user.is_authenticated():
            conn = get_redis_connection('default')
            cart_key = 'cart_%d'%user.id
            cart_count = conn.hlen(cart_key)

        context = {'types': types,
                   'index_banner': index_banner,
                   'promotion_banner': promotion_banner,
                   'cart_count': cart_count}

        # 使用模板
        return render(request, 'index.html', context)