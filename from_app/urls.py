from django.urls import path
from from_app.views import IndexPage, update_view, delete_view, post, show

urlpatterns = [
    path('', IndexPage, name="home"),
    path('create/', post, name="create"),
    path('show/<int:id>', show, name="show"),
    path('edite/<int:pk>', update_view, name="edite"),
    path('delete/<int:pk>/', delete_view, name='delete_view'),

]
