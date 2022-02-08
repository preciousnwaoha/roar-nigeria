import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assetIn('English', my_survey.responses)

unittest.main()