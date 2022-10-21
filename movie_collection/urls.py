from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
import movie.views
from movie import views
from rest_framework import routers

router_v1 = routers.DefaultRouter()
router_v1.register(r"movies", movie.views.MovieViewSet,basename="movies")
router_v1.register(r"collection", movie.views.CollectionViewSet)

# router_v1.register(r"request-count", movie.views.ReqCountViewSet)
# router_v1.register(r"reset", movie.views.ResetCountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("credy",views.AccessThirdPartyView,name="AccessThirdPartyView"),
    path('register', movie.views.authenticate_user, name='register'),
    path("", include(router_v1.urls), name="api-root"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('request-count/', views.ProcessRequestCount),
    path('request-count/reset/', views.ProcessRequestCount),
    

]
