from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register("logo", LogoView)
router.register("contactus", ContactUsView)
router.register("category", CategoryView)
router.register("videonews", VideoNewsView)
router.register("news", NewsView)
router.register("loyihalar", LoyixalarView)
router.register("xaftanews", XaftaNewsView)
router.register("city", CityView)
router.register("safarlar", SafarlarView)
router.register("category2", Category2View)
router.register("members", MembersView)
router.register("channels", ChannelsView)
router.register("conntecting", ConntectingView)