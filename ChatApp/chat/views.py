from django.shortcuts import render, redirect


def chat_page(request, *args, **kwargs):
	"""
	Redirects the user to the login page if they are not authenticated.
	Renders the chat page if the user is authenticated.
	"""
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
	return render(request, "chat/chatPage.html", context)