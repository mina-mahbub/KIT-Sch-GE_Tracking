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
`./SEGMeasure dir seq num_digist`  
For example:
./SEGMeasure /home/MinaHossain/DMNet_Rina_Tracking/6row_images 02 4







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







# Hyperparameter Results

This is where we give descriptions for each different set of hyperparameters we tested, and their various metrics.

## HP1

Hyperparameters:  
* Scale = .6
* Everything else default

Metrics:  
* Pre-Tracking  SEG: 0.285091
* Post-Tracking SEG: 0.293515
* Post-Tracking TRA: 0.473306

Notes:  

## HP2

Hyperparameters:  
* Scale = .8
* Everything else default

Metrics:  
* Pre-Tracking  SEG: 0.190449
* Post-Tracking SEG: 0.190702
* Post-Tracking TRA: 0.338809

Notes:  



## HP2

Hyperparameters:  
* Scale = .4
* Everything else default

Metrics:  
* Pre-Tracking  SEG: 0.149996
* Post-Tracking SEG: 0.157061
* Post-Tracking TRA: 0.177376

Notes: