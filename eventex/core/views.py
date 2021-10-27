from django.shortcuts import render


def home(request):
    speakers = [
        {'nama': 'Grace Hopper', 'photo':'http://hbn.link/hopper-pic'},
        {'nama': 'Alan Turing', 'photo':'http://hbn.link/turing-pic'},
    ]
    
    return render(request, 'index.html')
