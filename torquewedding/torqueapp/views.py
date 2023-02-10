from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Func,Contact
# Create your views here.

def index(request):
    func=Func.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        email = request.POST.get('email')
        contact = Contact(name=name, mobile=mobile, place=place, email=email)
        contact.save()
        return redirect('/info')
    return render(request, 'index.html', {'func':func})

def detail(request,func_id):
    func=Func.objects.get(id=func_id)
    return  render (request,"detail.html",{'func': func})

def info(request):
    return render(request,"info.html")

def test(request):
    return render(request,"test.html")
