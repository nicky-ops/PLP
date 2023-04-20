import unittest
class Tdd_Python(unittest.TestCase):
    def test_banking_credit_method_returns_correct_result(self):
        bank = Banking()
final_bal = bank.credit(1000)
self.assertEqual(1000, final_bal)
