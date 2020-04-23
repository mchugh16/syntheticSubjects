
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


            seasian_m = {
                "gender_race":"seasian_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

            
            seasian_f = {
                "gender_race":"seasian_f",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

        
            easian_m = {
                "gender_race":"easian_m",
                "total": 0,
                "frontal_detected": 0,
                "profile_detected": 0,
                "both_detected":0
            }

           
            easian_f = {
                "gender_race":"easian_f",
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
                    seasian_m["total"] += 1
                    if face_detected and profile_detected:
                        seasian_m["both_detected"] += 1
                    elif face_detected:
                        seasian_m["frontal_detected"] += 1
                    elif profile_detected:
                        seasian_m["profile_detected"] += 1
                elif ((race == "Southeast Asian") and (gender == "Female")):
                    seasian_f["total"] += 1
                    if face_detected and profile_detected:
                        seasian_f["both_detected"] += 1
                    elif face_detected:
                        seasian_f["frontal_detected"] += 1
                    elif profile_detected:
                        seasian_f["profile_detected"] += 1
                elif ((race == "East Asian") and (gender == "Male")):
                    easian_m["total"] += 1
                    if face_detected and profile_detected:
                        easian_m["both_detected"] += 1
                    elif face_detected:
                        easian_m["frontal_detected"] += 1
                    elif profile_detected:
                        easian_m["profile_detected"] += 1
                elif ((race == "East Asian") and (gender == "Female")):
                    easian_f["total"] += 1
                    if face_detected and profile_detected:
                        easian_f["both_detected"] += 1
                    elif face_detected:
                        easian_f["frontal_detected"] += 1
                    elif profile_detected:
                        easian_f["profile_detected"] += 1
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
                'seasian_m': seasian_m,
                'seasian_f': seasian_f,
                'easian_m': easian_m,
                'easian_f': easian_f,
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