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
        "sparkles", "glitter", "hearts", "sunshine", "peace", "bubbles"]
    indexes = sample(range(0, len(list_of_awesomeness)), 3)
    greeting = list_of_awesomeness[indexes[0]].title() + ", " + list_of_awesomeness[indexes[1]] + " and " \
            + list_of_awesomeness[indexes[2]] + ","

    return greeting


