
### Dataset


The dataset used for training this model is sourced from https://www.kaggle.com/atulyakumar98/gundetection

It providing diverse instances for model training and validation.

- **Image Size:** 640x640 pixels
- **Batch Size:** 16

## Data Split

- **Train-Validation-Test Split:**
  - Training Data: 70%
  - Validation Data: 20%
  - Test Data: 10%

## Model Training Parameters

- **YOLO Version:** YOLOv5
- **Number of Classes:** 1 (Gun)
- **Training Epochs:** 30
- **Learning Rate:** 0.01
- **Optimizer:** AdamW
- **Loss Function:** YOLOv5 Loss

## Data Augmentation

- **Data Augmentation Techniques:**
  - Random Horizontal Flips
  - Random Vertical Flips
  - Random Rotation (±15 degrees)
  - Random Zoom (scale: 0.8 to 1.2)
  - Color Jittering
  - Blur upto 2.5px
  - Noise upto 0.14%
