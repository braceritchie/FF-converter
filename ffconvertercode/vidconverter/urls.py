from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'vidconverter'
urlpatterns = [
        path('<slug>',views.conv,name = 'filetype'),
        
        ]