"""
URL configuration for fronted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webApp.views import test

from webApp.views import set_all_lights_states

from webApp.views import set_lights_states
from webApp.views import set_transport_band
from webApp.views import set_garage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    path('set_all_lights_states/', set_all_lights_states, name='set_all_lights_states'),
    path('set_lights_states/', set_lights_states, name='set_lights_states'),
    path('set_transport_band/', set_transport_band, name='set_transport_band'),
    path('set_garage/', set_garage, name='set_garage'),

]
