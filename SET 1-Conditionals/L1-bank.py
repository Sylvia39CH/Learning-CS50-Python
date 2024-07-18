s = str(input("Greet to me: ")).strip().lower()

if "hello" in s:
    e = 0
elif "h" in s:
    e = 20
else:
    e = 100

print(f"Bonus: ${e}")