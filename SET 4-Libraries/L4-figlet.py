#（疑问）怎么看出来需要使用figlet、getFonts这些功能？
import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
figlet_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(figlet_fonts)
elif len(sys.argv) == 2:
    f = Figlet(font= sys.argv[1])
else:
    sys.exit()
    

text = input("Yout text: ")
print (f.renderText(text))