from fastai.tabular import *
from flask import Flask, request
import requests
import os.path


path = ''

export_file_url = 'https://www.dropbox.com/s/wrgn9ncshu8w1vq/prescription_volume_next_year.pkl?dl=1'
export_file_name = 'prescription_volume_next_year.pkl'


def down_load_file(filename, url):
    """
    Download an URL to a file
    """
    with open(filename, 'wb') as fout:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        # Write response data to file
        for block in response.iter_content(4096):
            fout.write(block)
            
def download_if_not_exists(filename, url):
    """
    Download a URL to a file if the file
    does not exist already.
    Returns
    -------
    True if the file was downloaded,
    False if it already existed
    """
    if not os.path.exists(filename):
        down_load_file(filename, url)
        return True
    return False

download_if_not_exists(export_file_name, export_file_url)

learn = load_learner(path, export_file_name)



app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        Number_of_Manufacturers = float(request.form.get('Number_of_Manufacturers'))
        Total_Spending_2016 = float(request.form.get('Total_Spending_2016'))
        Total_Dosage_Units_2016 = float(request.form.get('Total_Dosage_Units_2016'))
        Total_Claims_2016 = float(request.form.get('Total_Claims_2016'))
        Total_Beneficiaries_2016 = float(request.form.get('Total_Beneficiaries_2016'))
        Total_Spending_2015 = float(request.form.get('Total_Spending_2015'))
        Total_Dosage_Units_2015 = float(request.form.get('Total_Dosage_Units_2015'))
        Total_Claims_2015 = float(request.form.get('Total_Claims_2015'))
        Total_Beneficiaries_2015 = float(request.form.get('Total_Beneficiaries_2015'))
        Total_Spending_2014 = float(request.form.get('Total_Spending_2014'))
        Total_Dosage_Units_2014 = float(request.form.get('Total_Dosage_Units_2014'))
        Total_Claims_2014 = float(request.form.get('Total_Claims_2014'))
        Total_Beneficiaries_2014 = float(request.form.get('Total_Beneficiaries_2014'))
        Total_Spending_2013 = float(request.form.get('Total_Spending_2013'))
        Total_Dosage_Units_2013 = float(request.form.get('Total_Dosage_Units_2013'))
        Total_Claims_2013 = float(request.form.get('Total_Claims_2013'))
        Total_Beneficiaries_2013 = float(request.form.get('Total_Beneficiaries_2013'))
        
        Average_Spending_Per_Dosage_Unit_Weighted_2016 = Total_Spending_2016/Total_Dosage_Units_2016
        Average_Spending_Per_Claim_2016 = Total_Spending_2016/Total_Claims_2016
        Average_Spending_Per_Beneficiary_2016 = Total_Spending_2016/Total_Beneficiaries_2016
        
        change_Spending_2013_2014 = ((Total_Spending_2014 - Total_Spending_2013)/Total_Spending_2013)*100
        change_Spending_2014_2015 = ((Total_Spending_2015 - Total_Spending_2014)/Total_Spending_2014)*100
        change_Spending_2016_2015 = ((Total_Spending_2016 - Total_Spending_2015)/Total_Spending_2015)*100
        
        change_Dosage_2013_2014 = ((Total_Dosage_Units_2014 - Total_Dosage_Units_2013)/Total_Dosage_Units_2013)*100
        change_Dosage_2014_2015 = ((Total_Dosage_Units_2015 - Total_Dosage_Units_2014)/Total_Dosage_Units_2014)*100
        change_Dosage_2015_2016 = ((Total_Dosage_Units_2016 - Total_Dosage_Units_2015)/Total_Dosage_Units_2015)*100
        
        change_Claims_2013_2014 = ((Total_Claims_2014 - Total_Claims_2013)/Total_Claims_2013)*100
        change_Claims_2014_2015 = ((Total_Claims_2015 - Total_Claims_2014)/Total_Claims_2014)*100
        change_Claims_2016_2015 = ((Total_Claims_2016 - Total_Claims_2015)/Total_Claims_2015)*100
        
        change_Beneficiaries_2013_2014 = ((Total_Beneficiaries_2014 - Total_Beneficiaries_2013)/Total_Beneficiaries_2013)*100
        change_Beneficiaries_2014_2015 = ((Total_Beneficiaries_2015 - Total_Beneficiaries_2014)/Total_Beneficiaries_2014)*100
        change_Beneficiaries_2015_2016 = ((Total_Beneficiaries_2016 - Total_Beneficiaries_2015)/Total_Beneficiaries_2015)*100
        
        
        change_Spend_Per_Dose_2013_2014 = (((Total_Spending_2014/Total_Dosage_Units_2014) - 
                                           (Total_Spending_2013/Total_Dosage_Units_2013))
                                           /(Total_Spending_2013/Total_Dosage_Units_2013))*100
        change_Spend_Per_Dose_2014_2015 = (((Total_Spending_2015/Total_Dosage_Units_2015) - 
                                           (Total_Spending_2014/Total_Dosage_Units_2014))
                                           /(Total_Spending_2014/Total_Dosage_Units_2014))*100
        change_Spend_Per_Dose_2015_2016 = (((Total_Spending_2016/Total_Dosage_Units_2016) - 
                                           (Total_Spending_2015/Total_Dosage_Units_2015))
                                           /(Total_Spending_2015/Total_Dosage_Units_2015))*100
        
        change_Spend_Per_Claim_2013_2014 = (((Total_Spending_2014/Total_Claims_2014) - 
                                           (Total_Spending_2013/Total_Claims_2013))
                                           /(Total_Spending_2013/Total_Claims_2013))*100
        change_Spend_Per_Claim_2014_2015 = (((Total_Spending_2015/Total_Claims_2015) - 
                                           (Total_Spending_2014/Total_Claims_2014))
                                           /(Total_Spending_2014/Total_Claims_2014))*100
        change_Spend_Per_Claim_2016_2015 = (((Total_Spending_2016/Total_Claims_2016) - 
                                           (Total_Spending_2015/Total_Claims_2015))
                                           /(Total_Spending_2015/Total_Claims_2015))*100
        
        change_Spend_Per_Beneficiaries_2013_2014 = (((Total_Spending_2014/Total_Beneficiaries_2014) - 
                                           (Total_Spending_2013/Total_Beneficiaries_2013))
                                           /(Total_Spending_2013/Total_Beneficiaries_2013))*100
        change_Spend_Per_Beneficiaries_2014_2015 = (((Total_Spending_2015/Total_Beneficiaries_2015) - 
                                           (Total_Spending_2014/Total_Beneficiaries_2014))
                                           /(Total_Spending_2014/Total_Beneficiaries_2014))*100
        change_Spend_Per_Beneficiaries_2015_2016 = (((Total_Spending_2016/Total_Beneficiaries_2016) - 
                                           (Total_Spending_2015/Total_Beneficiaries_2015))
                                           /(Total_Spending_2015/Total_Beneficiaries_2015))*100
        
        log_Total_Spending_2016 = log(Total_Spending_2016)
        log_Total_Dosage_Units_2016 = log(Total_Dosage_Units_2016)
        log_Total_Claims_2016 = log(Total_Claims_2016)
        log_Total_Beneficiaries_2016 = log(Total_Beneficiaries_2016)
        log_Average_Spending_Per_Claim_2016 = log(Average_Spending_Per_Claim_2016)
        log_Average_Spending_Per_Beneficiary_2016 = log(Average_Spending_Per_Beneficiary_2016)
        
        
        inf_df = pd.DataFrame(columns=['Number of Manufacturers', 'Total Spending 2016', 
                                       'Total Dosage Units 2016', 'Total Claims 2016', 'Total Beneficiaries 2016', 
                                       'Average Spending Per Dosage Unit (Weighted) 2016', 
                                       'Average Spending Per Claim 2016', 'Average Spending Per Beneficiary 2016', 
                                       'change%_Spending_2013-2014', 
                                       'change%_Spending_2014-2015', 'change%_Spending_2016-2015', 
                                       'change%_Dosage_2013-2014', 'change%_Dosage_2014-2015', 
                                       'change%_Dosage_2015-2016', 'change%_Claims_2013-2014', 
                                       'change%_Claims_2014-2015', 'change%_Claims_2016-2015', 
                                       'change%_Beneficiaries_2013-2014', 'change%_Beneficiaries_2014-2015', 
                                       'change%_Beneficiaries_2015-2016', 'change%_Spend_Per_Dose_2013-2014', 
                                       'change%_Spend_Per_Dose_2014-2015', 'change%_Spend_Per_Dose_2015-2016',
                                       'change%_Spend_Per_Claim_2013-2014', 'change%_Spend_Per_Claim_2014-2015', 
                                       'change%_Spend_Per_Claim_2016-2015', 'change%_Spend_Per_Beneficiaries_2013-2014',
                                       'change%_Spend_Per_Beneficiaries_2014-2015', 
                                       'change%_Spend_Per_Beneficiaries_2015-2016'])
        
        
        
        inf_df.loc[0] = [Number_of_Manufacturers, log_Total_Spending_2016, log_Total_Dosage_Units_2016, log_Total_Claims_2016,
                         log_Total_Beneficiaries_2016, Average_Spending_Per_Dosage_Unit_Weighted_2016, 
                         log_Average_Spending_Per_Claim_2016, log_Average_Spending_Per_Beneficiary_2016, 
                         change_Spending_2013_2014, change_Spending_2014_2015, change_Spending_2016_2015, 
                         change_Dosage_2013_2014, change_Dosage_2014_2015, change_Dosage_2015_2016, 
                         change_Claims_2013_2014, change_Claims_2014_2015, change_Claims_2016_2015,
                         change_Beneficiaries_2013_2014, change_Beneficiaries_2014_2015, 
                         change_Beneficiaries_2015_2016, change_Spend_Per_Dose_2013_2014, 
                         change_Spend_Per_Dose_2014_2015, change_Spend_Per_Dose_2015_2016,
                         change_Spend_Per_Claim_2013_2014, change_Spend_Per_Claim_2014_2015, 
                         change_Spend_Per_Claim_2016_2015, change_Spend_Per_Beneficiaries_2013_2014, 
                         change_Spend_Per_Beneficiaries_2014_2015, change_Spend_Per_Beneficiaries_2015_2016]
        
        
        answer = learn.predict(inf_df.iloc[0])[1].item()
        ok = int('%.0f'%(exp(answer)))
        

        
        
        return '''The input Number of Manufacturers is: {}<br>
                    <br>
                    The input total spending this year is: {}<br>
                    The input total dosage units this year are: {}<br>
                    The input total claims this year are: {}<br>
                    The input total beneficiaries this year are: {}<br>
                    <br>
                    The input total spending last year is: {}<br>
                    The input total dosage units last year are: {}<br>
                    The input total claims last year are: {}<br>
                    The input total beneficiaries last year are: {}<br>
                    <br>
                    The input total spending two years ago is: {}<br>
                    The input total dosage units two years ago are: {}<br>
                    The input total claims two years ago are: {}<br>
                    The input total beneficiaries two years ago are: {}<br>
                    <br>
                    The input total spending three years ago is: {}<br>
                    The input total dosage three years ago are: {}<br>
                    The input total claims three years ago are: {}<br>
                    The input total beneficiaries three years ago are: {}<br>
                    <br>
                    <h1>The predicted total dosage units for the next year is: {}</h1>
                    <br>
                    Note: If you left the default values for the prediction, the
                    answer you receive should be about 946,380 dosage units. The default
                    values were taken from an actual drug on Medicare Part D from years
                    2013 through 2016.  The actual total dosage units in 2017 was
                    1,050,323, so this prediction was within 6.5% of actual'''.format(Number_of_Manufacturers,
                                                                                   Total_Spending_2016,
                                                                                Total_Dosage_Units_2016,
                                                                               Total_Claims_2016,
                                                                               Total_Beneficiaries_2016,
                                                                                 Total_Spending_2015,
                                                                                Total_Dosage_Units_2015,
                                                                               Total_Claims_2015,
                                                                               Total_Beneficiaries_2015,
                                                                                 Total_Spending_2014,
                                                                                Total_Dosage_Units_2014,
                                                                               Total_Claims_2014,
                                                                               Total_Beneficiaries_2014,
                                                                                 Total_Spending_2013,
                                                                                Total_Dosage_Units_2013,
                                                                               Total_Claims_2013,
                                                                               Total_Beneficiaries_2013, ok)

    return '''<form method="POST">
                  <h1>Predicting the total dosage units for next year</h1>
                  
                  How many manufacturers produce the drug?: <input type="number" name="Number_of_Manufacturers" step=1 min=1 max =10 value="1"><br>
                  
                  <h3>For this year</h3>
                  What was the total spending?: <input type = "number" name="Total_Spending_2016" min=1 step=0.01 value="215930.43">
                  What was the total Dosage units?: <input type = "number" name="Total_Dosage_Units_2016" min=1 step=0.01 value="1050323">
                  <br>
                  What was the total Claims?: <input type = "number" name="Total_Claims_2016" min=1 step=0.01 value="8897">
                  What was the total number of Beneficiaries?: <input type = "number" name="Total_Beneficiaries_2016" min=1 step=0.01 value="3423">
                  <br>
                  
                  <h3>For last year</h3>
                  What was the total spending?: <input type = "number" name="Total_Spending_2015" min=1 step=0.01 value="133958.3">
                  What was the total Dosage units?: <input type = "number" name="Total_Dosage_Units_2015" min=1 step=0.01 value="717548">
                  <br>
                  What was the total Claims?: <input type = "number" name="Total_Claims_2015" min=1 step=0.01 value="5789">
                  What was the total number of Beneficiaries?: <input type = "number" name="Total_Beneficiaries_2015" min=1 step=0.01 value="2283">
                  <br>
                  
                  <h3>For two years ago</h3>
                  What was the total spending?: <input type = "number" name="Total_Spending_2014" min=1 step=0.01 value="123285.7">
                  What was the total Dosage units?: <input type = "number" name="Total_Dosage_Units_2014" min=1 step=0.01 value="677160">
                  <br>
                  What was the total Claims?: <input type = "number" name="Total_Claims_2014" min=1 step=0.01 value="5620">
                  What was the total number of Beneficiaries?: <input type = "number" name="Total_Beneficiaries_2014" min=1 step=0.01 value="2087">
                  <br>
                  
                  <h3>For three years ago</h3>
                  What was the total spending?: <input type = "number" name="Total_Spending_2013" min=1 step=0.01 value="94537.7">
                  What was the total Dosage units?: <input type = "number" name="Total_Dosage_Units_2013" min=1 step=0.01 value="518920">
                  <br>
                  What was the total Claims?: <input type = "number" name="Total_Claims_2013" min=1 step=0.01 value="4376">
                  What was the total number of Beneficiaries?: <input type = "number" name="Total_Beneficiaries_2013" min=1 step=0.01 value="1620">
                  <br>

                  <input type="submit" value="Submit"><br>
              </form>'''
