from django.urls import path
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .views import SignUpView

urlpatterns = [
	path("", chat_views.chat_page, name="chat-page"),
	# login-section
	path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
	path("auth/logout/", LogoutView.as_view(), name="logout-user"),
	path("register/", SignUpView.as_view(), name="create-user"),
]
