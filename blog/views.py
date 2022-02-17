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
    comments = Blogcomment.objects.filter(post=post, parent=None)
    replies = Blogcomment.objects.filter(post =post).exclude(parent =None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)




    context = {"post": post, "comments": comments, "user": request.user, "replyDict": replyDict}
    return render(request, "blog/blogpost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sn=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = Blogcomment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "You have commented on this")

        else:
            parent = Blogcomment.objects.get(sno = parentSno)
            comment = Blogcomment(comment = comment, user =user, post=post, parent =parent)
            comment.save()
            messages.success(request, "You reply has been posted successfully")

        return redirect(f"/blog/{post.slug}")



