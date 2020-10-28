import pandas as pd

# Read in CSV as pandas DataFrame
cities_df = pd.read_csv("Resources/cities.csv", index_col=0)

# Convert pandas DataFrame to HTML
cities_html = cities_df.to_html()

# Export the HTML file
text_file = open("cities.html", "w") 
text_file.write(cities_html) 
text_file.close() 