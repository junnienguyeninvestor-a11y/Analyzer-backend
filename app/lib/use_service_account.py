import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
import json

# load .env
load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Load JSON key from env variable
# service_account_info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))

# Load JSON key from file 
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'credential.json')
with open(json_path, 'r') as file:
    service_account_info = json.load(file)

creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

client = gspread.authorize(creds)
#sheet = client.open_by_key(os.getenv("SPREADSHEET_ID")).sheet1


# Fetching data from sheet1
def fetch_data_from_sheet():
    sheet = client.open_by_key(os.getenv("SPREADSHEET_ID")).sheet1
    return sheet.get_all_values()

def get_sheet_dict(num):
    sheet = client.open_by_key(os.getenv("SPREADSHEET_ID")).get_worksheet(num-1)
    return sheet