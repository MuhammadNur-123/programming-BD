from django.shortcuts import render, get_object_or_404, redirect
from .models import Enrolled
from .forms import EnrolledForm
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa  # You need to install this package
from django.contrib.auth.decorators import login_required




# List of enrolled students
@login_required(login_url='login')
def enrolled_list(request):
    enrolled_students = Enrolled.objects.all()
    return render(request, 'enroll/enrolled_list.html', {'enrolled_students': enrolled_students})

# Detailed view of a particular enrollment
@login_required(login_url='login')
def enrolled_detail(request, pk):
    enrolled = get_object_or_404(Enrolled, pk=pk)
    return render(request, 'enroll/enrolled_detail.html', {'enrolled': enrolled})

# Create a new enrollment
@login_required(login_url='login')
def enrolled_create(request):
    if request.method == 'POST':
        form = EnrolledForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrolled_list')
    else:
        form = EnrolledForm()
    return render(request, 'enroll/enrolled_form.html', {'form': form})

# Update an enrollment
@login_required(login_url='login')
def enrolled_update(request, pk):
    enrolled = get_object_or_404(Enrolled, pk=pk)
    if request.method == 'POST':
        form = EnrolledForm(request.POST, instance=enrolled)
        if form.is_valid():
            form.save()
            return redirect('enrolled_detail', pk=enrolled.pk)
    else:
        form = EnrolledForm(instance=enrolled)
    return render(request, 'enroll/enrolled_form.html', {'form': form})

# Delete an enrollment
@login_required(login_url='login')
def enrolled_delete(request, pk):
    enrolled = get_object_or_404(Enrolled, pk=pk)
    if request.method == 'POST':
        enrolled.delete()
        return redirect('enrolled_list')
    return render(request, 'enroll/enrolled_confirm_delete.html', {'enrolled': enrolled})



@login_required(login_url='login')
def enrolled_download_pdf(request, pk):
    enrolled = get_object_or_404(Enrolled, pk=pk)
    template_path = 'pdf/enrolled_pdf.html'  # Create this template for PDF
    context = {'enrolled': enrolled}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{enrolled.course_name}_enrollment.pdf"'

    # Generate PDF
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)

    # Check if PDF generation was successful
    if pisa_status.err:
        return HttpResponse('We had some errors while generating the PDF <pre>' + html + '</pre>')
    
    return response
@login_required(login_url='login')
def support_course(requset):
    return render(requset,'enroll/support_course.html')