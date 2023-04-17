import pandas as pd
import plotly.graph_objects as go
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

fields =['Months', 'Hilo', 'Hana', 'Princeville']
df = pd.read_csv('rainfall_data.csv', skipinitialspace=True, usecols=fields)

month = df.Months
hilo = df.Hilo
hana = df.Hana
princeville = df.Princeville
#month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#hana = [7.77, 4.91, 8.99, 7.11, 5.58, 4.31, 5.94, 5.77, 6.82, 7.28, 7.77, 6.98]
#princeville = [6.91, 6.22, 7.00, 6.20, 5.11, 4.39, 5.77, 5.70, 5.68, 6.63, 10.04, 8.11]

fig = go.Figure()

fig.add_trace(go.Scatter(x=month, y=hilo, name='Hilo', line=dict(color='firebrick', width=4)))
fig.add_trace(go.Scatter(x=month, y=hana, name = 'Hana', line=dict(color='blue', width=4)))
fig.add_trace(go.Scatter(x=month, y=princeville, name='Princeville', line=dict(color='orange', width=4)))
fig.update_layout(title='Average rainfall in inches', xaxis_title='Months', yaxis_title='Rainfall (inches)')
fig.show()



