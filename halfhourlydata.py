import requests
import json
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Set up the Octopus Energy API credentials
api_key = 'add api id'
meter_id = 'add meter mpan'
meter_sr_no = 'add meter serial number'

# Set the start and end date for the daily consumption
today = datetime.date.today()
start_date = today.strftime('%Y-%m-%d')
end_date = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Make the API call to retrieve the smart meter data
url = f'https://api.octopus.energy/v1/electricity-meter-points/{meter_id}/meters/{meter_sr_no}/consumption/'
params = {'period_from': start_date, 'period_to': end_date, 'group_by': 'half_hour'}
response = requests.get(url, auth = (api_key,''))

if response.status_code != 200:
    print('Error retrieving smart meter data')
else:
    # Parse the response data
    data = json.loads(response.text)
    results_list = data['results']
    
    # Extract the consumption data for each half-hour period of the day
    consumption_data = {}
    for result in results_list:
        consumption = result['consumption']
        interval_end = result['interval_end']
        print(interval_end)
        hour, minute, second = interval_end.split('T')[1].split('+')[0].split(':')
        half_hour = f'{int(hour)}:{int(minute)//30*30}'
        if half_hour in consumption_data:
            consumption_data[half_hour] += consumption
        else:
            consumption_data[half_hour] = consumption
    
    # Convert the consumption data to a numpy array
    half_hours = sorted(consumption_data.keys())
    consumption = [consumption_data[h] for h in half_hours]
    x_pos = np.arange(len(half_hours))
    
    # Create a bar chart of the consumption data
    plt.bar(x_pos, consumption, align='center', alpha=0.5)
    plt.xticks(x_pos, half_hours)
    plt.ylabel('Electricity Consumption (kWh)')
    plt.title('Electricity Consumption over the Day')
    plt.show()
