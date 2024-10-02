from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def post_home(request):
	return HttpResponse("<h1>Hello</h1>")

def post_create(request):
	return HttpResponse("<h1>Hello</h1>")

def post_detail(request, id):
	# instance = Post.objects.get(id=1)

	instance = get_object_or_404(Post, id=id)

	context_data = {
		"title":"detail",
		"instance": instance.title
	}
	return render(request, "post_detail.html", context_data)
	# return HttpResponse("<h1>Hello</h1>")

def post_list(request):
	# if request.user.is_authenticated():
	# 	{
	# 		context_data = {
	# 							"title":"my user list"
	# 						}		
	# 		return render(request, "other_page.html", context_data)
	# 	}
	# else
	# 	{
	# 		context_data = {
	# 							"title":"list"
	# 						}		
	# 	}

	queryset = Post.objects.all()

	context_data = {
	"object_list": queryset,
	"title":"list"
	}	
	return render(request, "index.html", context_data)
	# return HttpResponse("<h1>Hello</h1>")

def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse("<h1>Hello</h1>")