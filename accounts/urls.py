from django.views.generic.base import RedirectView
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", RedirectView.as_view(url='dashboard/', permanent=True)),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("post_passage/", views.post_view, name="post"),
    path("logout/", views.logout_view, name='logout'),
    path("delete_passage/<int:passage_id>/", views.delete_passage_view, name="delete_passage"),
    path("edit_passage/<int:passage_id>/", views.edit_passage_view, name="edit_passage"),
    path("change_username/", views.change_username, name="change_username"),
    path("user_profile/", RedirectView.as_view(url='/', permanent=False)),
    path("user_profile/<int:userid>/", views.user_profile_view, name="user_profile"),
    path("sms_code/", views.sms_code_view, name="fill_sms_code")
]