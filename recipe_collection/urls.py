from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from checking import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# 	path('api_recipe/', include('checking.urls')),
# ]

urlpatterns = [
	path('admin/', admin.site.urls),
    # path('', include('frontend.urls')),
    path('', include('checking.urls')),
    # path('', include('accounts.urls'))
]
