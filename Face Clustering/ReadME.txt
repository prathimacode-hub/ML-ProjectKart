Face recognition and face clustering are different, but highly related concepts. When performing face recognition we are applying supervised learning where we have both (1) example images of faces we want to recognize along with (2) the names that correspond to each face (i.e., the “class labels”).
But in face clustering we need to perform unsupervised learning — we have only the faces themselves with no names/labels. From there we need to identify and count the number of unique people in a dataset.

Face clustering is the task of grouping unlabeled face images according to individual identities. Several applications require this type of clustering, for instance, social media, law enforcement, and surveillance applications. In this paper, we propose an effective graph-based method for clustering faces in the wild. The proposed algorithm does not require prior knowledge of the data. This fact increases the pertinence of the proposed method near to market solutions. The experiments conducted on four well-known datasets showed that our proposal achieves state-of-the-art results, regarding the clustering performance, also showing stability for different values of the input parameter. Moreover, in these experiments, it is shown that our proposal discovers a number of identities closer to the real number existing in the data.
* One to extract and quantify the faces in a dataset
* Another to cluster the faces, where each resulting cluster (ideally) represents a unique individual


Configuring your development environment : 

As a quick breakdown, here is everything you’ll need in your Python environment:

* OpenCV
* dlib
* imutils
* scikit-learn


Our project has:

* encode_faces.py : This is our first script — it computes face embeddings for all faces in the dataset and outputs a serialized encodings file.
* encodings.pickle : Our face embeddings serialized pickle file.
* cluster_faces.py : The magic happens in this script where we’ll cluster similar faces and ideally find the outliers.


To run :
 ``` $ python cluster_faces.py --encodings encodings.pickle ```

Result :

Here are the face clusters generated from our 128-d facial embeddings and the DBSCAN clustering algorithm on our dataset:

