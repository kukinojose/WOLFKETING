from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Ruta a tu archivo JSON de credenciales
SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'  # Cambia esto

# ID de la carpeta en Drive donde quieres subir los archivos
FOLDER_ID = '1CSxvKQbTurCAeEhU62mOy-09SkpMQlrF'  # Tu carpeta de Drive

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def upload_file_to_drive(file_path, file_name):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_name,
        'parents': [FOLDER_ID]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'Archivo subido con ID: {file.get("id")}')

if __name__ == '__main__':
    # Ejemplo: subir un archivo local 'venta.mp4' a la carpeta
    upload_file_to_drive('venta.mp4', 'video_venta.mp4')
