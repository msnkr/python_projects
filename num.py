import phonenumbers

test_num = "+2774758777"

x = phonenumbers.parse(test_num, "ZA")
print(phonenumbers.is_possible_number(x))
