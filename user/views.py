
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserUpdateForm, UserDeleteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import get_user_model

from django.contrib import messages
from .models import User
from django.db.models import Q
User = get_user_model()


@login_required
def profile_view(request):
    return render(request, 'user/profile.html', {'user': request.user})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect after successful user creation
    else:
        form = UserCreationForm()
    return render(request, 'user/create_user.html', {'form': form})
@login_required(login_url='login')
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'user/update_user.html', {'form': form})



@login_required(login_url='login')
def delete_user(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list') 
    return render(request, 'user/user_list.html')

@login_required
def user_list(request):
    users = User.objects.all()
     
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(
            Q(email__icontains=query) |
            Q(name__icontains=query) |
            Q(user_type__icontains=query) |
            Q(education__icontains=query) |
            Q(membership_number__icontains=query)
        )
    else:
        users = User.objects.all()

    context = {
        'users': users,
        'search_query': query
    }
    context = {
        'users': users
    }
    return render(request, "user/user_list.html", context)
@login_required(login_url='login')
def update_user_status(request, user_id):
    
    if request.method == 'POST':
        
        user = get_object_or_404(User, id=user_id)
        # Update the is_active status
        user.is_active = request.POST.get('is_active') == 'on'
        user.save()
        # Redirect back to the user list or any other appropriate page
        return redirect('user_list') 





