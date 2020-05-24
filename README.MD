# Art & Logic Software innovation Programming challenge

## Set up
* python 3.7.6_1

## file structure
* encoding.py
    * encoding class
* test_encoding.py
    * testing script
* encode_decode.bash
    * small application CLI 

# how to use class encoding
```python
    from encoding import Encoding

    # get class
    encoder = Encoding()
    
    # encode to decimal
    decimal =  encoder.encode_decimal("A")

    # encode to hex
    hex = encoder.encode_hex("A")

    # encode string to list of decimals
    encode = encoder.encode("tacocat")

    # decode decimal to string
    decode = encoder.decode_decimal(251792692)

    # decode array of decimals t0 string
    decode = encoder.decode([251792692, 125043731])
```

## how to run test
```
    python3 test_encoding.py
```

## how to start simple CLI
```
    chmod +x encode_decode.bash
    ./encode_encode.bash
```
