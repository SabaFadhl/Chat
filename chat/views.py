from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def chat_page(request, *args, **kwargs):
	"""
	Redirects the user to the login page if they are not authenticated.
	Renders the chat page if the user is authenticated.
	"""
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chat/chatPage.html", context)



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login-user")
    template_name = "chat/Signup.html"