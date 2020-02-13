import unittest
from gdpr import AnonymizerTransformer


class GDPRTests(unittest.TestCase):
    def test_gdpr_v1(self):
        """
        First test to improve.
        """
        text = """
Hi ! My name is John Doe and I want to say that I am very glad to be a customer of your store in Paris.
Patricia, my advisor helps me a lot to choose my products.
I give you my phone number to call me about my joy : 07 07 07 07 07.
        """
        at = AnonymizerTransformer()
        anonymized = at.transform(text)

        self.assertEqual(anonymized,
        """
 Hi ! My name is PROPN PROPN and I want to say that I am very glad to be a customer of your store in PROPN . 
 PROPN , my advisor helps me a lot to choose my products . 
 I give you my phone number to call me about my joy : 07 07 07 07 07 . 
        """
        )

    # def test_gdpr(self):
    #     anonymized = gdpr.anonymize(
    #     """
    #     Hi ! My name is John Doe and I want to say that I am very glad to be a customer of your store in Paris.
    #     Patricia, my advisor helps me a lot to choose my products.
    #     I give you my phone number to call me about my joy : 07 07 07 07 07.
    #     """
    #     )

    #     self.assertEqual(anonymized,
    #     """
    #     Hi ! My name is FIRST_NAME LAST_NAME and I want to say that I am very glad to be a customer of your store in Paris.
    #     FIRST_NAME, my advisor helps me a lot to choose my products.
    #     I give you my phone number to call me about my joy : PHONE_NUMBER.
    #     """
    #     )
