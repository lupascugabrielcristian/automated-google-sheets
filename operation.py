from __future__ import print_function

import os.path
import random

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '[placeholder]'

def get_values(sheet_service, range_name):
    result = sheet_service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    rows = result.get('values', [])
    return rows

# range_name de forma "A1:C2"
# body de forma [['A', 'B'], ['C', 'D']]
def put_values(sheet_service, range_name, values):
    body = { 'values': values }
    result = sheet_service.values().update(spreadsheetId=SPREADSHEET_ID, range=range_name, valueInputOption="USER_ENTERED", body=body).execute()
    return result


# Need to format values such as: [["4"], ["5"], ["6"], ["7"]]
def generate_stock_values(count):
    values = []
    for i in range(count):
        values.append([str( random.randrange(100, 2000) )])
    return values

# Need to format values such as: [["4"], ["5"], ["6"], ["7"]]
def generate_sales_values(count):
    values = []
    for i in range(count):
        values.append([str( random.randrange(10, 300) )])
    return values


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file credentials.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("from_client_secrets")
            flow = InstalledAppFlow.from_client_secrets_file( 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        rows = get_values(sheet, "A1:A5")
        print(f'{len(rows)} rows obtained')

        rows_to_add = 100

        # Day
        days_values = []
        for i in range(rows_to_add):
            days_values.append([ str(i) ])
        put_result = put_values(sheet, "A2:A102", days_values)

        # Stock price values
        stock_values = generate_stock_values(rows_to_add)
        put_result = put_values(sheet, "B2:B102", stock_values)

        # Sales values
        sales_values = generate_sales_values(rows_to_add)
        put_result = put_values(sheet, "C2:C102", sales_values)

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
