from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        # You can add form processing logic
        return HttpResponse("Thank you for your message!")
    return render(request, 'contact.html')

def privacy(request):
    if request.method == 'POST':
        # Handle form submission here
        return HttpResponse("Thank you for your message!")
    return render(request, 'privacy.html')

def about(request):
    return render(request, 'about.html')
