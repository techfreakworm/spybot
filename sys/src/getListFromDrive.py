import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload 
from google.oauth2 import service_account
from httplib2 import Http
import sys

SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = '/opt/sys/src/spyer-techfreak-a4558b616283.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

##### Get list of files
results = drive_service.files().list(pageSize=10, fields="nextPageToken, files(id, name,webViewLink,permissionIds)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print('{0} {1} {2} {3}'.format(item['name'], item['id'], item['webViewLink'], item['permissionIds']))
