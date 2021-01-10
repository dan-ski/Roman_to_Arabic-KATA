class Roman_to_Arabic(object):

    def __init__(self):
        self.roman_number = ""

    def ask_about_number(self):
        self.roman_number= input("Proszę podaj liczbę rzymską: ")
        return self.roman_number

    def change_roman_to_arabic(self, roman_number):

        roman_arabic_dictionary = {"I": 1, "V": 5, "X": 10}
        roman_list= list(roman_number)
        for i in range(len(roman_list)):
            roman_list[i] = roman_arabic_dictionary[roman_list[i]]

        if len(roman_list) == 1:
            arabic_number = roman_list[0]
            return arabic_number
        else:
            arabic_number = roman_list[len(roman_list) - 1]
            i = 0
            while i < (len(roman_list)-1):

                if roman_list[i] < roman_list[i+1]:
                    arabic_number -= roman_list[i]

                else:
                    arabic_number += roman_list[i]
                    #import pdb; pdb.set_trace()
                i += 1

            return arabic_number



def main():
    roman_to_arabic = Roman_to_Arabic()
    