import numpy as np


def CsvToText(filename):
    labels_dictionary = {0:'vehicles'}
    f = open(filename, 'r')
    for line in f:
        line_list = line.split(' ')
        # print(line_list)
        TextFile_Name = line_list[0][-10:-4]    
        # print(TextFile_Name)
        detections_list = line_list[1:]
        # print(detections_list)
        TextFile = open('validation\ground-truth\\'+ TextFile_Name + '.txt','w')
        for detection in detections_list:
            detection = detection.split(',')
            TextFile.write(labels_dictionary[int(detection[4][0])] + ' ')
            dimensions = ' '.join(detection[:4])
            TextFile.write(dimensions)
            TextFile.write('\n')
        TextFile.close()
    f.close()
    return


filename = 'lgsvl1_testset_1000.txt'
result = CsvToText(filename)