import infer
from PIL import Image
import os

def main():
    image=Image.open("./images/image.jpg") 
    label = infer.predict(image)
    print("Inference Done!")
    print("Label = ", label)
       


if __name__ == '__main__':
    main()