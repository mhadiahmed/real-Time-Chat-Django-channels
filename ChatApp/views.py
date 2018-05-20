from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
	title = "my Chat"
	return render(request,'main.html',{"title":title})

def chat(request):
	if request.method != "POST":
		return HttpResponseRedirect(reverse('index'))
	else:
		title = "Chat Room"
		username = request.POST.get('username')
		return render(request,'chat.html',{"title":title,"username":username})