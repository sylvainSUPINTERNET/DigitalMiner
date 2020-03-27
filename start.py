from colorama import init
from menu.index import menu
from menu.welcome import fidget


# Init for colorama use need it to use termcolor etc ...
init()

if __name__ == '__main__':
    fidget()
    menu()
