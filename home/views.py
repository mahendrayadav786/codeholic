from django.shortcuts import render, HttpResponse
from django.contrib import messages
# Create your views here.
from .models import Contact
from blog.models  import Post

def home(request):
    all_post = Post.objects.all()

    context = {"all_post": all_post}

    return render(request, "home/home.html", context)

def about(request):
    return render(request, "home/about.html")

def contact(request):

        if request.method == "POST":
            name = request.POST["name"]
            phone = request.POST["phone"]
            email = request.POST["email"]
            desc = request.POST["textarea"]

            if len(name)<3 or len(phone)<10 or len(desc)<10:
                messages.error(request, 'Enter a valid input.')
            else:
                contact = Contact(name = name, email = email, phone = phone, textarea = desc)
                contact.save()
                messages.success(request, 'Your form has been submitted.')



        return render(request, "home/contact.html")