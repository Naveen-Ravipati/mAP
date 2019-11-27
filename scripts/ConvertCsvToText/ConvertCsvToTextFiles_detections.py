import numpy as np


def CsvToText(filename):
    labels_dictionary = {0:'vehicles', 1:'pedestrians'}
    f = open(filename, 'r')
    for line in f:
        image = line.split(';')
        TextFile_Name = image[0][:-4]
        detections_list = image[1].split(' ')
        detections_list = detections_list[:-1]
        # print(detections_list)
        TextFile = open('validation\detection-results\\'+TextFile_Name + '.txt','w')
        for detection in detections_list:
            detection_list = detection.split(',')
            # print(detection_list)
            TextFile.write(labels_dictionary[int(detection_list[5][0])] + ' ')
            TextFile.write(detection_list[4] + ' ')
            dimensions = ' '.join(detection_list[:4])  
            TextFile.write(dimensions)
            TextFile.write('\n')
        TextFile.close()
    f.close()
    return


filename = 'detections_kitti_waymo_testset.csv'
result = CsvToText(filename)