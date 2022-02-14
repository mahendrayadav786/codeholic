from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import Contact
from blog.models  import Post

#HANDLE TEMPLATES
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


def search(request):
    # if request.method == "GET":
    query = request.GET["query"]
    print(query)
    blog_post = Post.objects.filter(query)
    context = {"all_post": blog_post}
    return render(request, "home/search.html", context)


#HANDLE authenticate APIS
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST["user_name"]
        Fname = request.POST["Fname"]
        Lname = request.POST["Lname"]

        email = request.POST["email"]
        password = request.POST["pass1"]
        confirm_pasaword = request.POST["pass2"]
        print(username)
        #CHECK ERROR!
        if password != confirm_pasaword:
            messages.error(request, 'Password and confirm password do not match.')
            return redirect("home")

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = Fname
        myuser.last_name = Lname
        myuser.save()
        messages.success(request, 'Your have been registered with us.')
        return redirect("home")


    else:
        return HttpResponse("404 -Not Found")


def handlelogin(request):
    if request.method =="POST":
        username = request.POST["username"]
        user_password = request.POST["login_pass"]

        user = authenticate(username = username, password = user_password)
        if user is not None:
            login(request, user)
            messages.success(request, "Youu have successfully loged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid credential")
            return redirect("/")

    return HttpResponse("login page")

def handlelogout(request):
    logout(request)
    messages.success(request, "Youu have successfully loged out")
    return redirect("/")



    return HttpResponse("logout paage")
