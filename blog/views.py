from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Blogcomment
from django.contrib import messages

# Create your views here.
def bloghome(request):
      all_post = Post.objects.all()
      context = {"all_post": all_post}



      return render(request, "blog/bloghome.html", context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Blogcomment.objects.filter(post=post)
    context = {"post": post, "comments": comments, "user": request.user}
    return render(request, "blog/blogpost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sn=postSno)
        comment = Blogcomment(comment = comment, user =user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/blog/{post.slug}")