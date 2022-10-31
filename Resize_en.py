import PIL
from PIL import Image
import os
import warnings
import time

C = input("Path to the folder where images to compress/resize are. /!\ THIS FOLDER MUSN'T CONTAIN ANY OTHER FOLDER /!\  Path =  ")
C2 = input("Path to the destination folder for the compressed/resized images. /!\ WARNING /!\ If the original and destination folders are the same, original images will be deleted. Path to the destination folder  :  ")
k = input("Resize ratio ? A ratio of 1.0 allows a compression of the images' weight by about 80% thanks to the LANCZOS resampling, without any resizing nor visible loss of quality. Ratio  =  ")

start = time.time() #counts time like Simple Plan et Marie-Mai in the french version of Jet Lag

k = float(k)
C = str(C)
Cs = "/" 
C = C + Cs #adds a slash at the end of the original and destination paths
C1 = str(C)
C2 = str(C2)
C2 = C2 + Cs
C3 = str(C2)
Pm = 0 #futur average loss in weight of the images
M3 = 0 #futur total final weight size

image_list = os.listdir(C) #creates a list with all the names of the folder's files

N = len(image_list)

print ("\n" "\n" "\n", N, " images have been selected" "\n" "\n" "\n")

i = 0
while i < N :
    C = C + str(image_list[i]) #complete path of the i-th image
    C2 = C2 + str(image_list[i]) #futur complete path of the i-th downscaled/compressed image
    new_image=Image.open(C) #takes the original image and looks at it in the eyes
    M1 = os.path.getsize(C) #weights its weight
    l, h = new_image.size
    l = int(k*l) #new width
    h = int(k*h) #new height
    with warnings.catch_warnings():  #hides the popping warning when the image is too big
        warnings.simplefilter('ignore') #ignores the useless warning
        new_image = new_image.resize((l,h), resample=Image.LANCZOS) #RESIZING BITCH
        new_image.save(C2) #saves the new image
    M2 = os.path.getsize(C2) #weight of the downscaled image
    M = float(M2/M1) #ratio of the before/after weights 
    M = 100 * M #puts the ratio in %
    PT = 100 - int(M) #gives the loss percentage
    Pm = Pm + PT #sums the percentages to do the average loss next
    M3 = M3 + M2 #sums the new weights to give the destination folder's final weight
    print("Processing of the : ",i+1,"-th image done")
    C = C1 #resets the original folder's path
    C2 = C3 #same for the destination folder
    i = i+1 #next image !
    
Pm = Pm/N #average loss/gain of weight
M3 = float(M3/1000000) #converts the images' weight, until now in bytes, in Megabytes

end = time.time() #stops counting time

print ("\n" "The weight of the images has been reduces by ",int(Pm),"% in average.")
print ("\n" "Total final weight = about", int(M3), " Mo.")
print ("\n" "Time spent : ", int(end - start)," seconds.")
print ("\n" "Good job, computer !")

### MADE BY CREDOS97 ###

