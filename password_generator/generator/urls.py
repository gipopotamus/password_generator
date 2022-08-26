from django.urls import path
from .views import password, home

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('password', password, name="password"),
]