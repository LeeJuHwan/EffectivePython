"""슈퍼클래스의 기존 동작을 사용하면서 해당 동작을 특화 시키기"""

class Teller:
    def deposit(self, amount, account):
        account.deposit(amount)


class CorruptTeller(Teller):
    def __init__(self):
        self.coffers = 0

    def deposit(self, amount, account):
        self.coffers += amount * 0.01
        super().deposit(amount * 0.99, account)
