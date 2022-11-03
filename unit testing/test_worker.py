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


if __name__ == '__main__':
    unittest.main()