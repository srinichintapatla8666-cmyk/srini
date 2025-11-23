from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to home or any desired page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def logout_view(request):
    """Log the user out and redirect to the login page."""
    logout(request)
    return redirect('login')






# from django.shortcuts import render, redirect
# from .forms import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login or your desired page.
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})









# from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from django.contrib import messages

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')
#             return redirect('myapp:index')
 
#     form = RegisterForm()
#     return render(request, 'users/register.html', {'form': form})













# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .forms import RegisterForm # type: ignore
# from django.contrib import messages
# # Create your views here.
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         email=request.POST['email']
#         # form=RegisterForm(request.POST)

#         # if form.is_valid():
#         user=User.objects.create_user(username=username,password=password,email=email)
#         user.save()    
#         form.save()
#             # username=form.cleaned_data.get('username')
#             # messages.success(request,f'Account created for {username}') 
#         return redirect('login')
#     else:
#         form=RegisterForm()
#     return render(request, 'users/register.html', {'form': form})









# from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from django.contrib import messages

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')
#             return redirect('myapp:index')
#  
#     form = RegisterForm()
#     return render(request, 'users/register.html', {'form': form})



 