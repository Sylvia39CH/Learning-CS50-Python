def main():
    word = input("Message: ")
    print(f"{shorten(word)}")

def shorten(word):
    t = list(str(word).lower())
    for i in range(len(t)):
        if t[i] in ["a","e","i","o","u"]:
            t[i] =  ""
        else:
            t[i] = t[i]
    return str(''.join(t))

if __name__ == "__main__":
    main()


