from django.shortcuts import render


# Create your views here.
def specify(request):
  return render(request, 'specify.html')

def mapHeaders(request):
  return render(request, 'mapHeaders.html')

def confirm(request):
  return render(request, 'confirm.html')
