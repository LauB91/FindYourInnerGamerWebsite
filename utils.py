import pandas as pd
import requests
from bs4 import BeautifulSoup

BUCKET_NAME='find_your_inner_gamer'
BUCKET_CSV_DATA_PATH="data/clean_df.csv"

def get_img(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    try:
        return soup.find('img', class_='game_header_image_full').attrs['src']
    except AttributeError:
        return 'no image'


def get_data_from_gcp():
    """method to get the  data from google cloud bucket"""
    path = f"gs://{BUCKET_NAME}/{BUCKET_CSV_DATA_PATH}"
    return pd.read_csv(path)
