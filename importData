import psycopg2
## connection to the database
## Remember to replace your credentials
con = psycopg2.connect(
    host='your_host',
    port='your_port',
    database='your_database',
    user='your_username',
    password='your_password'
)
cursor = con.cursor()
# Query data from the database
Q = "SELECT time, sales FROM sales WHERE time >= '2020-01-01' AND time <= '2023-12-31'"
query = sql.SQL(Q)
cursor.execute(query)
# Fetch the data
data = cursor.fetchall()

dates = []
sales = []

for date, sale in data:
    dates.append(date)
    sales.append(sale)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame({'date': dates, 'sale': sales})
