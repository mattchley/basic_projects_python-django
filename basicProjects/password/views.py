from django.shortcuts import render
import string
from random import *
from .forms import Password_Form

class Password:
        def __init__(self, length, letters, numbers, symbols, capitalization):
            self.length = length
            self.letters = letters
            self.numbers = numbers
            self.symbols = symbols
            self.capitalization = capitalization


def create_password(test):
        characters = string.ascii_letters
        symbols = string.punctuation
        numbers = string.digits

        if test.letters:
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
        else:
            print("working on the password")
            things = characters + numbers + symbols
            password = "".join(choice(things) for x in range(randint(test.length, test.length)))

            return password



def index(request):
    if request.method == 'POST':
        form = Password_Form(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            letters = form.cleaned_data['letters']
            numbers = form.cleaned_data['numbers']
            symbols = form.cleaned_data['symbols']
            capitalization = form.cleaned_data['capitalization']

            test = Password(length, letters, numbers, symbols, capitalization)
            
            password_obj = create_password(test)

    else:
        form = Password_Form()
        password_obj = None 
    
    

    return render(request, 'password/password.html', {'form':form, 'password_obj': password_obj })


# Create your views here.
