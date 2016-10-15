from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def get_transcript(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse({"success": True})
