# To get Pre-tracking segmentation metrics

We are interested in seeing the difference that tracking can make in our segmentation performance.  
Specifically, the KIT-Sch-GE tracking alogrithm does segmentation correction, which should hopefully increase our segmentation metic.  
So we need to get the metric first so we can compare.

### Naming Convention

Place pre-tracked results as HPx_PRETRA.  
For example:  
cp -rp /home/MinaHossain/DMNet_Rina_Tracking/data/06_RES-GT /home/MinaHossain/DMNet_Rina_Tracking/6row_images/HP1_PRETRA

### Evaluation

Since evaluation code only looks at a 0x_RES folder, we need to copy which ever data we want to evaluate into that folder.  
For example:  
rm -rf /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02_RES  
cp -rp /home/MinaHossain/DMNet_Rina_Tracking/6row_images/HP1_PRETRA /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02_RES  

Get the metrics:  

cd /home/MinaHossain/EvaluationSoftware/Linux  
 
For example:
./SEGMeasure /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4


# Get averaged center distance score
cd /home/MinaHossain/DMNet_Rina_Tracking  
python center_score.py /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4  






# Get Tracking Restults

This will run code after going through the 2021-cell-tracking README setup (i.e. getting gurobi working)

### Naming Convention

Save tracking results for a given set of hyperparameters as HPx_TRA

### Get Tracking

To generate tracking results, run:  

cd /home/MinaHossain/DMNet_Rina_Tracking/2021-cell-tracking  
conda activate venv_graph_tracking_kit_sch_ge_2021 

`python -m run_tracking --image_path IMAGE_PATH --segmentation_path SEGMENTATION_PATH --results_path RESULTS_PATH`  
For example: 
python -m run_tracking --image_path /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02 --segmentation_path /home/MinaHossain/DMNet_Rina_Tracking/data/06_RES-GT --results_path /home/MinaHossain/DMNet_Rina_Tracking/6row_images/HP1_TRA

### Evaluation

Remeber to copy the results you want to test into 02_RES

rm -rf /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02_RES   
cp -rp /home/MinaHossain/DMNet_Rina_Tracking/6row_images/HP1_TRA /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02_RES  
cd /home/MinaHossain/EvaluationSoftware/Linux  
./SEGMeasure /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4  
./TRAMeasure /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4  

cd /home/MinaHossain/DMNet_Rina_Tracking  
python center_score.py /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4  





# Get averaged center distance score

Pretty much the same process as before
cd /home/MinaHossain/DMNet_Rina_Tracking 

python center_score.py /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4

rm -rf /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02_RES   
cp -rp /home/MinaHossain/DMNet_Rina_Tracking/6row_images/HP1_TRA /home/MinaHossain/DMNet_Rina_Tracking/6row_images/02_RES  






# Hyperparameter Results

This is where we give descriptions for each different set of hyperparameters we tested, and their various metrics.

## HP1

Hyperparameters:  
* Scale = 0.6
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.285091
                Average Distance Score: 126.202320
                Average Count Difference: 4.957346 

* Post-Tracking SEG:  0.293515
* Post-Tracking TRA:  0.473306
                Average Score: 126.067462
                Average Count Difference: 6.398104

Notes:  



## HP2

Hyperparameters:  
* Scale = 0.8
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.190449
                Average Distance Score: 128.775603
                Average Count Difference: 2.620853

* Post-Tracking SEG:  0.190702
* Post-Tracking TRA:  0.348809
                Average Distance Score: 130.219933
                Average Count Difference: 4.004739



Notes:  


## HP3

Hyperparameters:  
* Scale = 0.4
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.149996
                Average Distance Score: 239.335159
                Average Count Difference: 22.763033

* Post-Tracking SEG:  0.157061
* Post-Tracking TRA:  0.177376
                Average Score: 238.460585
                Average Count Difference: 27.004739


Notes:


## HP4

Hyperparameters:  
* Scale = 1.0
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.211015
                Average Distance Score: 214.236262
                Average Count Difference: 83.720379

* Post-Tracking SEG:  0.204772
* Post-Tracking TRA:  0.197051
                Average Score:  214.546096
                Average Count Difference: 94.075829

Notes:



## HP5

Hyperparameters:  
* Scale = 0.7
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.039549
                Average Distance Score: 288.947484
                Average Count Difference: -25.658768

* Post-Tracking SEG:  0.045106
* Post-Tracking TRA:  0.325688
                Average Score: 280.427629
                Average Count Difference: -24.246445

Notes:



## HP6

Hyperparameters:  
* Scale = 0.5
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.171219
                Average Distance Score: 198.530347
                Average Count Difference: -5.123223

