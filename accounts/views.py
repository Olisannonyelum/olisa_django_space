
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from accounts.forms import article_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def register_veiw(request):
    form = UserCreationForm(request.POST or None)# this is the form for creating new user
    if form.is_valid():
        obj = form.save()
        return redirect('/login')
                        
    context = {
        'form': form    
    }

    return render(request, "accounts/register.html", context=context)

#the usercrationform is the form mustely use to register user, django provide this to make registering a user easy or registering user
# it provide future as to clean the data that is pass in to the form 


def login_view(request): 
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): #this is authenticate to see if the user is in the system
            user = form.get_user() # this will return the user detail if the authentication whent well
            """
                it work like the authentication function where it check username and password
            """
            print("this here is the shit........", user)
            if user is not None:
                login(request, user)
                return redirect('/admin')

    else:
        form = AuthenticationForm(request)

    context = {
        "form": form
    }


        # password = request.POST.get("password")
        # username = request.POST.get("username")
        # # remeber to remove this for security reason
        # print(password, username)
        # user = authenticate(request, username=username, password=password)
        # if user is None:
        #     context = {"error": "Invalin username or password."}
        #     return render(request, "accounts/login.html", context)
        # print(user) 
        # login(request, user) 
        # return redirect('/admin') #from your basic python this return will brack you out of the if block
    return render(request, "accounts/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
        print("requste sent in")
        # put in mind the redirect function work with return
    print("requste not sent in")
    return render(request, "accounts/logout.html", {})

