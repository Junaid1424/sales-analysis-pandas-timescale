import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import mplcursors
import plotly.graph_objects as go
# Load the dataset
df = pd.read_csv('sales_dataset.csv')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

df.columns = ['ds', 'y']
# Initializing Prophet model
model = Prophet()

# Daily Prediction
df_daily = df.resample('D', on='ds').sum().reset_index()  # Resample to daily
model_daily = Prophet()
model_daily.fit(df_daily)
future_daily = model_daily.make_future_dataframe(periods=7, freq='D')  # Next 7 days
forecast_daily = model_daily.predict(future_daily)

# Weekly Prediction
df_weekly = df.resample('W', on='ds').sum().reset_index()  # Resample to weekly
model_weekly = Prophet()
model_weekly.fit(df_weekly)
future_weekly = model_weekly.make_future_dataframe(periods=4, freq='W')  # Next 4 weeks
forecast_weekly = model_weekly.predict(future_weekly)

# Create Plotly figure for Daily Forecast
fig_daily = go.Figure()
fig_daily.add_trace(go.Scatter(x=df_daily['ds'], y=df_daily['y'], mode='lines', name='Actual'))
fig_daily.add_trace(go.Scatter(x=forecast_daily['ds'], y=forecast_daily['yhat'], mode='lines', name='Forecast'))
fig_daily.update_layout(title='Daily Sales Forecast', xaxis_title='Date', yaxis_title='Sales')

# Create Plotly figure for Weekly Forecast
fig_weekly = go.Figure()
fig_weekly.add_trace(go.Scatter(x=df_weekly['ds'], y=df_weekly['y'], mode='lines', name='Actual'))
fig_weekly.add_trace(go.Scatter(x=forecast_weekly['ds'], y=forecast_weekly['yhat'], mode='lines', name='Forecast'))
fig_weekly.update_layout(title='Weekly Sales Forecast', xaxis_title='Date', yaxis_title='Sales')

# Display the figures
fig_daily.show()
fig_weekly.show()
