from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:read')
    else:
        form = UserForm()
    return render(request, 'user/create_user.html', {'form': form})

def update_user(request, id_user):
    user = get_object_or_404(User, id_user=id_user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:read')
    else:
        form = UserForm(instance=user)
    return render(request, 'user/update_user.html', {'form': form})

def delete_user(request, id_user):
    user = get_object_or_404(User, id_user=id_user)
    if request.method == 'POST':
        user.delete()
        return redirect('user:read')
    return render(request, 'user/delete_user.html', {'user': user})
