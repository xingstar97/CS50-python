def main():
    text = input("Text: ")
    print(shorten(text))

def shorten(text):
    res = str()
    for i in range(len(text)):
        if text[i].lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            res += text[i]
    return res

if __name__ =="__main__":
    main()


# def shorten(text):
#     text=list(text)
#     for i in range(len(text)):
#         if text[i].lower() in ["a", "e", "i", "o", "u"]:
#             text[i]=''
#     return "".join(text)