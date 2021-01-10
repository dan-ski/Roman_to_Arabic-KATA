from roman_to_arabic import Roman_to_Arabic


def main():
    roman_to_arabic = Roman_to_Arabic()
    roman_number = roman_to_arabic.ask_about_number()
    print(roman_to_arabic.change_roman_to_arabic(roman_number))

main()
