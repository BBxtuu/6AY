from django.shortcuts import render

def profile_view(request):
    return render(request, 'users/profile.html')

def contact(request):
    return render(request, 'users/contact.html')