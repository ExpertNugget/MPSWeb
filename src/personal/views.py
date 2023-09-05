from django.shortcuts import render

# Create your views here.

def home_screen_view(request):

    context = {}

    list = []
    list.append("forst")
    list.append("second")
    list.append('third')

    context['list'] = list

    return render(request, "personal/home.html", context)