* Post-Tracking SEG:   0.176423
* Post-Tracking TRA:   0.333586
                Average Score: 200.096805
                Average Count Difference: -2.526066




## HP7

Hyperparameters:  
* Scale = 0.9
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.015757
                Average Distance Score: 277.629905
                Average Count Difference: -35.540284

* Post-Tracking SEG: 0.018235  
* Post-Tracking TRA: 0.294437   
                Average Score:  274.801086
                Average Count Difference: -35.042654


##################################### Hyperparameter Results for New Test Data Set ################# 

This is where we give descriptions for each different set of hyperparameters we tested, and their various metrics.

## HP1_N

Hyperparameters:  
* Scale = 0.6
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.375683
                Average Distance Score:  305.621359
                Average Count Difference: 19.901408

* Post-Tracking SEG: 0.381504  
* Post-Tracking TRA: 0.690886  
                Average Score: 307.858485
                Average Count Difference: 22.830986

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking



## HP2_N

Hyperparameters:  
* Scale = 0.8
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.281744 
                Average Distance Score:  329.841714
                Average Count Difference: 65.253521

* Post-Tracking SEG:  0.282195  
* Post-Tracking TRA:  0.380805 
                Average Score: 326.305749
                Average Count Difference: 76.394366 

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking






#####################################                       Hyperparameter Results for New Test Data Set                    ###################### 


######   "Cell-Data-P2": [6600, 0.99, 0.50],  # Area threshold, marker threshold, mask threshold 


## HP1_N_B(Test data set from newly labelled data)

Hyperparameters:  
* Scale = 0.6
* Everything else default

Metrics:  
* Pre-Tracking  SEG: 0.221587
                Average Distance Score:  367.884829
                Average Count Difference: 55.140000

* Post-Tracking SEG: 0.235539 
* Post-Tracking TRA: 0.271501
                Average Score:366.757321
                Average Count Difference: 63.200000

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking





This is where we give descriptions for each different set of hyperparameters we tested, and their various metrics.
"Cell-Data-P2": [6600, 0.99, 0.99],  # Area threshold, marker threshold, mask threshold 


## HP1_N_A(Test data set from Old labelled data)

Hyperparameters:  
* Scale = 0.6
* Everything else default

Metrics:  
* Pre-Tracking  SEG:  0.009511
                Average Distance Score:  675.829736
                Average Count Difference: 32.610000

* Post-Tracking SEG: 0.009631  
* Post-Tracking TRA: 0.000000  
                Average Score: 675.617132
                Average Count Difference: 36.210000

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking



## HP1_N_B(Test data set from newly labelled data)

Hyperparameters:  
* Scale = 0.6
* Everything else default

Metrics:  
* Pre-Tracking  SEG: 0.093740 
                Average Distance Score:  334.085236
                Average Count Difference: 18.320000

* Post-Tracking SEG:0.096998   
* Post-Tracking TRA: 0.055107 
                Average Score:324.774894 
                Average Count Difference: 20.810000

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking






#####################################                       Hyperparameter Results for New Test Data Set     July 07 - July 15               ###################### 


######   "Cell-Data-P2": [6600, 0.99, 0.50],  # Area threshold, marker threshold, mask threshold 


## HP1_N_A1(Test data set from newly labelled data)



Hyperparameters:  
* Scale = 0.6
* Area threshold, marker threshold, mask threshold = [6600, 0.99, 0.50]


Metrics:  
* Pre-Tracking  SEG: 0.409140 
                Average Distance Score:371.018940  
                Average Count Difference: 52.590000


* Post-Tracking SEG: 0.421954 
* Post-Tracking TRA: 0.524639  
                Average Score: 381.959826
                Average Count Difference: 59.000000

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking


## HP1_N_A2(Test data set from newly labelled data)



Hyperparameters:  
* Scale = 0.6
* Area threshold, marker threshold, mask threshold = [6600, 0.99, 0.75]


Metrics:  
* Pre-Tracking  SEG: 0.341717
                Average Distance Score: 366.403104
                Average Count Difference: 59.550000


* Post-Tracking SEG: 0.353441 
* Post-Tracking TRA:   0.275393 
                Average Score: 372.022390
                Average Count Difference:66.080000

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking




## HP1_N_A1(Test data set from newly labelled data)



Hyperparameters:  
* Scale = 0.6
* Area threshold, marker threshold, mask threshold = [6600, 0.99, 0.90]


Metrics:  
* Pre-Tracking  SEG: 0.178650 
                Average Distance Score: 300.758126 
                Average Count Difference: 21.400000


* Post-Tracking SEG: 0.179887 
* Post-Tracking TRA: 0.127069 
                Average Score: 309.441619
                Average Count Difference: 28.770000

Notes:  New Data set has improved accuracy in terms of Segmentation and Tracking
