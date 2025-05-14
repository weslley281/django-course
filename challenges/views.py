from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge_by_number(request, month):
    challenge_text = None

    if month == 1:
        challenge_text = "Isso está funcionando em janeiro"
    elif month == 2:
        challenge_text = "Isso está funcionando em fevereiro"
    elif month == 3:
        challenge_text = "Isso está funcionando em março"
    else:
        return HttpResponseNotFound("404 Página não encontrada")

    return HttpResponse(challenge_text)


def monthly_challenge(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = "Isso está funcionando em janeiro"
    elif month == 'february':
        challenge_text = "Isso está funcionando em fevereiro"
    elif month == 'march':
        challenge_text = "Isso está funcionando em março"
    else:
        return HttpResponseNotFound("404 Página não encontrada")

    return HttpResponse(challenge_text)