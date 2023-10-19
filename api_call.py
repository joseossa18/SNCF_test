#The necessary libraries are imported
import requests
import pandas as pd

#Variables are defined for the url and endpoint
url =  'http://v0.ovapi.nl/'
endpoint = '/line/'

#Both variables are concatenated to get one complete url to make the call
complete_url = f'{url}{endpoint}'

#The get request is made using the function get from the requests library and catch the response in the variable r
r = requests.get(complete_url)
#The Response Object (r in this case) has an associate method json which is a built in decoder that will be used to deal with the json data
#This method returns a dictionary, making it easier to work with
json_data = r.json()

#As the requested output is a csv file, the best way is to convert the dictionary into a pandas Data Frame.
#The dataframe has to be transposed so that keys, which in this case are the Lines, can be displayed as rows
df = pd.DataFrame(json_data).T
#Then the reset_idex method is used just to make the lines another column, so that the name of the column can be changed. 
#The purpose of this is to have a better format and avoid any possible errors when importing the csv to any other database
df = df.reset_index()
df = df.rename(columns={'index': 'Line'})

#Finally the Data Frame is exported as a CSV file. 
#The parameter index = False so that the CSV does not have an extra column with the index created in the Data Frame
df.to_csv('lines.csv', index = False)
