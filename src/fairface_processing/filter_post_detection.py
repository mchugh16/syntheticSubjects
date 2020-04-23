import os, shutil, csv
from tkinter import filedialog
from tkinter import *

def copy_detected_faces(detected_face_images, source, destination):
    root = Tk()
    root.withdraw()

    for filename in os.listdir(source):
        if filename in detected_face_images:
            filename = source + '/' + filename
            shutil.copy(filename, destination)
        else:
            print("file does not exist: " + filename)

def split_by_race_gender(annotations, images):
    with open(annotations,'r') as csvinput:
        reader = csv.reader(csvinput)
        images_by_race_gender = {
            "Easian_f": [],
            "Easian_m": [],
            "SEasian_f": [],
            "SEasian_m": [],
            "black_m": [],
            "black_f": [],
            "indian_f": [],
            "indian_m": [],
            "latino_f": [],
            "latino_m": [],
            "midE_m": [],
            "midE_f": [],
            "white_m": [],
            "white_f": [],
        }

        header = next(reader)
    
        for row in reader:
            filename = row[0]
            if filename in images:
                race = row[3]
                gender = row[2]
                print("working on")
                if ((race == "White") and (gender == "Male")):
                    images_by_race_gender["white_m"].append(filename)

                elif ((race == "White") and (gender == "Female")):
                    images_by_race_gender["white_f"].append(filename)

                elif ((race == "Black") and (gender == "Male")):
                    images_by_race_gender["black_m"].append(filename)

                elif ((race == "Black") and (gender == "Female")):
                    images_by_race_gender["black_f"].append(filename)

                elif ((race == "Middle Eastern") and (gender == "Male")):
                    images_by_race_gender["midE_m"].append(filename)

                elif ((race == "Middle Eastern") and (gender == "Female")):
                    images_by_race_gender["midE_f"].append(filename)

                elif ((race == "Indian") and (gender == "Male")):
                    images_by_race_gender["indian_m"].append(filename)

                elif ((race == "Indian") and (gender == "Female")):
                    images_by_race_gender["indian_f"].append(filename)

                elif ((race == "Southeast Asian") and (gender == "Male")):
                    images_by_race_gender["SEasian_m"].append(filename)

                elif ((race == "Southeast Asian") and (gender == "Female")):
                    images_by_race_gender["SEasian_f"].append(filename)

                elif ((race == "East Asian") and (gender == "Male")):
                    images_by_race_gender["Easian_m"].append(filename)

                elif ((race == "East Asian") and (gender == "Female")):
                    images_by_race_gender["Easian_f"].append(filename)

                elif ((race == "Latino_Hispanic") and (gender == "Male")):
                    images_by_race_gender["latino_m"].append(filename)

                elif ((race == "Latino_Hispanic") and (gender == "Female")):
                    images_by_race_gender["latino_f"].append(filename)
            
        # check to see if images were categorized correctly
        for key, value in images_by_race_gender.items():
            print(key)
            print(len(value))

        return images_by_race_gender


def get_detected_faces(annotations):
    with open(annotations,'r') as csvinput:
        reader = csv.reader(csvinput)
        detected_face_images = []
        header = next(reader)
    
        for row in reader:
            filename = row[0]
            face_detected = (True if row[5] == 'True' else False)
            profile_detected = (True if row[6] == 'True' else False)
            if face_detected or profile_detected:
                detected_face_images.append(filename)

        return detected_face_images



def main():

    detected_face_images = get_detected_faces('./fairface_annotations.csv')
    print(len(detected_face_images)) # 51801

    # images_by_race_gender is a dict with folder (race/gender group) as keys, list of image names as values
    images_by_race_gender = split_by_race_gender('./fairface_annotations.csv', detected_face_images)

    for key, value in images_by_race_gender.items():
        print("Working on group: " + key)
        destination = '../../data/fairface-filtered/' + key
        copy_detected_faces(value, '../../data/fairface-original', destination)

    # check num images in destination folder
    print("DONE COPYING IMAGES")
    for key, value in images_by_race_gender.items():
        destination = '../../data/fairface-filtered/' + key
        print(key)
        images = os.listdir(destination)
        print(len(images))






if __name__ == '__main__':
    main()

