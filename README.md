# Transportation Classification
## Description
## Objectives
## Features
## Project Structure
## Installation

1. Installation
    ```
       
    ```
3. Create Virtual Envirotment (Optional)
4. Install Dependencies
5. Configure Kaggle API
6. Run the Notebook
## Model Architecture
## Result
After training and testing process, the model achieved the following performance:

### Training Process

|          Metric             |      Value     |
|-----------------------------|----------------|
| Final Training Loss         |     0.0281     |
| Final Training Accuracy     |     0.9898     |
| Final Validation Loss       |     0.0082     |
| Final Validation Accuracy   |     0.9979     |

### Model Evaluation

|   Dataset    |  Accuracy  |    Loss   |
|--------------|------------|-----------|
| Training Set |   0.9951   |   0.0142  |
| Test Set     |   0.9944   |   0.0174  |

### Classification Report

|     Class     |     Precision     |     Recall     |     F1-Score     |
|---------------|-------------------|----------------|------------------|
| non-vehicles  |       0.99        |     1.00       |      0.99        |
| vehicles      |       1.00        |     0.99       |      0.99        |

### Test Model

|     Class    | Correct | Wrong | Accuracy |
|--------------|---------|-------|----------|
|     All      |   33    |   7   |  82.50%  |
| non-vehicles |   17    |   3   |  85.00%  |
|  vehicles    |   16    |   4   |  80.00%  |

### Metric Visualization
Below is a visualizatiion of the result:

1. Accuracy Plot

   <img src="https://raw.githubusercontent.com/Junazidomi/Transportation-Classification/refs/heads/main/Output/Accuracy%20Graph.png" width="350"/>
   
2. Loss Plot

   <img src="https://raw.githubusercontent.com/Junazidomi/Transportation-Classification/refs/heads/main/Output/Loss%20Graph.png" width="350"/>
   
3. Confusion Matrix

   <img src="https://raw.githubusercontent.com/Junazidomi/Transportation-Classification/refs/heads/main/Output/Confusion%20Matrix.png" width="350"/>
   
## Evaluation
