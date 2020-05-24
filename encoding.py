import sys
###################################################################### 
# Encoding  
###################################################################### 
class Encoding:
    
    def __init__(self):
        pass

    # public
    def encode_decimal(self, string):
        """
        gives decimal encryption
        @param string is a string 
        @return decimal value of encrypted string
        """
        return int(self.__encrypt(string), 2)

    def encode_hex(self, string):
        """
        gives hex encryption
        @param string is a string
        @return decimal value of encrypted string
        """
        return hex(self.encode_decimal(string))

    def encode(self, string):
        """
            returns list of ints from string to encode
            @param string is string to encode 
            @return encode list
        """
        step, encode= 4, []
        for i in range(0, len(string), 4):
            encode.append(self.encode_decimal(string[i:step]))
            step += 4
        return encode
    
    def decode(self, decimal_array):
        """
            returns decoded string from endoced list
            @param decimal_array list of ints
            @return decoded string
        """
        decoded = ""
        for x in decimal_array:
            decoded += self.decode_decimal(x)
        return decoded.rstrip("\x00")

    def decode_decimal(self, decimal):
        """
            gets encoded number and returns decoded string
            @param decimal int
            @return string
        """
        decimal = bin(decimal)[2:].zfill(32)
        red, purple, green, blue = self.__cycle_through_binary(decimal)
        return self.__put_together_decode(red, purple,green,blue)
    
    def cli_decode(self, args):
        """
            prints decoded string from ints
            @param args list
        """
        numbs = args
        try:
            numbs = [int(i) for i in numbs]
        except:
            print( ("All args for decode must be "
                "numbers ex. 267487694, 125043731"))
            return
        print(encoder.decode(numbs))

    def cli_encode(self, args):
        """
            prints list of ints from string to encode
            @param list of int
        """
        print(encoder.encode(" ".join(args)))
  
    def __cycle_through_binary(self, decimal):
        """
            loops through endcoded string 
            @param decimal string
            @return list of chars
        """
        blue, green, purple, red = "", "", "", "" 
        for x in range(len(decimal)):
            blue, green, purple, red = self.__place_decode_index(
                    x, decimal, blue, green, purple, red)
        return red, purple, green, blue
    
    def __place_decode_index(
            self, x, decimal, blue, green, purple, red):
        """
            takes binary and seperates into buckets
            @param x int
            @param decimal string
            @param blue string
            @param green string
            @param purple string
            @param red string
            @retun list of strings
        """
        if x%4 == 0: blue += decimal[x]
        elif x%4 == 1: green += decimal[x]
        elif x%4 == 2: purple += decimal[x]
        elif x%4 == 3: red += decimal[x]
        return blue, green, purple, red
     
    def __put_together_decode(self, red, purple, green, blue):
        """
            creates 4 letter char from char int
            @param red char
            @param purple char
            @param green char 
            @param blue char 
            @return a decoded string
        """
        return self.__int_to_char(red) \
                + self.__int_to_char(purple)  \
                +  self.__int_to_char(green)  \
                + self.__int_to_char(blue) 
        
    def __int_to_char( self, color):
        """
        converts char int to ascii char
        @param color is char of int 
        returns char
        """
        return chr( int(color, 2))

    # private
    def __encrypt(self, string):
        """
        gives encryption string
        @param string is a string
        @return a encrypted string value 
        """
        sections = self.__get_sections(string)
        return self.__cycle_through_to_encrypt( sections)
    
    def __get_sections(self, string):
        """
        generates json object with initial string in 4 sections
        @param string is a string
        @return json object of string seperated in 4 sections 
            each section has been transformed from char to int
        """
        blue = self.__get_char_to_int(string, 0)
        green = self.__get_char_to_int(string, 1)
        purple = self.__get_char_to_int(string, 2)
        red = self.__get_char_to_int(string, 3)

        return {"red":red, "purple": purple, "green":green, "blue":blue}

    def __get_char_to_int(self, string, index ):
        """
            returns int from char 
            @param string is string
            @param index is int
            @return 0 or int value of char   
        """
        return ord(string[index]) if len(string) > index  else 0

    def __cycle_through_to_encrypt(self, sections):
        """
            encrypts with json sections
            @param sections is json object
            @return encrypted string 
        """
        output, xor, hold  = "", 1, None
        for y in range(4): 
            output, xor = self.__alternate_section(
                    hold, output, xor, sections)
        return str(output[::-1])
    
    def __alternate_section( self, hold, output, xor, sections):
        """
            encrypts sections 
            @param hold is a string
            @param output is string
            @param xor is int
            @param settions is json object
            @return string encypted char by car in reverse order and
                bitwise shift amount
        """
        for x in range(2):
            output, xor = self.__section_by_section( 
                    hold, output, sections, xor)
        return output, xor        
    
    def __section_by_section( self, hold, output, sections, xor):
        """
            encryptios section by section
            @param hold string
            @param output string
            @param sections json object
            @param xor int
            @return string encypted char by car in reverse order and
                bitwise shift amount
        """
        for section in ['blue', 'green', 'purple', 'red']:
            output = self.__add_next_digit( 
                    hold, output, sections[section], xor)
        xor = xor << 1
        return output, xor

    def __add_next_digit(self, digit, output, section, xor):
        """
            gives biniary value
            @param digit is string can be converted to int 
            @param output is string
            @param section is int
            @param xor is int
            @return 1 or 0 digit to be added to revered encryption string
        """
        digit = section & xor
        if (int(digit) > 0): output += "1"
        else:  output += "0"
        return output

if __name__ == "__main__":
    encoder = Encoding()
    if sys.argv[1] == "e" or sys.argv[1] == "E":
        encoder.cli_encode(sys.argv[2:])
    else:
        encoder.cli_decode(sys.argv[2:])
