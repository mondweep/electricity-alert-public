import requests
import json
import datetime

# Set up the Octopus Energy API credentials
api_key = 'add api id'
meter_id = 'add meter MPAN'
meter_sr_no = 'add meter serial number'

# Set the start and end date for the daily budget
today = datetime.date.today()
start_date = today.strftime('%Y-%m-%d')
end_date = (today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
print(start_date, end_date)
# Set the daily budget in kWh
daily_budget = 10

# Make the API call to retrieve the smart meter data
url = f'https://api.octopus.energy/v1/electricity-meter-points/{meter_id}/meters/{meter_sr_no}/consumption/'
params = {'period_from': start_date, 'period_to': end_date, 'group_by': 'day'}
#headers = {'Authorization': f'key {api_key}',
#'Content-Type': 'application/json',
#'Accept': 'application/json'
#}
#print(headers)
#response = requests.get(url, headers=headers, params=params)
response = requests.get(url, auth = (api_key,''))
#print(response.text)

if response.status_code != 200:
    print('Error retrieving smart meter data')
else:
    # Parse the response data
    data = json.loads(response.text)
    results_list = data['results']
    #print(results_list)   
    #Extract the current consumption data
    if isinstance(results_list, list):    
        latest_reading = results_list[0]
        usage = latest_reading['consumption']
        timestamp = latest_reading['interval_start']
    else:
        latest_reading = results_list[0]
        usage = data['consumption']
        timestamp = latest_reading['interval_start']
    #Format the timestamp
    dt_object = datetime.datetime.fromisoformat(timestamp)
    formatted_timestamp = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    print(f'Latest Electricity usage ({formatted_timestamp}): {usage} kWh')
