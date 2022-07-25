"""thedoorofmercy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('Home.urls')),
	#path('/testimonials/', include('Testimonials.urls')),
	#path('/alms/', include('Alms.urls')),
	path('/sermons/', include('Catalog.urls')),
	#path('/biblequiz/', include('BibleQuiz.urls')),
	#path('/biblestudy/', include('BibleStudy.urls')),
	#path('/hymns/', include('Hymns.urls')),
	#path('/miracles/', include('Miracles.urls')),
	path('/prayers/', include('Prayers.urls')),
	path('/thanksgivings/', include('Thanksgivings.urls')),
]
