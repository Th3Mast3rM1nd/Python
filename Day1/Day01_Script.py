#!/usr/bin/env python3

#
name="mastermind"
print(f"Hello {name}")
print(f"{name.upper()}")
print(f"{name.lower()}")

name_2 = "the"
full_name = f"{name_2} {name}"
print(f"{full_name.title()}")

author_name = "Albert Einstein"
print(f"\t{author_name} once Said, \" A Person who never made a\n\tmistake never tried anything new" )

name_with_spaces = "    Mast3rM1nd"
name_with_spaces_1 = "Th3Mat3rM1nd        "
print(f"{name_with_spaces} {name_with_spaces_1}")

name_without_spaces = name_with_spaces.lstrip()
name_without_spaces_1 = name_with_spaces_1.rstrip()
print(f"{name_without_spaces} {name_without_spaces_1}")

number = 10_10_1000_00000
print(number)

