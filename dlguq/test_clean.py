from ctypes import *

# Load the shared object file
adder = CDLL('./filter.so')

# Try to load the function manually using the mangled name
try:
    check_keywords = getattr(adder, "_Z17CheckHaveKeywordsPKcS0_")
    check_keywords.argtypes = [c_char_p, c_char_p]
    check_keywords.restype = c_bool

    # Convert the strings to bytes using UTF-8 encoding
    result = check_keywords("헬1멧".encode('utf-8'), "./list.txt".encode('utf-8'))
    
    print(result)

except AttributeError as e:
    print(f"Error loading function: {e}")
