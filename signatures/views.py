from django.shortcuts import render, HttpResponse
from random import sample


def home(request):
    return render(request, 'signatures/home.html', {})


def generate_new_signature(request, optional=None):
    greetings = update_greeting()
    if optional == 'oxford_comma':
        signature = '{}, {}, and {},'.format(greetings[0].title(), greetings[1], greetings[2])
    else:
        signature = '{}, {} and {},'.format(greetings[0].title(), greetings[1], greetings[2])
    return HttpResponse(signature)


def update_greeting():
    list_of_awesomeness = ["kittens", "cupcakes", "donuts", "rainbows", "hugs", "love", "puppies",
                           "dolphins", "ponies", "unicorns", "high fives", "cheers", "smiles", "cuddles", "thanks",
                           "success", "stars", "fun", "awesomeness", "laughter", "appreciation", "marshmallows",
                           "sparkles", "glitter", "hearts", "sunshine", "peace", "bubbles", "ducklings", "stroopwafels",
                           "pancakes", "butterflies"]
    greetings = sample(list_of_awesomeness, 3)
    return greetings


