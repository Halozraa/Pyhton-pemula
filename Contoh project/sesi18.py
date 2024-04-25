import pandas as pd

#Read The CSV file into a DataFrame
df = pd.read_csv('data_pengangguran.csv') # untuk membaca format csv

# Write The DataFrame to an Excel FIle
df.to_html('data_pengangguran.html', index=False) #untuk merubah format csv to html