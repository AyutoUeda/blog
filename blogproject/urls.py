from django.contrib import admin
from django.urls import path, incluse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', incluse('blogpost.urls'))
]
