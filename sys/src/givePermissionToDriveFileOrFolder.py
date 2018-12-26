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

### Set permissions
file_id = '1xGJuzrHZITGOfwhuCT-Okk9UDEUDQhLs'
def callback(request_id, response, exception):
    if exception:
        # Handle error
        print exception
    else:
        print "Permission Id: %s" % response.get('id')

batch = drive_service.new_batch_http_request(callback=callback)
user_permission = {
    'type': 'user',
    'role': 'reader',
    'emailAddress': 'xyz@gmail.com'
}
batch.add(drive_service.permissions().create(
        fileId=file_id,
        body=user_permission,
        fields='id',
))
domain_permission = {
    'type': 'domain',
    'role': 'reader',
    'domain': 'example.com'
}
batch.add(drive_service.permissions().create(
        fileId=file_id,
        body=domain_permission,
        fields='id',
))
batch.execute()
