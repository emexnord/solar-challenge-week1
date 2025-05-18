Interim Technical Report: Solar Data Analysis
Introduction
This project focuses on analyzing a solar dataset to preprocess data and detect outliers for a solar challenge. The dataset contains measurements such as Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), temperature, and wind speed, recorded at regular intervals. The goal is to clean the data, convert timestamps, and identify outliers using statistical methods to ensure data quality for further analysis. This interim report outlines the progress made, challenges encountered, and the plan to complete the project.
Methodology
The following steps have been implemented using Python and the pandas library:

Data Loading and Inspection:

Loaded the solar dataset into a pandas DataFrame.
Inspected column names and data using df.columns and df.head() to understand the structure.

Timestamp Conversion:

Converted the timestamp column to a datetime format using pd.to_datetime.
Set the timestamp as the DataFrame index for time-based analysis.

Column Name Cleaning:

Removed double quotes from column names (e.g., '"GHI_Avg"' to 'GHI_Avg') using df.columns.str.strip('"') to simplify access.

Outlier Detection:

Selected key columns (e.g., GHI, DNI, temperature, wind speed) for analysis.
Applied z-score calculations using scipy.stats.zscore to identify outliers (data points with z-scores > 3).

Results

Successfully loaded and cleaned the dataset, resolving issues with quoted column names.
Converted the timestamp column to datetime and set it as the index.
Implemented outlier detection, though some columns initially caused errors due to name mismatches.

Challenges & Solutions

Challenge: A KeyError occurred when accessing the "TIMESTAMP" column.

Cause: The column name was '"TIMESTAMP"' (with quotes) due to the dataset’s formatting.
Solution: Used the exact column name ('"TIMESTAMP"') and later cleaned all column names by removing quotes.

Challenge: Another KeyError occurred during outlier detection for columns like ' "DNI_Avg"', '"ModA"', and ' "ModB"'.

Cause: Leading spaces in some column names and non-existent columns ('"ModA"', '"ModB"') in the dataset.
Solution: Corrected the column list by removing spaces and excluding missing columns. Verified column names using print(df.columns) before processing.

Future Plan
To complete the project, the following tasks remain:

Validate Outlier Detection:

Test the outlier detection process on the cleaned dataset and analyze results.
Visualize outliers using plots (e.g., box plots or time series) to confirm findings.

Handle Missing Data:

Check for missing or invalid data in key columns and apply imputation or removal as needed.

Further Analysis:

Perform additional statistical analysis or modeling based on project requirements (e.g., correlating GHI and DNI with weather conditions).

Final Report:

Document all findings, including cleaned data, outlier analysis, and visualizations, in a comprehensive report.

These tasks will be completed by systematically testing each step and ensuring robust data quality.
Conclusion
Significant progress has been made in preprocessing the solar dataset, resolving column name issues, and setting up outlier detection. The challenges with KeyError exceptions were addressed by carefully inspecting and cleaning column names. I am confident in moving forward with the remaining tasks, as the core data processing pipeline is now functional. The next steps will focus on validating results and preparing a final analysis to meet the project’s objectives.
