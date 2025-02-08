from django.shortcuts import render
from django.http import JsonResponse
from .aiengine import *


def home(request):
    
    context = {}
    if request.method == 'POST':
        prompt = request.POST['prompt']
        res = {}
        res['answer'] = generateChatResponse(prompt)
        return JsonResponse(res)
    return render(request, 'profiles/index.html',context)