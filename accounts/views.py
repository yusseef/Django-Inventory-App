from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def AccountLoginView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    
    context = {'form': form}
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