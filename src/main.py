import inquirer
from pyfiglet import Figlet

from src import addressManager
from src import option


def main():
    f = Figlet(font="slant")
    msg = f.renderText("Ethereum Wallet Generator")
    print(msg)
    options = option.setOption()
    addressManager.generateWallet(options)


if __name__ == "__main__":
    main()
