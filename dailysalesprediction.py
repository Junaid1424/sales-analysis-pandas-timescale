import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
# Generate sample dataset for one day with random sales data
target_date = '2023-07-15'  # Example date to select
hours = pd.date_range(start=target_date, periods=24, freq='H')
sales_data = {
    'ds': hours,
    'y': np.random.randint(10, 100, size=24)  # Random sales data for each hour
}
df_day = pd.DataFrame(sales_data)

# Hourly Prediction
model_hourly = Prophet()
model_hourly.fit(df_day)
future_hourly = model_hourly.make_future_dataframe(periods=24, freq='H')  # Next 24 hours
forecast_hourly = model_hourly.predict(future_hourly)

# Create Plotly figure for Hourly Forecast
fig_hourly = go.Figure()
fig_hourly.add_trace(go.Scatter(x=df_day['ds'], y=df_day['y'], mode='lines', name='Actual'))
fig_hourly.add_trace(go.Scatter(x=forecast_hourly['ds'], y=forecast_hourly['yhat'], mode='lines', name='Forecast'))
fig_hourly.update_layout(title='Hourly Sales Forecast for {}'.format(target_date), xaxis_title='Time', yaxis_title='Sales')

# Dis
