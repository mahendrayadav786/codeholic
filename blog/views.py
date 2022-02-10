from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.
def bloghome(request):
      all_post = Post.objects.all()
      context = {"all_post": all_post}



      return render(request, "blog/bloghome.html", context)

def blogpost(request, slug):
    blog_post = Post.objects.filter(slug=slug)
    context = {"blog_post": blog_post}
    return render(request, "blog/blogpost.html", context)