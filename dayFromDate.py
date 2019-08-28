import pandas as pd
order = pd.read_csv('https://query.data.world/s/3hIAtsCE7vYkPEL-O5DyWJAeS5Af-7')
order['Order_Date'] = pd.to_datetime(order['Order_Date'])

order['day'] = order['Order_Date'].dt.day_name()

print(order.head(10))