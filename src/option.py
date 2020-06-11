import inquirer
import re


def setOption():
    questions = [
        inquirer.Text('num', message="How many generate Ethereum wallet? (1~100)",
                      validate=lambda _, x: re.fullmatch(r'[1-9]|[1-9][0-9]|100', x),),
        inquirer.List(
            "output",
            message="How do you output?",
            choices=["console", ".txt",
                     ".xlsx"],
            carousel=False,
        )
    ]
    answers = inquirer.prompt(questions)
    return answers
