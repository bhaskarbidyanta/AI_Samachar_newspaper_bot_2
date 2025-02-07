from django.shortcuts import render



def home(request):
    #Write the Page Base Function Logic in here
    context = {}
    return render(request, 'profiles/index.html',context)