"""
가위바위보 게임
"""
import random

# 1. 조잡한 절차적 코딩 방식
# options = ['rock', 'paper', 'scissors']
# print('(1) Rock\n(2) Paper\n(3) Scissors')
# human_choice = options[int(input('Enter the number of your choice: ')) - 1]
# print(f'You chose {human_choice}')
# computer_choice = random.choice(options)
# print(f'The computer chose {computer_choice}')
# if human_choice == 'rock':
#     if computer_choice == 'paper':
#         print('Sorry, paper beat rock')
#     elif computer_choice == 'scissors':
#         print('Yes, rock beat scissors!')
#     else:
#         print('Draw!')
# elif human_choice == 'paper':
#     if computer_choice == 'scissors':
#         print('Sorry, scissors beat paper')
#     elif computer_choice == 'rock':
#         print('Yes, paper beat rock!')
#     else:
#         print('Draw!')
# elif human_choice == 'scissors':
#     if computer_choice == 'rock':
#         print('Sorry, rock beat scissors')
#     elif computer_choice == 'paper':
#         print('Yes, scissors beat paper!')
#     else:
#         print('Draw!')


# 조잡한 절차적 코딩을 리팩터링한 함수로 추출된 코드
# OPTIONS = ["rock", "paper", "scissors"]


# def get_computer_choice():
#     return random.choice(OPTIONS)


# def get_human_choice():
#     choice_number = int(input('Enter the number of your choice: '))
#     return OPTIONS[choice_number - 1]


# def print_options():
#     print("\n".join(f"({i}) {option.title()}" for i, option in enumerate(OPTIONS, 1)))


# def print_choices(human_choice, computer_choice):
#     print(f"You choose {human_choice}")
#     print(f"You computer choose {computer_choice}")


# def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
#     if computer_choice == human_loses_to:
#         print(f"Sorry, {computer_choice} beats {human_choice}")
#     elif computer_choice == human_beats:
#         print(f"Yes, {human_choice} beats {computer_choice}")


# def print_result(human_choice, computer_choice):
#     if human_choice == computer_choice:
#         print("Draw!")

#     if human_choice == "rock":
#         print_win_lose("rock", computer_choice, "scissors", "paper")
#     elif human_choice == "paper":
#         print_win_lose("paper", computer_choice, "rock", "scissors")
#     elif human_choice == "scissors":
#         print_win_lose("sccisors", computer_choice, "paper", "rock")


# print_options()
# human_choice = get_human_choice()
# computer_choice = get_computer_choice()
# print_choices(human_choice, computer_choice)
# print_result(human_choice, computer_choice)


# 함수형 코드에서 발생하는 중복 인자 처리를 위한 리팩터링 클래스 코드
class RockPaperScissors:
    def __init__(self):
        self.OPTIONS = ["rock", "paper", "scissors"]
        self.computer_choice = None
        self.human_choice = None

    def get_computer_choice(self):
        return random.choice(self.OPTIONS)

    def get_human_choice(self):
        choice_number = int(input("Enter the number of your choice: "))
        return self.OPTIONS[choice_number - 1]

    def print_options(self):
        print("\n".join(f"({i}) {option.title()}" for i, option in enumerate(self.OPTIONS, 1)))

    def print_choices(self, human_choice, computer_choice):
        print(f"You chose {human_choice}")
        print(f"Computer chose {computer_choice}")

    def print_win_lose(self, human_choice, computer_choice, human_beats, human_loses_to):
        if computer_choice == human_loses_to:
            print(f"Sorry, {computer_choice} beats {human_choice}")
        elif computer_choice == human_beats:
            print(f"Yes, {human_choice} beats {computer_choice}")

    def print_result(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            print("Draw!")

        if human_choice == "rock":
            self.print_win_lose("rock", computer_choice, "scissors", "paper")
        elif human_choice == "paper":
            self.print_win_lose("paper", computer_choice, "rock", "scissors")
        elif human_choice == "scissors":
            self.print_win_lose("scissors", computer_choice, "paper", "rock")

    def simulate(self):
        self.print_options()
        human_choice = self.get_human_choice()
        computer_choice = self.get_computer_choice()
        self.print_choices(human_choice, computer_choice)
        self.print_result(human_choice, computer_choice)


# 생성자를 적극 활용여 데이터의 중복 활용을 방지한 클래스 리팩터링 코드
class RockPaperScissorsSimulator:
    def __init__(self):
        self.OPTIONS = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.OPTIONS)

    def get_human_choice(self):
        choice_number = int(input("Enter the number of your choice: "))
        self.human_choice = self.OPTIONS[choice_number - 1]

    def print_options(self):
        print("\n".join(f"({i+1}) {option.title()}" for i, option in enumerate(self.OPTIONS)))

    def print_choices(self):
        print(f"You chose {self.human_choice}")
        print(f"Computer chose {self.computer_choice}")

    def print_win_lose(self, human_beats, human_loses_to):
        if self.computer_choice == human_loses_to:
            print(f"Sorry, {self.computer_choice} beats {self.human_choice}")
        elif self.computer_choice == human_beats:
            print(f"Yes, {self.human_choice} beats {self.computer_choice}")

    def print_result(self):
        if self.human_choice == self.computer_choice:
            print("Draw!")

        if self.human_choice == "rock":
            self.print_win_lose("scissors", "paper")
        elif self.human_choice == "paper":
            self.print_win_lose("rock", "scissors")
        elif self.human_choice == "scissors":
            self.print_win_lose("paper", "rock")

    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()


if __name__ == "__main__":
    RPS = RockPaperScissorsSimulator()
    RPS.simulate()
