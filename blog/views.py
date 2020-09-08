from django.shortcuts import render
from .models import Blog

# Create your views here.
def allblogs(request):
	Blogs = Blog.objects
	return render(request,'blog/allblogs.html',{'allBlogs':Blogs})