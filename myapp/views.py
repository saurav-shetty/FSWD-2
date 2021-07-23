from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        contact.fname=fname
        contact.lname=lname
        contact.email=email
        contact.city=city
        contact.state=state
        contact.zip=zip
        contact.save()
        return HttpResponse("<h3>THANKS FOR CONTACT US</h3>")
    
    return render(request,'index.html')
