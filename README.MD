# Art & Logic Software innovation Programming challenge

## Set up
* python 3.7.6_1

## file structure
* encoding.py
    * encoding class
* test_encoding.py
    * testing script

# how to use class encoding
```python
    from encoding import Encoding

    # get class
    encoder = Encoding()
    
    # get decimal
    decimal =  encoder.encode_decimal("A")

    # get hex
    hex = encoder.encode_hex("A")
```

## how to run test
```
    python3 test_encoding.py
```
