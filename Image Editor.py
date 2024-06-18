import numpy as np
from matplotlib import pyplot as plt

def crop(image, dist1, dist2, dist3, dist4):
        img = plt.imread(image)
        r,c,ch=img.shape
        if r-dist3<=dist1 or c-dist2<=dist4:
                print("Cropping can not be performed for this value")
        else:
                cropped = img[dist1:r-dist3,dist4:c-dist2]
                plt.imshow(cropped)
                plt.show()

def rotate(image, direction, angle):
        img = plt.imread(image)
        r,c,ch=img.shape
        mid_coords = np.floor(0.5*np.array(img.shape))
        mid_coords[2]=ch
        rotated_img = np.zeros((r, c,3))
        if direction=='anticlockwise':
                cos = np.cos(np.deg2rad(angle))
                sin = np.sin(np.deg2rad(angle))
                for i in range(r):
                        for j in range(c):
                                x = int(mid_coords[0] + ((i - mid_coords[0]) * cos) - ((j - mid_coords[1]) * sin))
                                y = int(mid_coords[1] + ((j - mid_coords[1]) * cos) + ((i - mid_coords[0]) * sin))
                                if 0<=x<r and 0<=y<c:
                                        rotated_img[x][y] = img[i][j]
                plt.imshow(rotated_img.astype(np.uint8))
                plt.show()
        elif direction=='clockwise':
                cos = np.cos(np.deg2rad(-angle))
                sin = np.sin(np.deg2rad(-angle))
                for i in range(r):
                        for j in range(c):
                                x = int(mid_coords[0] + ((i - mid_coords[0]) * cos) - ((j - mid_coords[1]) * sin))
                                y = int(mid_coords[1] + ((j - mid_coords[1]) * cos) + ((i - mid_coords[0]) * sin))
                                if 0<=x<r and 0<=y<c:
                                        rotated_img[x,y] = img[i,j]
                plt.imshow(rotated_img.astype(np.uint8))
                plt.show()
        else:
                print("Invalid direction")

def blending(image1,image2, weight1,weight2,gamma):
        img1 = plt.imread(image1)
        img2 = plt.imread(image2)
        r1, c1, ch1 = img1.shape
        r2, c2, ch2 = img2.shape
        if r2<r1 :
                img1=np.resize(img1,(r2,c1,ch1))
        else:
                img2=np.resize(img2,(r1,c2,ch2))
        r1, c1, ch1 = img1.shape
        r2, c2, ch2 = img2.shape      
        if c2<c1 :
                img1=np.resize(img1,(r1,c2,ch1))
        else:
                img2=np.resize(img2,(r2,c1,ch2))
        blend = img1 * weight1 + img2 * weight2 + gamma
        plt.imshow(blend.astype(np.uint8))
        plt.show()

def bright_manipulate(image, percent_brightness):
        img = plt.imread(image)
        r,c,ch=img.shape
        value=percent_brightness/100
        if value>0:
                img[img > 255 - (value*img)] = 255
                img[img <= 255 - (value*img)] = img[img <= 255 - (value*img)] + value*img[img <= 255 - (value*img)]
        else:
                img[img+(value*img) < 0] = 0
                img[img+(value*img) >= 0] = img[img+(value*img) >= 0] + value*img[img+(value*img) >= 0]
        plt.imshow(img)
        plt.show()

c='y'
while c=='y' or c=='Y':
        print("\nMenu:")
        print("1. Crop image")
        print("2. Blend two images")
        print("3. Adjust Brightness")
        print("4. Rotate image by an angle in clockwise/anticlockwise")
        ch=int(input("Enter choice number: "))
        if ch==1:
                image=input("Enter absolute path of image: ")
                dist1=int(input("Enter distance from left: "))
                dist3=int(input("Enter distance from right: "))
                dist4=int(input("Enter distance from top: "))
                dist2=int(input("Enter distance from bottom: "))
                crop(image, dist1, dist2, dist3, dist4)
        elif ch==2:
                image1=input("Enter absolute path of image-1: ")
                image2=input("Enter absolute path of image-2: ")
                weight1=float(input("Enter weight of image-1: "))
                while weight1>1:
                        weight1=float(input("Weight can't be >1. Enter another value: "))
                weight2=1-weight1
                gamma=float(input("Enter gamma value: "))
                blending(image1,image2, weight1,weight2, gamma)
        elif ch==3:
                image=input("Enter absolute path of image: ")
                percent_brightness=int(input("Enter brightness% to be adjusted: "))
                bright_manipulate(image, percent_brightness)
        elif ch==4:
                image=input("Enter absolute path of image: ")
                direction=input("Enter clockwise or anticlockwise: ")
                angle=int(input("Enter angle to rotate in degrees: "))
                rotate(image, direction, angle)
        else:
                print("Invalid input")
        c=input("Enter y or Y if you want to perform more functions: ")
