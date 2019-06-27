from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
	print(args, kwargs);
	print(request.user);
	return render(request, "home.html", {});

def contact_view(request, *args, **kwargs):
	my_context = {
		"my_text": "What about us?",
		"my_num": 124,
		"my_list": ["yeet", "yort", "yart"]
	}
	return render(request, "contact.html", my_context);