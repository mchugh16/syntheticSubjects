
import cv2
import  os
import csv


def get_image_files(data_dir):
	files = os.listdir(data_dir)
	return files


# create an empty preidctions file with the proper headers 
# and empty strings in place of the predicted_label and predicted_prob
def create_predictions_file(annotations):
    with open(annotations,'r') as csvinput:
        with open("./fairface_annotations.csv", 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            reader = csv.reader(csvinput)
            

            all = []
            header = next(reader)
            header.append("face_detected")
            header.append("profile_detected")
            
            all.append(header)

            for row in reader:
                filename = row[0]
                face_detected = ""
                profile_detected = ""
                row.append(face_detected)
                row.append(profile_detected)
                all.append(row)

            writer.writerows(all)

# if not face is detected, returns ()
# if face is detected, returns coordinates of rect around face in form: [[ 16   2 189 189]]

def classify_and_record(data_dir, images, annotations_file, face_cascade):
    dict_predictions = {}
    for image in images:
        image_path = data_dir + image
        img = cv2.imread(image_path)
        # Convert into grayscale
        print("predicting image " + image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # profiles = profile_cascade.detectMultiScale(gray, 1.1, 4)
        filename = image
        dict_predictions[filename] = []
        if faces == ():
            dict_predictions[filename].append(False)
        else:
            dict_predictions[filename].append(True)
        print("Done predicting image " + image)
        # if profiles == ():
        #     dict_predictions[filename].append(False)
        # else:
        #     dict_predictions[filename].append(True)
    print(dict_predictions)
    write_to_csv(dict_predictions, annotations_file)

# take results of classifying 100 images (predictions_dict) and add to previous predicitons file
# write combined results to a new predictions file (labeled with the batch number)
def write_to_csv(dict_predictions, predictions_csv):
    output_file = "./detection_train_profiles.csv"
    with open(predictions_csv,'r') as csvinput:
        with open(output_file, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            header = next(reader)
            all.append(header)

            filenames = dict_predictions.keys()
            
            for row in reader:
                filename = row[0]
                if filename in filenames:
                    # face_detected = dict_predictions[filename][0]
                    profile_detected = dict_predictions[filename][0]
                    
                    # row[5] = face_detected
                    row[6] = profile_detected
                all.append(row)

            writer.writerows(all)

def merge_annotations():
    with open("./frontal_detections.csv",'r') as csv_input_frontals:
        with open("./profile_detections.csv",'r') as csv_input_profiles:
            with open("./fairface_annotations.csv", 'w') as csv_output:
                writer = csv.writer(csv_output)
                reader_frontals = csv.reader(csv_input_frontals)
                reader_profiles = csv.reader(csv_input_profiles)

                all = []
                header = next(reader_frontals)
                header_profiles = next(reader_profiles)
                all.append(header)

                for row_frontal in reader_frontals:
                    row_profile = next(reader_profiles)
                    filename_frontal = row_frontal[0]
                    filename_profile = row_profile[0]
                    if filename_frontal == filename_profile:
                        profile_detected = row_profile[6]
                        row_frontal[6] = profile_detected
                        all.append(row_frontal)

                writer.writerows(all)



def main():


    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

    # Read the input image
    # data_dir = '../data/'
    # images = get_image_files(data_dir)

    # Classify and record detections
    # classify_and_record(data_dir, images, "./fairface_annotations.csv", face_cascade)
    # classify_and_record(data_dir, images, "./fairface_annotations.csv", profile_cascade)

    merge_annotations()



if __name__ == '__main__':
    main()