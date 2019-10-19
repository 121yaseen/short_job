from django.shortcuts import render, render_to_response

def signup(request):
    return render_to_response('signup.html')
def index(request):
    return render_to_response('index.html')
