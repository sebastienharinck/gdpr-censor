# GDPR Censor
Aims to anonymize string data for GDPR compliance.

## Quickstart
```python
import gdpr
print(gdpr.anonymize("""
Hi ! My name is John Doe and I want to say that I am very glad to be a customer of your store in Paris.
Patricia, my advisor helps me a lot to choose my products.
I give you my phone number to call me about my joy : 07 12 34 56 78.
"""))
```

The results should be :
```
Hi ! My name is FIRST_NAME LAST_NAME and I want to say that I am very glad to be a customer of your store in Paris.
FIRST_NAME, my advisor helps me a lot to choose my products.
I give you my phone number to call me about my joy : PHONE_NUMBER.
```

## How to contribute ?
```
git clone git@github.com:odaxiom/gdpr-censor.git
cd gdpr-censor
pip3 install -e .
python3 -m unittest discover
```
