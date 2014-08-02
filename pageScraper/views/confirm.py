from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def confirm(request):
  return render(request, 'confirm.html')

