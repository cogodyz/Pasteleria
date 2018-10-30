"""MisPerris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from apps.formulario.views import index,formulario_view
from django.conf import settings
<<<<<<< HEAD
from django.contrib.auth.views import login, logout
=======
<<<<<<< HEAD
from django.contrib.auth.views import login, logout
=======
>>>>>>> 7e29db11c3e125ffec6bca5cbdb64ed8e348db2e
>>>>>>> 03b713bf1865f2e09b026cd8da2184f6da3b1f83

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^formulario/', formulario_view, name='contacto'),
<<<<<<< HEAD
     url(r'^rescate/', include('apps.rescate.urls')),
     url(r'^login/$', login),
    url(r'^logout/$', logout),
<<<<<<< HEAD
=======
=======
    url(r'^rescate/', include('apps.rescate.urls')),
>>>>>>> 7e29db11c3e125ffec6bca5cbdb64ed8e348db2e
>>>>>>> 03b713bf1865f2e09b026cd8da2184f6da3b1f83
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
