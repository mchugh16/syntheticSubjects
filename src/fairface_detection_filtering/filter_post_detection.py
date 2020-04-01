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

    copy_detected_faces(detected_face_images, '../fairface-original', '../fairface-filtered')

    # check num images in destination folder
    images = os.listdir('../fairface-filtered')
    print(len(images))




if __name__ == '__main__':
    main()

