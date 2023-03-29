from django.urls import path
from . import views
urlpatterns = [
    path('shows',views.allshows),
    path('shows/new',views.create_show),
    path('handle_form',views.handle_form),
    path('shows/<int:id>',views.show_details),
    path('shows/<int:id>/edit',views.edit_show),
    path('shows/<int:id>/handle_form',views.update_show),
    path('shows/<int:id>/delete',views.delete_show),
] 