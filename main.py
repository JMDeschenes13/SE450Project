import binary2strings

with open("mal-p2.exe", "rb") as file:
    binary_data = file.read()

strings = binary2strings.extract_all_strings(binary_data)

for string in strings:
    print(string)