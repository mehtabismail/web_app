from django.shortcuts import render, get_object_or_404
from . models import blog
# Create your views here.

def home(request):
    blog_variable = blog.objects
    return render(request, 'blog/index.html', {'blog': blog_variable})


#def detail(request, blog_id):
    #detailblog = get_object_or_404(blog, pk=blog_id)
    #return render(request, 'blog/details.html', {'blog': detailblog})
