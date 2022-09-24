from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('delobj/<objId>',views.delobj,name='delobj'),
    path('delAll',views.delAll,name='delAll'),
]