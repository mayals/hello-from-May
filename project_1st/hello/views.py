from django.shortcuts import render
# Create your views here.
def sayhello(request):
    return render(request,"sayhello.html",{})
     


#----IT IS WORK OK ---- bellow another way for same result with out need template --------

# from django.http import HttpResponse

# def sayhello(request):
#     return HttpResponse("<h1>hello May</h1>")
