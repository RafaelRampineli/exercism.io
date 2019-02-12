# Class used to implement Lock objects. One thread has acquired a lock and subsequent other threads acquire it blocks
from threading import Lock


class BankAccount(object):
    def __init__(self):
        self._balance = 0
        self._state = 'created'
        self._lock_Thread = Lock()

    def get_balance(self):
        if self._state != 'opened':
            raise ValueError("Cannot get balance from a closed account")
        else:
            return self._balance

    def open(self):
        self._state = 'opened'

    def deposit(self, amount):
        if self._state != 'opened':
            raise ValueError("Cannot deposit into a closed account")
        else:
            if amount < 0:
                raise ValueError("Cannot deposit negative values")
            else:
                with self._lock_Thread:
                    self._balance += amount

    def withdraw(self, amount):
        if self._state != 'opened':
            raise ValueError("Cannot withdraw from closed account")
        elif amount > self._balance:
            raise ValueError("Cannot withdraw more than deposited")
        else:
            if amount < 0:
                raise ValueError("Cannot withdraw negative values")
            else:
                with self._lock_Thread:
                    self._balance -= amount

    def close(self):
        self._state = 'closed'
