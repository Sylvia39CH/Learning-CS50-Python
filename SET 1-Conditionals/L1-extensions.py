str1 =input("Input a suffix: ").lower()

str2 = "."

s = str1[str1.index(str2):]

suffixes = {
    ".gif": "Graphics Interchange Format (GIF)",
    ".jpg": "JPEG images",
    ".jpeg": "JPEG images",
    ".png": "Portable Network Graphics",
    ".txt": "Text, (generally ASCII or ISO 8859-n)",
    ".zip": "ZIP archive"
}

if s in suffixes:
    print(f"media type: {suffixes[s]}")
else:
    print("media type: application/octet-stream")

#注意：列表用[]表示（有一系列的值），词典用{}表示（二维的列表，意思是有一系列的key，并且每个key又有对应的值）