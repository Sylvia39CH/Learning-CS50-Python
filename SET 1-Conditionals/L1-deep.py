s = input("the Answer to the Great Question of Life, the Universe and Everything:").strip().lower()
answer = ["42" ,"forty two","forty-two"]

if s in answer:
    print("Yes")
else:
    print("No")
    