import pandas as pd
import taipy.gui.builder as tgb
from taipy.gui import Gui

# STEP 1: Define the function to process stock data . Convert Date column to datetime format
def get_data(path_to_csv: str):
    dataset = pd.read_csv(path_to_csv)
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    return dataset

# STEP 2: Load the stock data 
path_to_csv = "TSLA.csv"
dataset = get_data(path_to_csv)

# STEP 3: Create a GUI using Taipy and display the stock opening price chart
with tgb.Page() as page:   
  tgb.text("# Tesla Stock Opening Price",mode='md')          
  tgb.chart("{dataset}", x="Date", y="Open")
Gui(page).run(debug=True)
