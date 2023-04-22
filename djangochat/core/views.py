from django.shortcuts import render ,redirect
from django.contrib.auth import login 
from .form import SignUpForm

# Create your views here.

def frontpage(request):

    data = {
        'title':"Welcome | DjangoChat"
    }
    return render(request , 'core/frontpage.html' ,data)

def signup(request):
    print("test1")
    if request.method == "POST":
        print("test2")
        form = SignUpForm(request.POST)
        username = request.POST.get("username","")
        password1 = request.POST.get("password1","")
        password2 = request.POST.get("password2","")
        print("username:",username)
        print("password1:",password1)
        print("password2:",password2)
        print(form.is_valid())
        if form.is_valid():
            print("test3")
            user = form.save()
            print("test4")
            login(request, user)
            return redirect("frontpage")
        else:
            print(form.errors)
        
    else :
        print("test5")
        form = SignUpForm()
    print("test6")
    return render(request, 'core/signup.html',{'form':form})



    

