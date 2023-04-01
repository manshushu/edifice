input_str = input()
num = len(input_str)
searched = []
for i in range(num):
    for j in range(num):
        if str(input_str[j:j+i:]) not in searched:
            searched.append(str(input_str[j:j+i:]))
print(len(searched))