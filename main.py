#!/usr/bin/env python3


import random
import subprocess

TIMES = 10
HARDNESS = 3    # How many digits in the question
TOTAL_SCORE = 100


class BColors:
    """
    Color tags for the terminal output.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Game:

    class Question:
        """
        Question object for the game which contains the answer.
        """

        def __init__(self, hardness):
            self.answer = random.randint(0, 10 ** hardness)

        def ask(self):
            """
            Plays the question to the user.
            """
            subprocess.run(["say", "-v", "Kyoko", str(self.answer)])

        def check(self, answer):
            """
            Checks if the given answer is correct.
            """
            return self.answer == answer

    def __init__(self, times, hardness):
        """
        Constructor for initializing the parameters.
        """
        self.times = times
        self.hardness = hardness
        self.questions = [
            self.Question(hardness)
            for _ in range(self.times)
        ]
        self.score = 0
        self.score_step = TOTAL_SCORE / self.times

    def start(self):
        """
        Starts the game.
        """
        for i in range(self.times):

            # Gets the question
            question = self.questions[i]

            # Asks the question
            print("Question %d, please listen." % (i + 1))
            question.ask()

            # Gets the user answer
            user_answer = input("Answer is >> ")

            # Asks again if no input
            while not user_answer:
                question.ask()
                user_answer = input("Answer is >> ")

            # Checks the answer
            try:
                if question.check(int(user_answer)):
                    print(BColors.OKGREEN + "Yes" + BColors.ENDC)
                    self.score += self.score_step
                else:
                    print(BColors.FAIL + "No!" + BColors.ENDC)
                    print("Answer is " + str(question.answer))

            except ValueError:
                print("Wrong input, skipped.")

    def print_score(self):
        """
        Prints the score.
        """
        print("Your score is %d / %d." % (self.score, TOTAL_SCORE))


def main():
    """
    Main entry function of the program.
    """
    game = Game(TIMES, HARDNESS)
    game.start()
    game.print_score()


if __name__ == "__main__":
    main()
