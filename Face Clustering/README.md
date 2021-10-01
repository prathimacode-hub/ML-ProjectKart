## Face Clustering :

Face recognition and face clustering are different, but highly related concepts. When performing face recognition we are applying supervised learning where we have both (1) example images of faces we want to recognize along with (2) the names that correspond to each face (i.e., the “class labels”).
But in face clustering we need to perform unsupervised learning — we have only the faces themselves with no names/labels. From there we need to identify and count the number of unique people in a dataset.

## Steps : 

* One to extract and quantify the faces in a dataset
* Another to cluster the faces, where each resulting cluster (ideally) represents a unique individual


## Configuring your development environment : 

As a quick breakdown, here is everything you’ll need in your Python environment:

* OpenCV
* dlib
* imutils
* scikit-learn


## Project has:

* encode_faces.py : This is our first script — it computes face embeddings for all faces in the dataset and outputs a serialized encodings file.
* encodings.pickle : Our face embeddings serialized pickle file.
* cluster_faces.py : The magic happens in this script where we’ll cluster similar faces and ideally find the outliers.


To run :
 ``` $ python cluster_faces.py --encodings encodings.pickle ```

## Result :

Here are the face clusters generated from our 128-d facial embeddings and the DBSCAN clustering algorithm on our dataset:
![Face ID #0](https://user-images.githubusercontent.com/65017645/135572088-d0f4376c-c60e-4edd-85aa-9655c68fd6ed.jpg)
![Face ID #1](https://user-images.githubusercontent.com/65017645/135572092-c3ea9382-aaf7-40ae-bd53-b831584f4954.jpg)
![Face ID #2](https://user-images.githubusercontent.com/65017645/135572094-432f8804-6f96-4270-bcf6-1e18aaf8ff4e.jpg)
![Face ID #3](https://user-images.githubusercontent.com/65017645/135572096-37a85ccf-4c76-45b0-871a-2775823d2193.jpg)
![Face ID #4](https://user-images.githubusercontent.com/65017645/135572099-46a44f2f-f135-4ff7-8105-7950c6a87502.jpg)


