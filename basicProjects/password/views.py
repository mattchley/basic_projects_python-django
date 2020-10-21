from django.shortcuts import render
from django.http import HttpResponse
import string
from random import *


def index(request):
    class Password:
        def __init__(self, length, letters, numbers, symbols, capitalization):
            self.length = length
            self.letters = letters
            self.numbers = numbers
            self.symbols = symbols
            self.capitalization = capitalization


    test = Password(20, False, True, True, True)

    def create_password(test):
        characters = string.ascii_letters
        symbols = string.punctuation
        numbers = string.digits

        if 128 >= test.length >= 12:
            print("this password will be %s long" % test.length)
        else:
            print("you need to create a different kind of password")
        if test.letters == True:
            print("Letters will be used")
        else:
            characters = ''

        if test.capitalization:
            characters = characters.upper()
        else:
            characters = characters.lower()

        if test.numbers:
            print("Numbers will be used")
        else:
            numbers = ''

        if test.symbols:
            print("Symbols will be used")
        else:
            symbols = ''

        if test.letters == False and test.numbers == False and test.symbols == False:
            print("I can't make a password with nothing :(")
            sys.exit()
        else:
            print("working on the password")
            things = characters + numbers + symbols
            password = "".join(choice(things) for x in range(randint(test.length, test.length)))
            print(password)

    create_password(test)
    return HttpResponse("Hello, world. You're at the password index.")


# Create your views here.
