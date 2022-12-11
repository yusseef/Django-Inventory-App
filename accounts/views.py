from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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
    if request.method == 'POST':
        logout(request)
        return redirect('AccountLogin')
    return render(request, 'accounts/AccountLogout.html', context)

def AccountRegisterView(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('AccountLogin')
    
    context = {'form': form}
    return render(request, 'accounts/AccountRegister.html', context)