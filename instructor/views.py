from django.shortcuts import render, redirect, get_object_or_404
from .models import Instractor
from .forms import InstractorForm ,InstractorUpdateForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def create_instractor(request):
    if request.method == 'POST':
        form = InstractorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('instractor_list')
    else:
        form = InstractorForm()
    return render(request, 'instractors/instractor_form.html', {'form': form})

@login_required(login_url='login')
def update_instractor(request,id):
    instractor = get_object_or_404(Instractor, id=id)
    if request.method == 'POST':
        form = InstractorUpdateForm(request.POST, request.FILES, instance=instractor)
        if form.is_valid():
            form.save()
            # return redirect('instractor_list')  # Redirect to the list after successful update
    else:
        form = InstractorUpdateForm(instance=instractor)
    return render(request, 'instractors/update_instractor.html', {'instructor': instractor,'form': form})

@login_required(login_url='login')
def delete_instractor(request,id):
    instractor = get_object_or_404(Instractor,id=id)
    if request.method == 'POST':
        instractor.delete()
        return redirect('instractor_list')
    return render(request, 'instractors/confirm_delete.html', {'instractor': instractor})

@login_required(login_url='login')
def instractor_list(request):
    instractors = Instractor.objects.all()
    return render(request, 'instractors/instractor_list.html', {'instractors': instractors})


def instractor_profile(request):
    instractors = Instractor.objects.all()
    
    return render(request, 'instractors/instractor_profile.html', {'instractors': instractors})
