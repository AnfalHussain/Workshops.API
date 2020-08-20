from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from api.views import (UserCreateAPIView, RegistrationItems,
                       WorkshopListView, ProfileUpdateView)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('workshops/', WorkshopListView.as_view(), name='workshops-list'),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("register/", RegistrationItems.as_view(), name="workshops-register"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
