import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# To run this app, you need to have streamlit, pandas, and altair installed.
# pip install streamlit pandas altair

# --- Sidebar for user input ---
st.sidebar.header("Data Generation Parameters")
n_samples = st.sidebar.slider("Number of samples (n)", 100, 1000, 500)
a = st.sidebar.slider("Coefficient (a)", -10.0, 10.0, 2.0, 0.1)
noise_variance = st.sidebar.slider("Noise Variance (var)", 0.0, 1000.0, 100.0)
b = 5  # Keeping b constant

# --- Data Generation ---
@st.cache_data
def generate_data(n, a, var, b):
    X = np.random.rand(n, 1) * 10
    noise = np.random.randn(n, 1) * np.sqrt(var)
    y = a * X + b + noise
    return pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})

data = generate_data(n_samples, a, noise_variance, b)
X = data[['X']]
y = data['y']

# --- Modeling ---
model = LinearRegression()
model.fit(X, y)
data['y_pred'] = model.predict(X)
data['residual'] = data['y'] - data['y_pred']
r2 = r2_score(y, data['y_pred'])

# --- Outlier Detection ---
data['is_outlier'] = np.abs(data['residual']) > 1.5 * np.std(data['residual'])
outliers = data[data['is_outlier']].sort_values(by='residual', ascending=False).head(5)


# --- App Layout ---
st.title("Interactive Linear Regression")

# --- Visualization ---
st.header("Data Visualization")

# The basic scatter plot
scatter_plot = alt.Chart(data).mark_circle(size=60, opacity=0.6).encode(
    x='X',
    y='y',
    color=alt.condition(
        alt.datum.is_outlier,
        alt.value('red'),
        alt.value('blue')
    ),
    tooltip=['X', 'y', 'residual']
).properties(
    width=600,
    height=400
)

# The regression line
regression_line = alt.Chart(data).mark_line(color='red').encode(
    x='X',
    y='y_pred'
)

# Annotations for outliers
outlier_text = alt.Chart(outliers).mark_text(
    align='left',
    baseline='middle',
    dx=7,
    color='red'
).encode(
    x='X',
    y='y',
    text=alt.condition(alt.datum.is_outlier, alt.value('Outlier'), alt.value(''))
)


# Combine the charts
chart = alt.layer(
    scatter_plot, regression_line, outlier_text
).interactive()

st.altair_chart(chart, use_container_width=True)

# --- Outlier Table ---
st.header("Top 5 Outliers")
st.dataframe(outliers[['X', 'y', 'y_pred', 'residual']])

# Display model metrics
st.write("---")
st.header("Model Performance")
col1, col2, col3 = st.columns(3)
col1.metric("Coefficient (a)", f"{model.coef_[0]:.2f}")
col2.metric("Intercept (b)", f"{model.intercept_:.2f}")
col3.metric("R-squared", f"{r2:.2f}")
st.write("---")
