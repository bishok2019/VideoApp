from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Video, News, Contact
from datetime import datetime
from django.contrib import messages

@login_required
def index(request):
    my_dict = {
        "insert_me": "Hello! I am from views.py",
        "user": request.user.username,
    }
    messages.success(request, f"Welcome to Bishok Multimedia, {request.user.username}!")
    return render(request, 'index.html', my_dict)

@login_required
def about(request):
    about_list = News.objects.all()
    return render(request, 'about.html', {'about_list': about_list})

@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been sent!')
    return render(request, 'contact.html')

@csrf_exempt
@login_required
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'service.html', {'videos': videos})

@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    user = request.user
    if user in video.disliked_by.all():
        video.disliked_by.remove(user)
        video.dislikes -= 1
    if user not in video.liked_by.all():
        video.liked_by.add(user)
        video.likes += 1
    else:
        video.liked_by.remove(user)
        video.likes -= 1
    video.save()
    return JsonResponse({'likes': video.likes, 'dislikes': video.dislikes})

@login_required
def dislike_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    user = request.user
    if user in video.liked_by.all():
        video.liked_by.remove(user)
        video.likes -= 1
    if user not in video.disliked_by.all():
        video.disliked_by.add(user)
        video.dislikes += 1
    else:
        video.disliked_by.remove(user)
        video.dislikes -= 1
    video.save()
    return JsonResponse({'likes': video.likes, 'dislikes': video.dislikes})