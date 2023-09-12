from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "appname": "Inventory",
        "name": "Dwiky Ahmad Megananta",
        "class": "PBP D"
    }
    return render(request, "main.html", context)
