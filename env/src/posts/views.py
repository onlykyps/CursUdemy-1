from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_home(request):
	return HttpResponse("<h1>Hello</h1>")

def post_create(request):
	return HttpResponse("<h1>Hello</h1>")

def post_detail(request):
	context_data = {
		"title":"detail"
	}
	return render(request, "index.html", context_data)
	# return HttpResponse("<h1>Hello</h1>")

def post_list(request):
	if request.user.is_authenticated():
		{
			context_data = {
								"title":"my user list"
							}		
			return render(request, "other_page.html", context_data)
		}
	else
		{
			context_data = {
								"title":"list"
							}		
		}

	
	return render(request, "index.html", context_data)
	# return HttpResponse("<h1>Hello</h1>")

def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse("<h1>Hello</h1>")