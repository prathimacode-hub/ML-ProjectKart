# About the Dataset
Dataset can be downloaded from [here](https://www.kaggle.com/uciml/zoo-animal-classification?select=class.csv)


# Attribute Information: (name of attribute and type of value domain)

**zoo.csv**
    animal_name: Unique for each instance
    hair Boolean
    feathers Boolean
    eggs Boolean
    milk Boolean
    airborne Boolean
    aquatic Boolean
    predator Boolean
    toothed Boolean
    backbone Boolean
    breathes Boolean
    venomous Boolean
    fins Boolean
    legs Numeric (set of values: {0,2,4,5,6,8})
    tail Boolean
    domestic Boolean
    catsize Boolean
    class_type Numeric (integer values in range [1,7])

**class.csv**

This csv describes the dataset

    Class_Number Numeric (integer values in range [1,7])
    NumberOfAnimalSpeciesIn_Class Numeric
    Class_Type character -- The actual word description of the class
    Animal_Names character -- The list of the animals that fall in the category of the class
