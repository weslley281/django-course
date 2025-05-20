from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge_by_number(request, month):
    challenges = {
        1: "Isso está funcionando em janeiro",
        2: "Isso está funcionando em fevereiro",
        3: "Isso está funcionando em março"
    }

    challenge_text = challenges.get(month)
    if challenge_text is None:
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