from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# List users
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# Create or Update user
def user_form(request, id=None):
    if id:
        user = get_object_or_404(User, pk=id)
    else:
        user = None
    form = UserForm(request.POST or None, instance=user)
    
    if form.is_valid():
        form.save()
        return redirect('user_list')

    return render(request, 'user_form.html', {'form': form})

# Delete user
def user_confirm_delete(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'user_confirm_delete.html', {'user': user})
