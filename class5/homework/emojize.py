import emoji

input1 = input("Input: ")
em = emoji.emojize(input1, language='alias')
print(f"Output: {em}")
