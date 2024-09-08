from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152361',
        'name': 'Peter Putra Lesmana',
        'class': 'PBP B',
        
    }

    return render(request, "main.html", context)