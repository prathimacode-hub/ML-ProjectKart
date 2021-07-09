**Mall Customers Segmentation**

**Goal**: This model will segment the customers based on the parameters.

**DATASET**: I have used Mall Customers dataset available on Kaggle.

**WHAT I HAD DONE**:

- Firstly I explored the data in different aspects.
- Then with the help of visualization libraries such as matplotlib and seaborn identified the group of customers.
- With help of that I visualized their pattern of spending.
- Based on this info , applied algorithms.
- And obtained the optimal number of clusters.

**MODELS USED**: I have used following algorithms.

- KMeans 
- Birch
- AffinityPropagation
- SpectralClustering

Out of this four algorithms the best result were displayed by the Birch and KMeans Clustering algorithms.

**LIBRARIES NEEDED**: 

- Pandas
- Numpy
- Matlplotlib
- Seaborn
- sklearn

**CONCLUSION**: Optimal number of clusters for this dataset would be 5.

a. High Income, High Spending Score (Cluster 5) - Target these customers by sending new product alerts which would lead to increase in the revenue collected by the mall as they are loyal customers.

b. High Income, Low Spending Score (Cluster 3) - Target these customers by asking the feedback and advertising the product in a better way to convert them into Cluster 5 customers.

c. Average Income, Average Spending Score (Cluster 2) - Can target these set of customers by providing them with Low cost EMI's etc.

d. Low Income, High Spending Score (Cluster 1) - May or may not target these group of customers based on the policy of the mall.

e. Low Income, Low Spending Score (Cluster 4) - Don't target these customers since they have less income and need to save money.
