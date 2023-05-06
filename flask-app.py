import subprocess
from datetime import datetime


#def run_program(program_path):
 #   output = subprocess.run(['python3', program_path], capture_output=True, text=True)
  #  return output.stdout
def run_program(program_path):
    # Get the output from the program
    output = subprocess.run(['python3', program_path], capture_output=True, text=True)
    
    # Extract the usage and percentage values from the output
    print(output)
    print(program_path)
    match program_path:
        case './electricityalert.py':
            _,_,usage, percentage = output.stdout.split('\n')[:4]
            print(output.stdout.split('\n')[:4])
            print("Here")
            #print(percentage)
            usage = usage.split(': ')[1]
            print(usage)
            percentage = percentage.split(': ')[1]
            print(percentage)
    
            # Get the current date
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d")
            print(date_string)
    
            # Return the usage, percentage, and date values along with the output
            return {
                'output': output.stdout,
                'usage': usage,
                'percentage': percentage,
                'date_string': date_string
            }
        case './electricity_now.py':
            return{
              output.stdout  
            }

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/electricity_now')
def electricity_now():
    #print("I am on electicity_now function")
    output = run_program('./electricity_now.py')
    return render_template('electricity_now.html', output=output)

@app.route('/electricityalert')
def electricityalert():
    #output = run_program('./electricityalert.py')
    #return render_template('electricityalert.html', usage=usage, percentage=percentage, date_string=date_string)
    result = run_program('./electricityalert.py')
    usage = result['usage']
    percentage = result['percentage']
    date_string = result['date_string']
    return render_template('electricityalert.html', usage=usage, percentage=percentage, date_string=date_string)
if __name__ == '__main__':
    app.run()
