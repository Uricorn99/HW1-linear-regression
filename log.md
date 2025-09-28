# Project Log

**Note:** Using numbering format #.# where the first # is the global task number and the second # is the local task number in each round.

1.1 Create log.md to log all steps for this project.

2.1 Use CRISP-DM methodology to plan solving a simple linear regression problem in Python.

CRISP-DM (Cross-Industry Standard Process for Data Mining) is a widely used methodology for data mining projects. Here's how it can be applied to a simple linear regression problem in Python:

1.  **Business Understanding:**
    *   **Objective:** To understand the project objectives and requirements from a business perspective.
    *   **Explanation:** In this phase, we define the problem we want to solve. For a simple linear regression problem, this could be predicting a continuous value based on a single input feature. For example, predicting a person's weight based on their height, or a house's price based on its square footage. The goal is to establish a clear success criterion for the project.

2.  **Data Understanding:**
    *   **Objective:** To collect, assess, and explore the initial data.
    *   **Explanation:** This phase starts with initial data collection and proceeds with activities in order to get familiar with the data, to identify data quality problems, to discover first insights into the data, or to detect interesting subsets to form hypotheses for hidden information. For our linear regression problem, we would look at the statistical properties of our variables, and visualize the data to see if there is a linear relationship between the input and output variables.

3.  **Data Preparation:**
    *   **Objective:** To construct the final dataset for modeling from the initial raw data.
    *   **Explanation:** This phase involves all activities to construct the final dataset (data that will be fed into the modeling tool) from the initial raw data. Data preparation tasks are likely to be performed multiple times, and not in any prescribed order. Tasks include table, record, and attribute selection as well as transformation and cleaning of data for modeling tools. For linear regression, this might involve handling missing values, removing outliers, and splitting the data into training and testing sets.

4.  **Modeling:**
    *   **Objective:** To select and apply various modeling techniques and calibrate their parameters to optimal values.
    *   **Explanation:** In this phase, various modeling techniques are selected and applied, and their parameters are calibrated to optimal values. Typically, there are several techniques for the same data mining problem type. Some techniques have specific requirements on the form of data. Therefore, stepping back to the data preparation phase is often needed. For our problem, we will use the simple linear regression algorithm. In Python, this can be easily implemented using libraries like `scikit-learn`.

5.  **Evaluation:**
    *   **Objective:** To evaluate the model's performance and and ensure it meets the business objectives.
    *   **Explanation:** Before proceeding to final deployment of the model, it is important to more thoroughly evaluate the model, and review the steps executed to construct the model, to be certain it properly achieves the business objectives. A key objective is to determine if there is some important business issue that has not been sufficiently considered. At the end of this phase, a decision on the use of the data mining results should be reached. For our linear regression model, we would use metrics like R-squared, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) to assess its performance on the test data.

6.  **Deployment:**
    *   **Objective:** To deploy the model into a production environment.
    *   **Explanation:** Creation of the model is generally not the end of the project. Even if the purpose of the model is to increase knowledge of the. The knowledge gained will need to be organized and presented in a way that the customer can use it. Depending on the requirements, the deployment phase can be as simple as generating a report or as complex as implementing a repeatable data mining process. For our problem, this could involve saving the trained model to a file and creating a simple application that can load the model and make predictions on new data.

3.1 Confirmed to use append for logging.

4.1 Generate synthetic data and fit a linear regression model in app.py.

4.2 Run app.py and show the regression score result.

4.3 `python` command not found, trying with `py`.

5.1 Expand app.py to allow user input for data generation parameters.

6.1 Convert the project into a Streamlit app in app.py.

6.2 Run the Streamlit app once to ensure functionality.

6.3 'streamlit' command not found. Instructed user to install it.

6.4 Attempting to run the Streamlit app again.

6.5 `streamlit` command still not found, trying with `py -m streamlit run app.py`.

7.1 Improve the Streamlit app with outlier highlighting and interactive visualization.

7.2 Run the improved Streamlit app.

8.1 Modify slider parameters in app.py and verify the app.

9.1 Rearrange sections and update plot style in app.py.

10.1 Create requirements.txt for app.py.

11.1 Initialize git repository.
11.2 Add remote origin.
11.3 Stage all files.
11.4 Commit files.
11.5 Push to remote repository.
