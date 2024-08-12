import sys
import os
from PIL import Image, ImageOps


#通过两个命令行打开图片及保存图片，如果出现少于两个命令行，或者不是jpg/png图片，
#或者两个扩展名的拓展名不同，或者input的文件不存在，#则情况则退出：
def main():
    valid_formats = [".png",".jpg",".jpeg"]

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_format = os.path.splitext(sys.argv[1])[1]
    output_format = os.path.splitext(sys.argv[2])[1]

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        if input_format in valid_formats and output_format in valid_formats:
            if output_format == output_format:
                try:
                    image(input_file,output_file)
                except FileNotFoundError:
                    sys.exit("Input does not exist")                
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")



def image(input_file,output_file):
    #Open the input with Image.open
    photo = Image.open(input_file)
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    
    resized_photo = ImageOps.fit(photo, shirt_size) # resize crop the input with ImageOps.fit to match the png shirt image size
    resized_photo.paste(shirt, shirt) #overlay the shirt with Image.paste
    resized_photo.save(output_file)#save the result with Image.save

if __name__ == "__main__":
    main() 