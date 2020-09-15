from django.contrib import admin
from django.urls import path, include

default = [
    # Admin
    path('admin/', admin.site.urls),
]

# django-rest-framework
# -------------------------------------------------------------------------------
drf = [
    # Auth
    path('api-auth/', include('rest_framework.urls')),
]

api_v1 = []

urlpatterns = default + drf + api_v1