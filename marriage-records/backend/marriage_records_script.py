from ultralytics import YOLO
import cv2
import numpy as np
from IPython.display import display, Image
from IPython import display
import yaml
import time
import shutil
import os

from roboflow import Roboflow
from IPython.display import display, clear_output
import subprocess

rf = Roboflow(api_key="9ubavwmtSsc3S8XChm2T")
project = rf.workspace("marrigerecordprocessing").project("mr-jfydd")
dataset = project.version(8).download("yolov8")

model = YOLO("best (4).pt")

def createTestModel(image_name):
    # Using with Python SDK
    img_src = image_name
    model.predict(img_src, project='predict', name="dataset", exist_ok=True, save=True, save_txt=True)

    clear_output()
    
    # Using with CLI
    subprocess.run(['yolo', 'task=detect', 'mode=predict', 'model=yolov8s.pt', 'conf=0.25', f'source={image_name}', 'save=True'])


test_image_folder = "test_image_folder/"
imagePath = []

for filename in os.listdir(test_image_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(test_image_folder, filename)
        imagePath.append(image_path)
        print(f"Image path: {image_path}")  # Print the image paths
        createTestModel(image_path)

# Extraction of the bounding boxes
def cropImage(j, crop_name, img, top_left, bottom_right):
    # Cropping an image
    img_crop = img[top_left[j][1]:bottom_right[j][1], top_left[j][0]:bottom_right[j][0]]

    # Ensure the output folder exists
    if not os.path.exists("croppedImages"):
        os.makedirs("croppedImages")

    error_image = cv2.imread("error_handle_pic.jpg")

    if img_crop.any() == False:
      cv2.imwrite(os.path.join("croppedImages", crop_name), error_image)
    else:
      # Save the cropped image to the specified folder
      cv2.imwrite(os.path.join("croppedImages", crop_name), img_crop)

def makeBox(name, j, color, lines, top_left, bottom_right, img):
  #print(name, j)
  index = int(lines[j].split()[0])
  img_d = cv2.rectangle(img, top_left[j], bottom_right[j], color,2)

def extractBox(number, name, j, color, lines, top_left, bottom_right, img, crop_name):
  if (name == number): # making boxes for milleottocentosettanta
    makeBox(name,j, color,lines, top_left, bottom_right, img)
    cropImage(j,crop_name, img, top_left, bottom_right)

def title_extract_to_file(number):
  title_file = [file for file in os.listdir("titles_folder") if file.lower().endswith('.jpg')]
  image_files = sorted(image_files)




def hconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    # Resize images to have the same height (assumes images have the same width)
    img_list_resized = [cv2.resize(img, (img_list[0].shape[1], img_list[0].shape[0]), interpolation=interpolation)
                        for img in img_list]

    # Concatenate images horizontally
    return cv2.hconcat(img_list_resized)

def h_concatenate_and_save():
    # Get a list of image files in the input folder
    image_files = [file for file in os.listdir("croppedImages") if file.lower().endswith('.jpg')]
    image_files = sorted(image_files)

    # Read images from the folder
    images = [cv2.imread(os.path.join("croppedImages", img)) for img in image_files]


    # Horizontally concatenate all the images
    img_out_put = hconcat_resize(images)

    # Ensure the output folder exists
    output_folder = "hConcatImages"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate output file name based on current timestamp
    timestamp = int(time.time())
    output_file = f"concatenated_{timestamp}.jpg"  # Unique filename based on timestamp

    # Save the concatenated image to the output folder
    cv2.imwrite(os.path.join(output_folder, output_file), img_out_put)

def h_concatenate_and_save_for_titles():
    # Get a list of image files in the input folder
    image_files = [file for file in os.listdir("titles_folder") if file.lower().endswith('.jpg')]
    image_files = sorted(image_files)


    # Read images from the folder
    images = [cv2.imread(os.path.join("titles_folder", img)) for img in image_files]

    # Horizontally concatenate all the images
    img_out_put = hconcat_resize(images)

    # Ensure the output folder exists
    output_folder = "vConcatImages"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate output file name based on current timestamp
    timestamp = int(time.time())
    output_file = f"concatenated_{timestamp}.jpg"  # Unique filename based on timestamp

    # Save the concatenated image to the output folder
    cv2.imwrite(os.path.join(output_folder, output_file), img_out_put)

def vconcat_resize(img_list, interpolation = cv2.INTER_CUBIC):
    # take minimum width
    w_min = min(img.shape[1] for img in img_list)
    # resizing images
    im_list_resize = [cv2.resize(img,(w_min, int(img.shape[0] * w_min / img.shape[1])),interpolation = interpolation) for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)

def v_concatenate_and_save():
    # Get a list of image files in the input folder
    image_files = [file for file in os.listdir("hConcatImages") if file.lower().endswith('.jpg')]
    image_files = sorted(image_files)


    # Read images from the folder
    images = [cv2.imread(os.path.join("hConcatImages", img)) for img in image_files]

    # Horizontally concatenate all the images
    img_out_put = vconcat_resize(images)

    # Ensure the output folder exists
    output_folder = "vConcatImages"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate output file name based on current timestamp
    timestamp = int(time.time())
    output_file = f"v_concatenated_{timestamp}.jpg"  # Unique filename based on timestamp

    # Save the concatenated image to the output folder
    cv2.imwrite(os.path.join(output_folder, output_file), img_out_put)

def final_v_concatenate_and_save():
    # Get a list of image files in the input folder
    image_files = [file for file in os.listdir("vConcatImages") if file.lower().endswith('.jpg')]
    image_files = sorted(image_files)


    # Read images from the folder
    images = [cv2.imread(os.path.join("vConcatImages", img)) for img in image_files]

    # Horizontally concatenate all the images
    img_out_put = vconcat_resize(images)

    # Ensure the output folder exists
    output_folder = "finalvConcatImages"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate output file name based on current timestamp
    timestamp = int(time.time())
    output_file = f"v_concatenated_{timestamp}.jpg"  # Unique filename based on timestamp

    # Save the concatenated image to the output folder
    cv2.imwrite(os.path.join(output_folder, output_file), img_out_put)

  # Clear contents of hConcatImages folder
def clear_hconcat_images_folder():
    folder_path = "hConcatImages"

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Remove all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"'{folder_path}' folder does not exist.")

  # Clear contents of vConcatImages folder
