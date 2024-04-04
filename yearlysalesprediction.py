# Load the dataset
df = pd.read_csv('sales_dataset.csv')

# Rename columns as Prophet expects
df.columns = ['ds', 'y']

# Initialize and fit the Prophet model
model = Prophet()
model.fit(df)

# Make predictions for the next 365 days
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
plt.title('Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
