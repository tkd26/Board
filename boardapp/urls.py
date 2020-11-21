from django.urls import path, include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/', goodfunc, name='good'),
    path('read/', readfunc, name='read'),
    # path('create/<int:userid>', BoardCreate.as_view(), name='create'),
    path('create/', BoardCreate.as_view(), name='create'),
]