def clear_vconcat_images_folder():
    folder_path = "vConcatImages"

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Remove all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"'{folder_path}' folder does not exist.")

def testModel(input_folder_images, input_folder_labels, output_folder):

    image_files = os.listdir(input_folder_images)
    image_files = sorted(image_files)

    label_files = os.listdir(input_folder_labels)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for img_file in image_files:
        img_name, img_ext = os.path.splitext(img_file)
        corresponding_label = next((label for label in label_files if label.startswith(img_name)), None)

        if corresponding_label:
            img_path = os.path.join(input_folder_images, img_file)
            label_path = os.path.join(input_folder_labels, corresponding_label)

             # Interpreting the results
            file_name = "datasets/MR-8/data.yaml"
            with open(file_name, "r") as stream:
              names = yaml.safe_load(stream)["names"]
            with open(label_path, "r") as label_file:
                lines = label_file.readlines()
            print(names); print(lines)

            top_left = [0]*len(lines)
            bottom_right = [0]*len(lines)

            temp_1 = [0]*len(lines)
            temp_2 = [0]*len(lines)

            lines.sort(key = lambda x: (x[1], x[2]))

            #Blue boxes for data
            for i in range(len(lines)):

              index = int(lines[i].split()[0])

              obj = lines[i].split()
              xc, yc, nw, nh = float(obj[1]), float(obj[2]), float(obj[3]), float(obj[4])
              # xc, yc are normalized center coordinates, nw and nh are normalized height and width

              img = cv2.imread(img_path)
              h, w = img.shape[0], img.shape[1]
              xc *= w; yc *= h; nw *= w; nh *= h

              # Grabing millocen,1,nato in,residente,2,nata in,residente, anni, di

              if (index == 11): # milleottocentosettanta bounding box
                top_left[i] = int(xc - nw/2+295), int(yc - nh/2-25); bottom_right[i] = int(xc + nw/2+200), int(yc + nh/2+10)

              if (index == 13): # nata in bounding box.
                top_left[i] = int(xc - nw/2+100), int(yc - nh/2-25); bottom_right[i] = int(xc + nw/2+300), int(yc + nh/2+10)

              if (index == 0): # 2 bounding box.
                top_left[i] = int(xc - nw/2+40), int(yc - nh/2-15); bottom_right[i] = int(xc + nw/2+625), int(yc + nh/2+15)

              if (index == 19): # residente bounding box
                temp_1[i] = int(xc - nw/2), int(yc - nh/2); temp_2[i] = int(xc + nw/2), int(yc + nh/2)
                #highest residente
                if((((600 < temp_2[i][0] and temp_2[i][0] < 725) and (700 < temp_2[i][1] and temp_2[i][1] < 880)))):
                  top_left[i] = int(xc - nw/2+180), int(yc - nh/2-25); bottom_right[i] = int(xc + nw/2+300), int(yc + nh/2+10)

                elif((((1500 < temp_2[i][0] and temp_2[i][0] < 2150) and (700 < temp_2[i][1] and temp_2[i][1] < 880)))):
                  top_left[i] = int(xc - nw/2+180), int(yc - nh/2-25); bottom_right[i] = int(xc + nw/2+300), int(yc + nh/2+10)

                # shifted residente.
                elif((((1220 < temp_2[i][0] and temp_2[i][0] < 1400) and (870 < temp_2[i][1] and temp_2[i][1] < 1125))) and temp_1[i][0] > 1000):
                  top_left[i] = int(xc - nw/2-1100), int(yc - nh/2+45); bottom_right[i] = int(xc + nw/2-950), int(yc + nh/2+80)

                elif((((2100 < temp_2[i][0] and temp_2[i][0] < 2300) and (870 < temp_2[i][1] and temp_2[i][1] < 1125))) and temp_1[i][0] > 1500):
                  top_left[i] = int(xc - nw/2-1100), int(yc - nh/2+45); bottom_right[i] = int(xc + nw/2-950), int(yc + nh/2+80)

                else:
                  top_left[i] = 0,0; bottom_right[i] = 0,0

              if (index == 7): # figlia d bounding box, this for right now is to grab residente.
                top_left[i] = int(xc - nw/2-300), int(yc - nh/2-15); bottom_right[i] = int(xc + nw/2-125), int(yc + nh/2+15)

              if (index == 8): # fidlio d bounding box, this for right now is to grab residente.
                top_left[i] = int(xc - nw/2-300), int(yc - nh/2-15); bottom_right[i] = int(xc + nw/2-125), int(yc + nh/2+15)

              if (index == 14): # nato in bounding box
                top_left[i] = int(xc - nw/2+100), int(yc - nh/2-25); bottom_right[i] = int(xc + nw/2+300), int(yc + nh/2+10)

              if (index == 9): # l bounding box
                top_left[i] = int(xc - nw/2+40), int(yc - nh/2-25); bottom_right[i] = int(xc + nw/2+550), int(yc + nh/2+15)

              if (index == 3): # addi bounding box
                top_left[i] = int(xc - nw/2+75), int(yc - nh/2-15); bottom_right[i] = int(xc + nw/2+200), int(yc + nh/2+15)


              if (index == 4): # anni bounding box
                temp_1[i] = int(xc - nw/2), int(yc - nh/2); temp_2[i] = int(xc + nw/2), int(yc + nh/2)

                # first anni
                if((((1000 < temp_2[i][0] and temp_2[i][0] < 2000) and (550 < temp_2[i][1] and temp_2[i][1] < 840)))):
                  top_left[i] = int(xc - nw/2+70), int(yc - nh/2-20); bottom_right[i] = int(xc + nw/2+210), int(yc + nh/2+10)

                elif((((600 < temp_2[i][0] and temp_2[i][0] < 950) and (550 < temp_2[i][1] and temp_2[i][1] < 840)))):
                  top_left[i] = int(xc - nw/2+70), int(yc - nh/2-20); bottom_right[i] = int(xc + nw/2+210), int(yc + nh/2+10)

                # second anni
                elif((((850 < temp_2[i][0] and temp_2[i][0] < 1300) and (800 < temp_2[i][1] and temp_2[i][1] < 1100)))):
                  top_left[i] = int(xc - nw/2+70), int(yc - nh/2-20); bottom_right[i] = int(xc + nw/2+210), int(yc + nh/2+10)

                elif((((50 < temp_2[i][0] and temp_2[i][0] < 500) and (800 < temp_2[i][1] and temp_2[i][1] < 1100)))):
                  top_left[i] = int(xc - nw/2+70), int(yc - nh/2-20); bottom_right[i] = int(xc + nw/2+210), int(yc + nh/2+10)

                # last two anni
                else:
                  top_left[i] = 0,0; bottom_right[i] = 0,0

           #Grabbing the first di
              if(index == 5):
                temp_1[i] = int(xc - nw/2), int(yc - nh/2); temp_2[i] = int(xc + nw/2), int(yc + nh/2)

                if((((2000 < temp_2[i][0] and temp_2[i][0] < 3000) and (100 < temp_2[i][1] and temp_2[i][1] < 500)))):
                  top_left[i] = int(xc - nw/2+50), int(yc - nh/2-15); bottom_right[i] = int(xc + nw/2+200), int(yc + nh/2+15)

                elif((((1000 < temp_2[i][0] and temp_2[i][0] < 2500) and (100 < temp_2[i][1] and temp_2[i][1] < 500)))):
                  top_left[i] = int(xc - nw/2+50), int(yc - nh/2-15); bottom_right[i] = int(xc + nw/2+200), int(yc + nh/2+15)

                else:
                  top_left[i] = 0,0; bottom_right[i] = 0,0


            for j in range(len(lines)):
              name =lines[j].split()[0]

              # making boxes for milleottocentosettanta
              extractBox('11', name, j, (0,255,0), lines, top_left, bottom_right, img, "7_millo_year.jpg")

              # making boxes for nata in
              #extractBox('13', name, j, (255, 0, 127), lines, top_left, bottom_right, img, "13_HW.jpg")

              # making boxes for 2
              extractBox('0', name, j, (0, 0, 255), lines, top_left, bottom_right, img, "1_husband_name.jpg")

              # making boxes for residente
              #highest residente
              if (name == '19'):
                bottom_x = bottom_right[j][0]
                bottom_y = bottom_right[j][1]
                top_x = top_left[j][0]

                if((((975 < bottom_x and bottom_x < 1010) and (800 < bottom_y and bottom_y < 875)))):
                  extractBox('19', name, j, (255, 255, 0), lines, top_left, bottom_right, img, "3_husband_res.jpg")

                elif((((1800 < bottom_x and bottom_x < 2450) and (750 < bottom_y and bottom_y < 900)))and top_x >1500 and top_x<2150):
                  extractBox('19', name, j, (255, 255, 0), lines, top_left, bottom_right, img, "3_husband_res.jpg")

                # shifted residente.
                elif((((275 < bottom_x and bottom_x < 425) and (1000 < bottom_y and bottom_y < 1150))) and top_x < 100):
                  extractBox('19', name, j, (255, 255, 0), lines, top_left, bottom_right, img, "6_wife_res.jpg")

                elif((((1100 < bottom_x and bottom_x < 1350) and (1000 < bottom_y and bottom_y < 1150))) and top_x > 800):
                  extractBox('19', name, j, (255, 255, 0), lines, top_left, bottom_right, img, "6_wife_res.jpg")

              # making boxes for l
              extractBox('9', name, j, (0, 0, 255), lines, top_left, bottom_right, img, "4_wife_name.jpg")

              # making boxes for addi
              extractBox('3', name, j, (255, 0, 255), lines, top_left, bottom_right, img, "8_addi_.jpg")

              #highest anni
              if (name == '4'):
                bottom_x = bottom_right[j][0]
                bottom_y = bottom_right[j][1]
                top_x = top_left[j][0]

                if((((50 < bottom_x and bottom_x < 3000) and (400 < bottom_y and bottom_y < 900)))):
                  extractBox('4', name, j, (0, 200, 250), lines, top_left, bottom_right, img, "2_anni_husband_age.jpg")

                # second anni
                elif((((50 < bottom_x and bottom_x < 1500) and (900 < bottom_y and bottom_y < 2150)))):
                  extractBox('4', name, j, (0, 200, 250), lines, top_left, bottom_right, img, "5_anni_wife_age.jpg")

              #The first di
              if(name == '5'):
                bottom_x = bottom_right[j][0]
                bottom_y = bottom_right[j][1]
                top_x = top_left[j][0]

                if((((2000 < bottom_x and bottom_x < 3000) and (100 < bottom_y and bottom_y < 400)))):
                  extractBox('5', name, j,(165, 42, 42), lines, top_left, bottom_right, img, "9_di_month.jpg")




            # Generate the output file name based on the image file name or other criteria
            output_file = f"{img_name}_processed{img_ext}"  # Adjust as needed

            h_concatenate_and_save()


            # Save or do further processing with the result
            output_path = os.path.join(output_folder, output_file)
            # cv2.imwrite(output_path, processed_image)  # Save the processed image

# Clear the contents of hConcatImages folder before running the code
clear_hconcat_images_folder()
clear_vconcat_images_folder()
testModel("test_image_folder","predict/dataset/labels", "testModel_image")

v_concatenate_and_save()
h_concatenate_and_save_for_titles()
final_v_concatenate_and_save()
