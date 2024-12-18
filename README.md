# Garment-Worker-Productivity-Prediction-
The Garment Worker Productivity Prediction System is a web-based tool designed to predict the productivity of garment workers based on various input parameters. It employs a machine learning model hosted on a FastAPI backend to process user inputs and return predictions.
<p>
    <img src="./images/garment.jpeg" alt="readme Image"/>
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

    `fastapi run main.py
    
2. Access the Application:
    Copy this url and paste it on the web browser `http://127.0.0.1:8000`

Usage
- Task Management: Use the web interface to input data and get predictions for productivity.