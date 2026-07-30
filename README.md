# Transportation Classification
## Description
## Objectives
## Features
## Project Structure

The following is the project structure:

```
      Animal-Face-Recognition/
      │
      ├── API/
      │   └── kaggle.json
      │
      ├── Model/
      │   └── model.h5
      │
      ├── Output/
      │   ├── Accuracy Graph.png
      |   ├── Loss Graph.png
      │   ├── Confusion Matrix.png
      │   ├── Cat Prediction.png
      │
      ├── src/
      │   ├── data_loader.py
      │   ├── model.py
      │   ├── train.py
      │   └── prediction.py
      │
      ├── Test/
      │   ├── non-vehicles
      |   |   ├── non-vehicles (1).jpeg
      |   |   ├── non-vehicles (2).jpeg
      |   |   ├── ...
      |   |   └── non-vehicles (20)
      |   |   
      │   └── vehicles
      |       ├── vehicles (1).jpeg
      |       ├── vehicles (2).jpeg
      |       ├── ...
      |       └── vehicles (20)
      |
      ├── Notebook.ipynb
      └── requirements.txt
      └── README.md
```
## Installation

1. Installation
   
    ```
       git clone https://github.com/Junazidomi/Transportation-Classification.git
       cd Transportation-Classification
    ```
2. Create Virtual Envirotment (Optional)

   Windows

   ```
     python -m venv venv
     venv\Scripts\activate
       
   ```
   Linux/MacOs

   ```
     python3 -m venv venv
     source venv/bin/activate
   ```
3. Install Dependencies

   ```
     pip install -r requirements.txt
   ```
   
4. Configure Kaggle API

   Download the kaggle.json from your Kaggle Account, then save it to the following folder:

   ```
      API/
      └── kaggle.json
   ```
5. Run the Notebook

   Open `Notebook.ipynb` using Jupyter Notebook, JupyterLab, or Visual Studio Code, then run all cells sequentially.

   The notebook automatically:

   - Download the dataset from kaggle.
   - Preprocess and augment the data
   - Build and train the CNN model
   - Evaluate the trained model
## Model Architecture

The architecture model in this project is: 

```
        Input (64×64×3)
                │
                ▼
        Conv2D (32, 3×3)
                │
            MaxPool2D
                │
           Dropout (0.25)
                │
                ▼
        Conv2D (64, 3×3)
                │
             MaxPool2D
                │
          Dropout (0.25)
                │
                ▼
        Conv2D (128, 3×3)
                │
           MaxPool2D
                │
         Dropout (0.5)
                │
           Dropout (0.3)
                │
             Flatten
                │
           Dense (64)
                │
          Dropout (0.5)
                │
             Softmax

```
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
