### Install
pyenv virtualenv 3.8.0 google-sheets  
pyenv activate google-sheets  
pip install --upgrade pip  
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  

[!] Ca sa mearga, a trebuit sa pun contul de google cu care ma loghez, la Test users

### Preparation
1. Create a Google project  
2. Enable GoogleSheets API
3. Create OAuth 2.0 Client IDs and obtain credentials json file. The file must be saved in the same folder as the project with the name "credentials.json"
4. In order for the scrip to work the SPREADSHEET_ID variable needs to filled in.  
5. credentials.json file must be downloaded from the Google Sheets API from Google Console  
6. Screen authentication must be passed  
