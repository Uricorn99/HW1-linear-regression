# Todo List for Simple Linear Regression Project

## 1. Business Understanding
- [x] Define the specific problem to be solved (e.g., predict house price based on square footage).
- [x] Define the success criteria for the model (e.g., achieve an R-squared value of 0.8 or higher).

## 2. Data Understanding
- [x] Find or generate a suitable dataset.
- [ ] Load the dataset into a pandas DataFrame.
- [ ] Use `df.info()` and `df.describe()` to get a summary of the data.
- [x] Visualize the relationship between the independent and dependent variables using a scatter plot.

## 3. Data Preparation
- [ ] Check for and handle any missing values.
- [x] Split the data into training and testing sets (e.g., 80% training, 20% testing).

## 4. Modeling
- [x] Import the `LinearRegression` class from `sklearn.linear_model`.
- [x] Create an instance of the `LinearRegression` model.
- [x] Train the model using the training data (`model.fit()`).
- [x] Get the model's coefficients (slope and intercept).

## 5. Evaluation
- [x] Make predictions on the testing data (`model.predict()`).
- [x] Calculate the Mean Squared Error (MSE) and R-squared score.
- [x] Visualize the regression line on the scatter plot of the data.

## 6. Deployment
- [ ] Save the trained model to a file using `joblib` or `pickle`.
- [x] Create a simple Python script that loads the model and makes a prediction on new input data.
