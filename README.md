# Garment-Worker-Productivity-Prediction-
The Garment Worker Productivity Prediction System is a web-based tool designed to predict the productivity of garment workers based on various input parameters. It employs a machine learning model hosted on a FastAPI backend to process user inputs and return predictions.
<p>
    <img src="https://github.com/Lynn-rose/Garment-Worker-Productivity-Prediction-/blob/main/app/static/images/garment.jpeg" alt="readme Image"/>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Surprise-4B0082?logo=python&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Vercel-FF4B4B?logo=vercel&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-NLTK-4EA94B?logo=python&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Seaborn-3776AB?logo=python&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Django-3F4F75?logo=django&logoColor=white&style=flat-square">
</p>

#### Authors
* [Lynn Achieng](https://github.com/Lynn-rose)

## Introduction
The garment industry, driven by tight margins, depends on worker productivity for efficiency and profitability. Variability in performance due to factors like skill levels and conditions disrupts production. Predicting productivity enables managers to optimize processes, address bottlenecks, and meet production targets, ensuring cost management, operational efficiency, and high-quality output.

## Objective
The Garment Worker Productivity Prediction project aims to accurately forecast the productivity of garment factory workers based on various workplace, environmental, and operational factors. This prediction is crucial for optimizing resource allocation, improving workflow efficiency, and maintaining high-quality production standards while reducing operational costs.

## Project Overview
- **Business Understanding**: Exploring the business reasons for our data mining effort and what the company hopes to gain from the project.
- **Data Understanding**: The datasets we utilized comprised of csv files.
- **Data Preparation**: It mainly involved; selecting the data to discover the columns to be used, cleaning the data to correct and remove erroneous values, formatting the data to effectively perform mathematical operations and integrating the datasets to create a merged dataset for effective analysis.
- **Exploratory Data Analysis**: The goal of this procedure is to summarize the main characteristics of the dataset, which is often done visually.
- **Modelling**: To further support and provide insight we built a hybrid-based system.
- **Evaluation**: Accuracy Score, Mean Absolute Error abd Root Mean Squared Error were used to measure the average of absolute deviance between actual and predicted ratings given by users.

## Setup Instructions

All these should be done in the terminal.

1. Clone the Repository:

    `git clone git@github.com:Lynn-rose/Garment-Worker-Productivity-Prediction-.git`
    
     `cd your-repo-name`
     
2. Create and Activate a Virtual Environment:

 `python3 -m venv env`
 
 `source env/bin/activate`
 
 On Windows, use `env\Scripts\activate`
 
3. Create your branch and move into your branch

  `git checkout -b branch-name`
  
4. Install Dependencies:

Generate a `requirements.txt` file using this command

   `pip freeze > requirements.txt`
    
   Install the required packages:
    
   `pip install -r requirements.txt`

Frontend Setup
If using plain HTML/CSS/JavaScript, ensure your static files are correctly placed in the `static` directory of your Django project.

Running the Application
1. Start the Backend Server:

    `fastapi run main.py`
    
2. Access the Application:
    Copy this url and paste it on the web browser `http://127.0.0.1:8000`

Usage
- Task Management: Use the web interface to input data and get predictions for productivity.

## Our Data
* `date`: Date of the record.
* `quarter`: The quarter of the year (e.g., Q1, Q2).
* `department`: Department of workers (e.g., sewing, finishing).
* `team`: The number representing the team.
* `targeted_productivity`: The target productivity (between 0 and 1).
* `smv`: Standard Minute Value (time required to complete the task).
* `wip`: Work In Progress (missing values present).
* `over_time`: Overtime in minutes.
* `incentive`: Bonus paid to workers.
* `idle_time`: Time during which no work was done.
* `idle_men`: Number of idle workers.
* `no_of_style_change`: Number of style changes in production.
* `no_of_workers`: Number of workers in the team.
* `actual_productivity`: Target variable representing the productivity achieved (between 0 and 1).

We also conducted feature engineering on some columns to capture more information. All this is well documented in the included project [**writeup**](https://github.com/Lynn-rose/Garment-Worker-Productivity-Prediction-/blob/main/Garment%20production.odt).

## EDA

We conducted some EDA that yielded us some domain knowledge we could use to inform future steps and modelling
Some of the plots we came up with are shown below: 
<p align='center'>
    <img src="https://github.com/Lynn-rose/Garment-Worker-Productivity-Prediction-/blob/main/app/static/images/Screenshot%20from%202024-12-13%2005-50-43.png" alt="Analysis of Target Variable"/>
    <img src="https://github.com/Lynn-rose/Garment-Worker-Productivity-Prediction-/blob/main/app/static/images/Screenshot%20from%202024-12-13%2005-59-16.png" alt="Feature-Target Relationships"/>
    <img src="https://github.com/Lynn-rose/Garment-Worker-Productivity-Prediction-/blob/main/app/static/images/Screenshot%20from%202024-12-13%2006-10-05.png" alt="Correlation Analysis"/>
</p> 

## Modelling 

We built multiple models powered by different algorithms.
These include:
* `Linear Regression`
* `Ridge and Lasso Regression`
* `Random Forest Regressor`
* `Gradient Boosting Regressor`
* `XGBoost Regressor`
* `Support Vector Regressor`
* `AdaBoost Regressor`

The best performing ones were tuned and ensembled to produce one model however this did not exhibit better performance. Further scaling of the dataset was done and cross validation included to improve the accuracy score  

## Additional Documentation

As mentioned before included in this repository is the complete project documentation. This includes:
* [Write-up documentation](https://github.com/Lynn-rose/Garment-Worker-Productivity-Prediction-/blob/main/Garment%20production.odt).

For any additional questions, please contact Lynn Rose Achieng, lynn90952@gmail.com
