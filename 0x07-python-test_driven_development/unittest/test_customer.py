import unittest
from customer import Customer

class Testcustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Mkelvo", "Prince", 1000)
        self.customer_2 = Customer("The", "Prince", 10000)

    def test_customer_mail(self):
        self.assertAlmostEqual(self.customer_1, "Mkelvo.Prince@gmail.com")
        self.assertAlmostEqual(self.customer_2, "The.Prince@gmail.com")

    def test_customer_fullname(self):
        self.assertAlmostEqual(self.customer_1, "Mkelvo Prince")
        self.assertAlmostEqual(self.customer_2, "The Prince")

    def test_apply_discount(self):
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()

        self.assertAlmostEqual(self.customer_1.purchase, 950)
        self.assertAlmostEqual(self.customer_2.purchase, 9500)

if __name__ == "__main__":
    unittest.main()