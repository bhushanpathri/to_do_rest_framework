"""to_do_project URL Configuration

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
from django.urls import path,include
from to_do_app import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path("task_ki_yadi/",views.task_ki_yadi,name="task_ki_yadi"),
    path("task_create/",views.task_create,name="task_create"),
    path("task_detailss/<int:pk>/",views.task_details,name="task_details"),
    path("task_class/",views.task_list.as_view(),name="task_class"),
    path("task_details_class/<int:pk>/",views.task_detail.as_view(),name="task_details_class")
]

