
## Prerequisites

You need to install:
- [Python](https://www.python.org/downloads/)

Optional:
- **plot** the results by [installing Matplotlib](https://matplotlib.org/users/installing.html) - Linux, macOS and Windows:
    1. `python -mpip install -U pip`  
    2.  `python -mpip install -U matplotlib`
-  show **animation** by installing [OpenCV](https://www.opencv.org/):
    1. `python -mpip install -U pip`
    2. `python -mpip install -U opencv-python`  


## Running the code

Step by step:
  1. Convert the ground truth in the csv file to the multiple text files (One file per image). Script is available in the **scripts/ConvertCsvToText/**
  2. Copy the ground-truth files into the folder **input/ground-truth/**
  3. Convert the detections in the csv file to the multiple text files (One file per image). Script is available in the **scripts/ConvertCsvToText/**
  4. Copy the detection-results files into the folder **input/detection-results/**
  5. Run the code:
         ```
         python main.py
         ```
  6. Sample analysis file is created (in **mAP/analysis.py**) to have a check of True positive count per image. This leads us to insights about the trained model.

#### Create the ground-truth files

- Create a separate ground-truth text file for each image.
- Use **matching names** for the files (e.g. image: "waymo_validation_front_251.jpg", ground-truth: "waymo_validation_front_251.txt").
- In these files, each line should be in the following format:
    ```
    <class_name> <left> <top> <right> <bottom> [<difficult>]
    ```
    ```
    vehicles 671.6959649999999 671.38017 864.330915 733.27599
    vehicles 625.2741000000001 674.222325 713.6967 717.8020349999999
    vehicles 1588.7646449999997 674.222325 1722.0301349999995 722.8547550000001
    vehicles 1856.558805 649.5903149999999 1869.822195 662.853705
    vehicles 689.6962799999999 675.485505 756.6448199999998 697.591155
    vehicles 1686.3453 683.3803800000001 1835.4005399999996 745.2762
    vehicles 600.0105 673.590735 656.8536 686.8541250000001
    vehicles 987.490965 661.27473 1120.7564550000002 719.38101
    vehicles 913.91073 674.222325 999.80697 722.8547550000001
    ```

#### Create the detection-results files

- Create a separate detection-results text file for each image.
- Use **matching names** for the files (e.g. image: "waymo_validation_front_251.jpg", detection-results: "waymo_validation_front_251.txt").
- In these files, each line should be in the following format:
    ```
    <class_name> <confidence> <left> <top> <right> <bottom>
    ```
- E.g. "image_1.txt":
    ```
    vehicles 0.47375885 907 665 997 723
    vehicles 0.6970133 976 659 1118 728
    ```
