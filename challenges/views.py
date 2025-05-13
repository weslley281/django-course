from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = "Isso está funcionando em janeiro"
    elif month == 'february':
        challenge_text = "Isso está funcionando em fevereiro"
    elif month == 'march':
        challenge_text = "Isso está funcionando em março"
    else:
        return HttpResponseNotFound("Isso não é suportado")

    return HttpResponse(challenge_text)