
import cv2
import  os
import csv


def get_gender_race_totals():
    with open("./fairface_annotations.csv",'r') as csv_input:
        with open("./fairface_stats.csv", 'w') as csv_output:
            reader = csv.reader(csv_input)

            fieldnames = ['gender_race', 'total', 'frontal_detected', 'profile_detected', 'both_detected']
            writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
            
            writer.writeheader()

            # initialize counts for race/gender subgroups

            white_m = {
                "gender_race":"white_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }
            white_f = {
                "gender_race":"white_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }
            black_m = {
                "gender_race":"black_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }
            black_f = {
                "gender_race":"black_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }
            mide_m = {
                "gender_race":"mide_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

            mide_f = {
                "gender_race":"mide_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

            indian_m = {
                "gender_race":"indian_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

            indian_f = {
                "gender_race":"indian_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }


            seasion_m = {
                "gender_race":"seasion_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

            
            seasion_f = {
                "gender_race":"seasion_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

        
            easion_m = {
                "gender_race":"easion_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

           
            easion_f = {
                "gender_race":"easion_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

           
            latino_m = {
                "gender_race":"latino_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

    
            latino_f = {
                "gender_race":"latino_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

           



            header = next(reader)


            for row in reader:
                gender = row[2]
                race = row[3]
                face_detected = (True if row[5] == 'True' else False)
                profile_detected = (True if row[6] == 'True' else False)

                if ((race == "White") and (gender == "Male")):
                    white_m["total"] += 1
                    if face_detected and profile_detected:
                        white_m["both_detected"] += 1
                    elif face_detected:
                        white_m["frontal_detected"] += 1
                    elif profile_detected:
                        white_m["profile_detected"] += 1
                elif ((race == "White") and (gender == "Female")):
                    white_f["total"] += 1
                    if face_detected and profile_detected:
                        white_f["both_detected"] += 1
                    elif face_detected:
                        white_f["frontal_detected"] += 1
                    elif profile_detected:
                        white_f["profile_detected"] += 1
                elif ((race == "Black") and (gender == "Male")):
                    black_m["total"] += 1
                    if face_detected and profile_detected:
                        black_m["both_detected"] += 1
                    elif face_detected:
                        black_m["frontal_detected"] += 1
                    elif profile_detected:
                        black_m["profile_detected"] += 1
                elif ((race == "Black") and (gender == "Female")):
                    black_f["total"] += 1
                    if face_detected and profile_detected:
                        black_f["both_detected"] += 1
                    elif face_detected:
                        black_f["frontal_detected"] += 1
                    elif profile_detected:
                        black_f["profile_detected"] += 1
                elif ((race == "Middle Eastern") and (gender == "Male")):
                    mide_m["total"] += 1
                    if face_detected and profile_detected:
                        mide_m["both_detected"] += 1
                    elif face_detected:
                        mide_m["frontal_detected"] += 1
                    elif profile_detected:
                        mide_m["profile_detected"] += 1
                elif ((race == "Middle Eastern") and (gender == "Female")):
                    mide_f["total"] += 1
                    if face_detected and profile_detected:
                        mide_f["both_detected"] += 1
                    elif face_detected:
                        mide_f["frontal_detected"] += 1
                    elif profile_detected:
                        mide_f["profile_detected"] += 1
                elif ((race == "Indian") and (gender == "Male")):
                    indian_m["total"] += 1
                    if face_detected and profile_detected:
                        indian_m["both_detected"] += 1
                    elif face_detected:
                        indian_m["frontal_detected"] += 1
                    elif profile_detected:
                        indian_m["profile_detected"] += 1
                elif ((race == "Indian") and (gender == "Female")):
                    indian_f["total"] += 1
                    if face_detected and profile_detected:
                        indian_f["both_detected"] += 1
                    elif face_detected:
                        indian_f["frontal_detected"] += 1
                    elif profile_detected:
                        indian_f["profile_detected"] += 1
                elif ((race == "Southeast Asian") and (gender == "Male")):
                    seasion_m["total"] += 1
                    if face_detected and profile_detected:
                        seasion_m["both_detected"] += 1
                    elif face_detected:
                        seasion_m["frontal_detected"] += 1
                    elif profile_detected:
                        seasion_m["profile_detected"] += 1
                elif ((race == "Southeast Asian") and (gender == "Female")):
                    seasion_f["total"] += 1
                    if face_detected and profile_detected:
                        seasion_f["both_detected"] += 1
                    elif face_detected:
                        seasion_f["frontal_detected"] += 1
                    elif profile_detected:
                        seasion_f["profile_detected"] += 1
                elif ((race == "East Asian") and (gender == "Male")):
                    easion_m["total"] += 1
                    if face_detected and profile_detected:
                        easion_m["both_detected"] += 1
                    elif face_detected:
                        easion_m["frontal_detected"] += 1
                    elif profile_detected:
                        easion_m["profile_detected"] += 1
                elif ((race == "East Asian") and (gender == "Female")):
                    easion_f["total"] += 1
                    if face_detected and profile_detected:
                        easion_f["both_detected"] += 1
                    elif face_detected:
                        easion_f["frontal_detected"] += 1
                    elif profile_detected:
                        easion_f["profile_detected"] += 1
                elif ((race == "Latino_Hispanic") and (gender == "Male")):
                    latino_m["total"] += 1
                    if face_detected and profile_detected:
                        latino_m["both_detected"] += 1
                    elif face_detected:
                        latino_m["frontal_detected"] += 1
                    elif profile_detected:
                        latino_m["profile_detected"] += 1
                elif ((race == "Latino_Hispanic") and (gender == "Female")):
                    latino_f["total"] += 1
                    if face_detected and profile_detected:
                        latino_f["both_detected"] += 1
                    elif face_detected:
                        latino_f["frontal_detected"] += 1
                    elif profile_detected:
                        latino_f["profile_detected"] += 1
            print(white_m)
            stats = {
                'white_m': white_m,
                'white_f': white_f,
                'black_m': black_m,
                'black_f': black_f,
                'mide_m': mide_m,
                'mide_f': mide_f,
                'indian_m':indian_m,
                'indian_f': indian_f,
                'seasion_m': seasion_m,
                'seasion_f': seasion_f,
                'easion_m': easion_m,
                'easion_f': easion_f,
                'latino_m': latino_m,
                'latino_f': latino_f
            }
            # print(stats)

            for stat, value in stats.items():
                writer.writerow(value)
        



def main():
    get_gender_race_totals()



if __name__ == '__main__':
    main()