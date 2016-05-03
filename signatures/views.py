from django.shortcuts import render, HttpResponse
from random import sample


def home(request):
    return render(request, 'signatures/home.html', {})


def generate_new_signature(request):
    signature = update_greeting()
    return HttpResponse(signature)


def update_greeting():
    list_of_awesomeness = ["kittens", "cupcakes", "donuts", "rainbows", "hugs", "love", "puppies",
        "dolphins", "ponies", "unicorns", "high fives", "cheers", "smiles", "cuddles", "thanks",
        "success", "stars", "fun", "awesomeness", "laughter", "appreciation", "marshmallows",
        "happiness", "chocolate", "dreams", "sweetness", "strawberries", "wins", "wows", "flowers",
        "sparkles", "glitter", "hearts", "sunshine", "peace", "bubbles", "ducklings", "stroopwafels",
        "pancakes", "butterflies"]
    greetings = sample(list_of_awesomeness, 3)
    greeting = '{}, {}, and {},'.format(greetings[0].title(), greetings[1], greetings[2])

    return greeting


