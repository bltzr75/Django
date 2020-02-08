from django.shortcuts import render

from django.http import JsonResponse

def blog_list(request):
    context={
        'title': 'title here',
        'description': 'some description here'
    }
    return JsonResponse(context)

def home(request):
    return render(request, "blog/index.html", {})