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

#### Create folder
file_metadata = {
    'name': 'Logs',
    'mimeType': 'application/vnd.google-apps.folder'
}
file = drive_service.files().create(body=file_metadata,
                                    fields='id').execute()
print('Folder ID: %s' % file.get('id'))