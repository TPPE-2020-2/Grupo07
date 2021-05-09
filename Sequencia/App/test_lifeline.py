import unittest
from lifeline import Lifeline

class LifelineTest(unittest.TestCase):
    def test_get_name_fals(self):
        lifeline = Lifeline('Lifeline fals')
        self.assertEqual(lifeline.get_name_fals(), 'Lifeline fals')
    def test_lifelines(self):
        lifelines = Lifeline('Lifeline 1')
        self.assertEqual(lifelines.lifeline['nomeLifeline'], 'Lifeline 1')

    # def setUp(self):
    #     self.lifeline = Lifeline()

    # #falsificacao    
    # def test_get_name_fals(self):
    #     self.assertEqual(self.lifeline.get_name_fals(), 'Lifeline Teste')

    # def test_set_name(self):
    #     self.lifeline.set_name('name')
    #     self.assertEqual(self.lifeline.get_name(), 'name')

    # def test_set_names(self):
    #   self.lifeline.set_name(self.lifeline.name)
    #   self.assertEqual(self.lifeline.get_name(), self.lifeline.name)


# if __name__ == "__main__":
#   unittest.main()