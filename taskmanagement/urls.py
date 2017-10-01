from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('main.urls'), name='main'),
    url(r'^task/', include('task.urls')),
    url(r'^admin/', admin.site.urls),
]


admin.site.site_header = 'TaskManagement Admin Panel'
admin.site.site_title = 'TaskManagement Admin Panel'
