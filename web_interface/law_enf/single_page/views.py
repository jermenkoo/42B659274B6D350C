from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Query

# Create your views here.


@csrf_exempt
def get_transcript(request):
    if request.method == 'POST':
        # text, encrypted_phone
        text = request.POST.get("text")
        encrypted_phone = request.POST.get("enc_phone")
        obj = Query(
            transcript=text,
            encrypted_phone=encrypted_phone
        )
        obj.save()
    return JsonResponse({"success": True})


def home(request):
    objects = Query.objects.all()
    return render(request, 'index.html', {'objects': objects})

@csrf_exempt
def decrypt(request):
    print(request.POST)
    number = request.POST["data"]
    #write decrypt function here
    return JsonResponse({"number": number})
