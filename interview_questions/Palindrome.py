input_text = str(input("Enter a string: ")).lower()
reversed_text = input_text[::-1]
if input_text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
