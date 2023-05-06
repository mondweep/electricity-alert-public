import requests
import json
import datetime

# Set up the Octopus Energy API credentials
api_key = 'add-api-key'
meter_id = 'add meter MPAN'
meter_sr_no = 'add meter serial number'

# Set the start and end date for the daily budget
today = datetime.date.today()
start_date = today.strftime('%Y-%m-%d')
end_date = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Set the daily budget in kWh
daily_budget = 10

# Make the API call to retrieve the smart meter data
url = f'https://api.octopus.energy/v1/electricity-meter-points/{meter_id}/meters/{meter_sr_no}/consumption/'
params = {'period_from': start_date, 'period_to': end_date, 'group_by': 'day'}
headers = {'Authorization': f'key {api_key}',
'Content-Type': 'application/json',
'Accept': 'application/json'
}
print(headers)
#response = requests.get(url, headers=headers, params=params)
response = requests.get(url, params=params,auth = (api_key,''))
print(response)

if response.status_code != 200:
    print('Error retrieving smart meter data')
else:
    # Parse the response data
    data = json.loads(response.text)

    # Extract the usage data for the current day
    usage = data['results'][0]['consumption']

    # Calculate the percentage of the daily budget used
    percentage = usage / daily_budget * 100

    # Print the usage and percentage
    print(f'Usage for {start_date}: {usage} kWh')
    print(f'Percentage of daily budget used: {percentage}%')

    # Check if the usage is near the daily budget limit
    if percentage >= 80:
        # Send an alert
        print('Usage is near the daily budget limit - please conserve energy!')

