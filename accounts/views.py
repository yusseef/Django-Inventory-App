from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def AccountLoginView(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username, password)
        user = authenticate(request, username = username, password = password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, 'accounts/AccountLogin.html', context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/AccountLogin.html', context)

def AccountLogoutView(request):
    context = {}
    return render(request, 'accounts/AccountLogout.html', context)

def AccountRegisterView(request):
    context = {}
    return render(request, 'accounts/Accountregister.html', context)