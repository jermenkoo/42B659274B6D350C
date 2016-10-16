from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Query
import string
# Create your views here.


@csrf_exempt
def get_transcript(request):
    if request.method == 'POST':
        # text, encrypted_phone
        text = request.POST.get("text")
        encrypted_phone = request.POST.get("enc_phone")
        obj = Query(
            transcript=text,
            encrypted_phone=encrypt(encrypted_phone)
        )
        obj.save()
    return JsonResponse({"success": True})


def home(request):
    objects = Query.objects.all()
    return render(request, 'index.html', {'objects': objects})

@csrf_exempt
def _decrypt(request):
    number = request.POST["data"]
    return JsonResponse({"number": decrypt("12345678", number)})

charset = string.digits + string.ascii_lowercase + string.ascii_uppercase


def encrypt(key, message):
    translated = []
    index = 0
    for symbol in message:
        num = charset.find(symbol)
        if num != -1:
            num += charset.find(key[index])
            num %= len(charset)

            index += 1
            if index == len(key):
                index = 0
            translated.append(charset[num])
        else:
            translated.append(symbol)
    return ''.join(translated)


def decrypt(key, message):
    translated = []
    index = 0
    for symbol in message:
        num = charset.find(symbol)
        if num != -1:
            num -= charset.find(key[index])
            num %= len(charset)

            index += 1
            if index == len(key):
                index = 0
            translated.append(charset[num])
        else:
            translated.append(symbol)
    return ''.join(translated)
