### U.S. weather history visualization

**GOAL**
The goal is to analyse the 12 months data of US industry and find th conclusion and display them via graphs.


**WHAT I HAD DONE**
- I have analysed the U.S. weather history
- I have represented my observation/results via visualization

**MODELS USED**
-  Linear Regression
-  K-Nearest Neighbors
-  Random Forest Regressor
-  Decision Tree Regressor

**LIBRARIES NEEDED**
- matplotlib.pyplot
- pandas

#### Code

Code file | Description
---|---------
`wunderground_scraper.py` | Downloades weather data web pages from Weather Underground
`wunderground_parser.py` | Parses the weather data from Weather Underground into a flat CSV file
`visualize_weather.py` | Creates the visualization of the weather data

#### Data/Dataset

The raw data and code behind the story [Dataset](http://fivethirtyeight.com/features/what-12-months-of-record-setting-temperatures-looks-like-across-the-u-s/)
Column | Description
---|---------
`date` | The date of the weather record, formatted YYYY-M-D
`actual_mean_temp` | The measured average temperature for that day
`actual_min_temp` | The measured minimum temperature for that day
`actual_max_temp` | The measured maximum temperature for that day
`average_min_temp` | The average minimum temperature on that day since 1880
`average_max_temp` | The average maximum temperature on that day since 1880
`record_min_temp` | The lowest ever temperature on that day since 1880
`record_max_temp` | The highest ever temperature on that day since 1880
`record_min_temp_year` | The year that the lowest ever temperature occurred
`record_max_temp_year` | The year that the highest ever temperature occurred
`actual_precipitation` | The measured amount of rain or snow for that day
`average_precipitation` | The average amount of rain or snow on that day since 1880
`record_precipitation` | The highest amount of rain or snow on that day since 1880

Source: [Weather Underground](http://wunderground.com)
