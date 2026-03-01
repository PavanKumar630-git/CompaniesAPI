from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="nic-login"),
    # path('policies/', views.list_policies),
    # path('policies/create/', views.create_policy),
    # path('policies/bulk/', views.bulk_insert),
]