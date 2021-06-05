# Customer-Segmentation-Analysis
# Algorithm used: K Means Clustering

![images](https://user-images.githubusercontent.com/77589822/120663781-f5f52b80-c4a7-11eb-8640-459d60d5c2a5.jpg)



Customer segmentation is the process of dividing customers into groups based on common characteristics so that companies can market to each group effectively and appropriately. I have used the mall_customers dataset from Kaggle. It has some basic data like the Customer ID, age, gender, annual income and spending score, which is automatically assigned to the customer based on the defined parameters like customer behavior and purchasing data.

This dataset is composed by the following five features:

CustomerID: Unique ID assigned to the customer Gender: Gender of the customer Age: Age of the customer Annual Income: Annual Income of the customer Spending Score (1-100): Score assigned by the mall based on customer behavior and spending nature.

The Customer Segmentation has been done using K Means Clustering. K-means clustering is a method of vector quantization that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. To find the appropriate number of clusters, we use the elbow method which gives an approximately best fit value where the graph bends. If for the first observation, the number of clusters are not unique, then we need to again find the value of k using elbow method for the given parameters because k can differ for different parameters. Here, we get 5, 4 and 6 clusters respectively.

For the 5 cluster analysis where all the three parameters, age,annual income and spending score is taken into consideration, I have plotted a 3-D plot using pyplot library which provides excellent readability.


Article

I wrote an article on the same analysis, please find it [**here**](https://theanshul.medium.com/customer-segmentation-using-k-means-clustering-ffded3a2695).
