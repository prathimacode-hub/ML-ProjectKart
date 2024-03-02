# Butterfly-classification

butterfly identification and conservation have attracted a lot of attention from the scientific community and the general public. The large amount of image data available from online databases and citizen science platforms, and the need of cataloguing and monitoring the diversity and distribution of butterflies, pose significant research challenges. Hence, computer vision and machine learning are essential for enabling automated or semi-automated processing of big data in lepidoptery. Although butterflies are diverse enough to present unique challenges on their own, most of them share the need to identify distinctive features such as wing patterns, colours, and shapes. In this project, an innovative deep learning approach to the classification of the butterfly in different contexts is presented. The work exploits the potential of a convolutional neural network classifier to decide which species or family a butterfly belongs to, based on a single image, overcoming the typical issues that can occur dealing with classical approaches on large and heterogeneous datasets (e.g. occlusion, background clutter, and pose variation). Experiments on real data confirm the validity of the proposed approach that achieves 85% accuracy and suggest its implementation and integration at a larger scale in more complex vision systems

![Alt text](https://i.natgeofe.com/k/c491536c-f34d-4e64-ad27-8ee070dce475/monarch-butterfly-orange-flower.jpg?w=1084.125&h=609)
# Dataset
The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset :https://www.kaggle.com/bertcarremans/butterfly-images

# Goal
The goal of this project is to make a deep learning model which will classify the images of butterfly using three pre-trained models.
They are resnet,vgg,inception

# What have I done?
- Downloading the dataset form kaggle and unzipping it
- Data viswalization
- Made three Classification model with
     * Resnet50
     * VGG16
     * InceptionV3
- Observation:

| Models | Resnet50 | VGG16 | InceptionV3 |
| :---: | :---: | :---: | :---: |
| Accuracy with training data | 0.988 | 0.989 |0.757 |
| Accuracy with validating data | 0.758 | 0.723 | 0.608 |

- Conclusion:resnet and vgg are preforming well for tasks like this compared to inception net


# Library used 
- numpy
- Matplotlib
- Tensorflow
- keras
- os





