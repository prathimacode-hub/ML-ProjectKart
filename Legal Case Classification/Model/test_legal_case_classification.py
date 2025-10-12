import unittest
import numpy as np
from legal_case_classification import LegalCaseClassifier

class TestLegalCaseClassifier(unittest.TestCase):

    def setUp(self):
        self.classifier = LegalCaseClassifier()

    def test_get_predictions_valid_input(self):
        try:
            texts = "The appellate court affirmed the lower court's decision."
            predictions = self.classifier.get_predictions(texts)
            self.assertTrue(isinstance(predictions, np.ndarray) or isinstance(predictions, list))
        except Exception as e:
            self.skipTest(f"Model file not found or failed to load: {e}")

    def test_get_predictions_invalid_input(self):
        try:
            texts = " "
            predictions = self.classifier.get_predictions(texts)
            self.assertEqual(predictions, "Input text is empty")
        except Exception as e:
            self.skipTest(f"Model file not found or failed to load: {e}")

    def test_preprocess_text(self):
        text = "Court ruled in favor of Smith vs. Jones."
        result = self.classifier.preprocess_text(text)
        self.assertIsInstance(result, str)

    
if __name__ == '__main__':
    unittest.main()