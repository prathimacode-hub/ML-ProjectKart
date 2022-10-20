# **MORTALITY RATE ANALYSIS AND PREDICITON**

<p align="center">
  <img width="600" height="325" src="https://zephyrnet.com/wp-content/uploads/2020/06/medtech-assessor-elektra-labs-is-offering-free-evaluations-of-covid-19-biosensors-to-doctors.gif">
</p>

* A mortality rate is the number of deaths due to a disease divided by the total population. If there are 25 lung cancer deaths in one year in a population of 30,000, then the mortality rate for that population is 83 per 100,000.

* We use mortality statistics to: produce population estimates and population projections, both national and subnational, produce life expectancy estimates, and quality assure census estimates.


## ❓ **WHAT IS MORTALITY RATE**

The mortality rate is the ratio of the number of deaths in the year to the average total population of the year.

The simplest mortality rate definition is the measure of the frequency of death in a specific population measured over a defined time period. 
It's usually expressed per 10n people. 
For instance, a mortality rate of 8.91 per 10,000 (n = 4) would mean that in every group of 10,000, approximately 8.91 people will have died over the specified time period.


## ❓ **WHAT ARE THE TYPES OF MORTALITY RATE**
There are several types of mortality rate, each providing us with different data and informing us of the risks associated with various states. The main ones are:

* Crude mortality rate - The most general type as it refers to all causes of death. Generally, it's used to compare the living conditions of certain periods or populations as it's been found that death rates decrease in developed countries. It also tells us what factors are especially crucial to our well-being.

* Specific death rates - These can be age, cause, race, or sex-specific. They provide more detailed data, allowing us to focus on reducing the impact of the most deadly factors, for instance, by producing vaccines. This is the case you consider when asking what is the mortality rate of the flu, for instance.
Infant, postneonatal, and neonatal mortality rates - These are particular age-specific cases. They cover different time intervals:

* Neonatal - From birth up to the first 28 days (excluding exactly 28 days);

* Postneonatal - From 28 days of age up to 1 year of age (excluding exactly 1 year);
Infant - A sum of the above two, so it covers the time from birth up to 1 year (excluding exactly 1 year).
It's commonly calculated annually and used for comparing health status among countries or historical periods.

* Maternal death rate - Another specific type as it deals only with women deceased during pregnancy or within 42 days of termination. It may be tricky to calculate as it excludes deaths caused by incidents unrelated to this state. It's another way of comparing the medical development of countries or periods; it also tells us what conditions may increase risks related to childbirth (e.g., age). Often, you can read about high maternal mortality rates in the past centuries as it had, perhaps surprisingly, a great impact on people's lifestyles.

* Combined mortality rate - A mixture of the specific rates often used in research. An instance could be the breast cancer mortality rate among women aged 35-79. This is age, cause, and sex-specific.

* Age-adjusted death rate - A standardized and more objective rate. Mortality increases with age, so if we simply compared an older society (such as Japanese with a median age of 48.6) with a younger one (e.g., the USA with a median age of 38.1), we'd find that the former has higher mortality rate. To eliminate such distortions, the values are adjusted using various statistical techniques, resulting in the age-adjusted death rate.

---

## 📗**MORTALITY RATE ANALYSIS AND PREDICTION USING PYTHON**
### **IMPLEMENTATION**
In this particular we will be aiming to visualize the given data using Tableau and Python and create plots for same.

The following steps will be followed for analysis-
1. Importing the libraries.
2. Defining a function to create plots.
3. Create plots.

For Prediction-
1. Load the Dataset
2. Find the missing values.
3. Plot Chloropeth Maps.
4. Normalize the data.
5. Splitting the Data in Test and Train Manually & Running Linear Regression
6. Validation Set & Cross Validation (Along with Linear Regression)


## 🎯**RESULTS**

![1](https://user-images.githubusercontent.com/36481036/196706291-96f4e119-e735-447c-8b4c-4f2a88f7e824.png)
![2](https://user-images.githubusercontent.com/36481036/196706302-397ca16f-52ad-418d-a6c3-8b060215d8cc.png)
![image](https://user-images.githubusercontent.com/36481036/196932834-c698a5d7-c1e8-4a8e-8bae-eccbc6ba7601.png)
![image](https://user-images.githubusercontent.com/36481036/196932962-e4005e31-8df2-4780-b8c8-b162a521ccb8.png)


## :page_facing_up: **CONCLUSION**
* The correlation between infant mortality rate and adult mortality rate and the average lifespan is as follows:
IMR and Lifespan: -0.196557
AMR and Lifespan: -0.696359
We see that the correlation between these two and average lifespan is negative, which means that if the infant mortality rate or the adult mortality rate rises, then the average lifespan decrease, which is quite intuitive

* We can see that schooling has a very strong direct correlation with the average lifespan, with a Pearson's correlation coefficient of 0.75. This may be due to the fact that schooling teaches many things about a healthy lifestyle and even first aids, which can be life saving in critical conditions

* Life expectancy has a direct positive correlation with drinking alcohol with a correlation coefficient of 0.404877

* The correlation coefficient of the population of a country and the life expectancy is -0.021538, which basically means that if the population rises, then the life expectancy decrease. This may be due to the fact the more population have severe effect on the capacity of the health system and it may crash because of this

## :bust_in_silhouette: **CREDITS**
* https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/mortality-rate
* https://www.kaggle.com/datasets/navinmundhra/world-mortality

**:sunglasses:** **CREATOR**- https://github.com/theshredbox
