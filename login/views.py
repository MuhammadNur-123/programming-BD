from pipes import quote
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
import random
from django.core.mail import send_mail
from user.models import User 
from instructor.models import Instractor
from all_course.models import Course
from enroll.models import Enrolled
from blog.models import Blog ,Course_Module
import requests
from isodate import parse_duration

# @login_required(login_url='login')
def dashboard_view(request):
    total_members = User.objects.filter(user_type='MEM').count()
    total_admin = User.objects.filter(user_type='ADM').count()
    total_cordinator = User.objects.filter(user_type='CCN').count()
    total_instractor =Instractor .objects.count()
    total_course = Course.objects.count()
    
    total_blog = Blog.objects.count()  
    total_module = Course_Module.objects.count()  
    total_enroll = Enrolled.objects.count() 
    

    context = {
        'total_members': total_members,
        'total_admin': total_admin,
        'total_cordinator': total_cordinator,
        'total_instractor': total_instractor,
        'total_course': total_course,
        'total_blog': total_blog,
        'total_module': total_module,
        'total_enroll': total_enroll,
        
      
    }
    

    return render(request, 'main/dashboard.html',context)
def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))

# Step 1: Password reset request view
def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['email'] = email  # Store email in session to confirm OTP later

            # Send OTP via email
            send_mail(
                'Password Reset OTP',
                f'Your OTP for resetting the password is {otp}.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'OTP sent to your email.')
            return redirect('password_reset_confirm')
        except User.DoesNotExist:
            messages.error(request, 'No user with this email found.')
            return redirect('password_reset_request')

    return render(request, 'login/password_reset_request.html')


# Step 2: Password reset confirmation view
def password_reset_confirm(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if otp == request.session.get('otp'):
            if password == confirm_password:
                email = request.session.get('email')
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successful.')
                return redirect('login')  # Redirect to login after successful reset
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Invalid OTP.')

    return render(request, 'login/password_reset_confirm.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user based on email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Redirect to the dashboard or home page
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def forgot_password_view(request):
    return render(request, 'login/forgotpassword.html')

def contact(request):
    return render(request,'includes/contact.html')

def youtube_search(request):
    videos = []
    if request.method == "POST":
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part': 'snippet',
            'q': request.POST['search'],
            'key': settings.YOUTUBE_API_KEY,
            'maxResults': 10,
            'type': 'video',
        }

        video_ids = []
        r = requests.get(search_url, params=search_params)
        results = r.json()['items']
        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'part': 'snippet, contentDetails',
            'key': settings.YOUTUBE_API_KEY,
            'id': ','.join(video_ids),
            'maxResults': 18,
        }
        r = requests.get(video_url, params=video_params)
        results = r.json()['items']
        for result in results:
            video_data = {
                'title': result['snippet']['title'],
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={result["id"]}',
                'thumbnail': result['snippet']["thumbnails"]['high']['url'],
                'duration': int(parse_duration(result['contentDetails']["duration"]).total_seconds()//60),
            }
            videos.append(video_data)
    context = {
        'videos': videos
    }
    return  render(request, 'main/youtube.html', context)
