from __future__ import print_function
import pickle
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
def get_mark_xml():
    SERVICE_ACCOUNT_FILE = 'mark_keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1QQMXzzrQJcSp9WzHtZtge-RQEFV4ZKOzPRU6ZsOcGzI'

    service = build('sheets','v4',credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="A1:Z9993").execute()
    df = pd.DataFrame(result['values'][1:],columns=result['values'][0])
    return result['values']

def upload_spreadsheets(data):
    SERVICE_ACCOUNT_FILE = 'uploaded_keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1acACUFT_ZRgFKQpkA-HOO4KjBhaYvm8xQCkuJHTKzy8'

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range='A1', valueInputOption='USER_ENTERED',body ={'values':data}).execute()

upload_spreadsheets(get_mark_xml())

