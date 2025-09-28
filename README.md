# Project Report: Simple Linear Regression Streamlit App

Demo site: https://hw1-linear-regression-zwrulmpdkdkysfpienvcr8.streamlit.app/

## 1. Project Overview

This project demonstrates the implementation of a simple linear regression model in Python. The project follows the CRISP-DM methodology to structure the data mining process. The final outcome is an interactive web application built with Streamlit that allows users to:
- Generate synthetic linear data by specifying parameters like the number of samples, coefficient, and noise variance.
- Visualize the generated data with a scatter plot.
- Fit a linear regression model to the data and visualize the regression line.
- Identify and highlight outliers in the data.
- View model performance metrics such as the coefficient, intercept, and R-squared score.

## 2. Methodology: CRISP-DM

The project was structured using the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology. This iterative process provides a framework for data mining projects and consists of the following phases:

1.  **Business Understanding:** Defining the project objectives and requirements. In this project, the objective was to build a simple linear regression model and visualize its performance.
2.  **Data Understanding:** Collecting and exploring the data. We started with a simple synthetic dataset to understand the relationship between the variables.
3.  **Data Preparation:** Preparing the data for modeling. This involved generating the data based on user-defined parameters and splitting it into training and testing sets (in the initial script).
4.  **Modeling:** Building and training the model. We used the `LinearRegression` model from `scikit-learn` to fit the data.
5.  **Evaluation:** Evaluating the model's performance. We used the R-squared score to evaluate the model and visualized the regression line.
6.  **Deployment:** Deploying the model. The model was deployed as an interactive Streamlit web application.

## 3. Implementation Details

### 3.1. Initial Python Script (`app.py`)

The project started with a simple Python script that:
- Generated synthetic linear data using `numpy`.
- Fitted a `LinearRegression` model from `scikit-learn`.
- Printed the model's coefficient, intercept, and R-squared score to the console.

### 3.2. Interactive Console App

The script was then expanded to allow user input from the console for the data generation parameters:
- Number of samples (`n`)
- Coefficient (`a`)
- Noise variance (`var`)

### 3.3. Streamlit Web Application

The console-based application was converted into a full-fledged interactive web application using Streamlit. The Streamlit app provides a user-friendly interface with the following features:

- **Sidebar Controls:** Sliders in the sidebar allow users to dynamically change the data generation parameters (`n`, `a`, `var`).
- **Interactive Visualization:** The generated data is visualized using an interactive scatter plot created with `altair`. The plot shows the data points, the regression line, and highlights outliers.
- **Outlier Detection:** The app identifies outliers based on their residuals and highlights them in the plot and in a separate table.
- **Model Performance Metrics:** The app displays the model's coefficient, intercept, and R-squared score, which are updated dynamically as the data generation parameters are changed.

## 4. File Structure

The project consists of the following files:

- `app.py`: The main Python script containing the Streamlit application.
- `requirements.txt`: A list of the Python libraries required to run the project.
- `log.md`: A log of all the steps taken during the project development.
- `Todo.md`: A to-do list used to track the implementation tasks.
- `README.md`: This report.

## 5. Dependencies

To run this project, you need to install the following Python libraries:

```
streamlit
numpy
pandas
altair
scikit-learn
```

You can install them using pip:
`pip install -r requirements.txt`

## 6. How to Run the Application

1.  Make sure you have Python and `pip` installed.
2.  Install the required libraries from `requirements.txt`:
    `pip install -r requirements.txt`
3.  Run the Streamlit app from your terminal:
    `streamlit run app.py`
    or
    `py -m streamlit run app.py`

This will open the application in your web browser.

## 7. GitHub Repository

The project is version-controlled with `git` and is intended to be pushed to a GitHub repository. The following steps were taken to set up the repository:

1.  Initialized a local `git` repository.
2.  Added a remote origin: `https://github.com/Uricorn99/HW1-linear-regression.git`
3.  Staged all project files.
4.  Committed the files with the message: "Initial commit: Linear Regression Streamlit App".

The final step of pushing to the remote repository requires user authentication and should be done by the user.
