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
        red = ord(string[len(string)-1]) if len(string) >3 else 0
        purple = ord(string[len(string)-2]) if len(string) > 2 else 0
        green = ord(string[len(string)-3]) if len(string) > 1 else 0
        blue = ord(string[0]) 
        return {"red":red, "purple": purple, "green":green, "blue":blue}
   
    def __cycle_through_to_encrypt(self, sections):
        """
            encrypts with json sections
            @param sections is json object
            @return encrypted string 
        """
        output, xor, hold  = "", 1, None
        for y in range(4): 
            output, xor = self.__alternate_section(hold, output, xor, sections)
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
            output, xor = self.__section_by_section( hold, output, sections, xor)
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
            output = self.__add_next_digit( hold, output, sections[section], xor)
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

