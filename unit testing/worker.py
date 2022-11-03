class Worker:
    raise_amount = 1.06

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email_adress(self):
        return '{}.{}@email.de'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Worker.raise_amount)


'''
worker_1 = Worker('Max', 'Mustermann', 40000)
print(worker_1.pay)
worker_1.apply_raise()
print(worker_1.pay)
'''