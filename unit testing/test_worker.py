import unittest
from worker import Worker


class TestWorker(unittest.TestCase):

    def test_fullname(self):
        worker_1 = Worker('Franz', 'Friedrich', 50000)
        worker_2 = Worker('Gabriela', 'Gabel', 55000)

        self.assertEqual(worker_1.fullname, 'Franz Friedrich')
        self.assertEqual(worker_2.fullname, 'Gabriela Gabel')

        worker_1.first = 'Frederik'
        worker_2.first = 'Gundula'

        self.assertEqual(worker_1.fullname, 'Frederik Friedrich')
        self.assertEqual(worker_2.fullname, 'Gundula Gabel')

    def test_emai(self):
        worker_1 = Worker('Franz', 'Friedrich', 50000)
        worker_2 = Worker('Gabriela', 'Gabel', 55000)

        self.assertEqual(worker_1.email_address, 'Franz.Friedrich@email.de')
        self.assertEqual(worker_2.email_address, 'Gabriela.Gabel@email.de')

        worker_1.last = 'Gabel'
        worker_2.last = 'Friedrich'

        self.assertEqual(worker_1.email_address, 'Franz.Gabel@email.de')
        self.assertEqual(worker_2.email_address, 'Gabriela.Friedrich@email.de')

    def test_apply_raise(self):
        worker_1 = Worker('Franz', 'Friedrich', 50000)
        worker_2 = Worker('Gabriela', 'Gabel', 55000)

        worker_1.apply_raise()
        worker_2.apply_raise()

        self.assertEqual(worker_1.pay, 53000)
        self.assertEqual(worker_2.pay, 58300)


if __name__ == '__main__':
    unittest.main()
