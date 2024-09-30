import pandas as pd
from bs4 import BeautifulSoup
from api.openai_api_helper import get_embedding
from core.constants import *

def read_csv(file_path: str) -> pd.core.frame.DataFrame:
  df = pd.read_csv(file_path)
  return df

def clean_data(df : pd.core.frame.DataFrame):
  df = df.dropna()
  return df
def get_product_embeddings():
  products_df = read_csv(File.PRODUCT_INPUT_FILE_PATH)
  products_df = clean_data(products_df)

  products_embeddings = []
  for index, row in products_df.iterrows(): 
    product_description_html = BeautifulSoup(row["Description"])
    product_description_zero_html = product_description_html.get_text().replace('\n',' ') 

    if len(product_description_zero_html) > 100:
      product_description_zero_html = product_description_zero_html.split('.')[0]
    else:
      product_description_zero_html = product_description_zero_html[:100]

    single_product_full_description = row["Title"] + " " + product_description_zero_html
    
    single_product_embedding = get_embedding(single_product_full_description)
    single_product_embedding 
    
    products_embeddings.append((row["Title"], single_product_full_description, row["Price"], single_product_embedding))

  products_embeddings = pd.DataFrame(products_embeddings)
  products_embeddings.columns = ["Title", "Full Description", "Price", "Embedding"]
  products_embeddings.to_csv(File.PRODUCT_EMBEDDINGS_FILE_PATH, index=False)

def apply_mask_for_dataframe(df, masks : list):
  combined_mask = ""
  if len(masks) == 1:
    combined_mask = masks[0]
  else:
    combined_mask = " & ".join(masks)
 
  return df.query(combined_mask)

def get_products_with_prices(df):
  return df[["Title", "Price"]]

def get_products_with_prices_string(df):
    combined_string = ""
    for index, row in df.iterrows():
        combined_string += f"Title: {row['Title']}, Price: {row['Price']}\n"
    return combined_string