import papermill as pm
import os
from flask import Flask, request, jsonify
from googleapiclient.discovery import build
import google.auth
from googleapiclient.http import MediaIoBaseDownload
import io
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_notebook():
    try:
        json_data = request.get_json(silent=True)
        if json_data:
            start_date = json_data.get('start_date')
            end_date = json_data.get('end_date')
        else:
            # Fallback to get data from URL parameters
            start_date = request.args.get('start_date')
            end_date = request.args.get('end_date')

    except Exception as e:
        return jsonify({'error': f'Failed to process request: {e}'}), 400

    # The file ID for your notebook. Double-check this from your URL.
    file_id = '1ovjKbDkV7XDS7yD6CKXcu-iNPSp4czDR'
    output_name = 'output.ipynb'
    local_notebook_path = '/tmp/downloaded_notebook.ipynb'
    output_path = f'/tmp/{output_name}'

    try:
        # Authenticate with Google Drive API
        creds, project = google.auth.default()
        service = build('drive', 'v3', credentials=creds)

        # Download the notebook from Google Drive using the file ID
        request_drive = service.files().get_media(fileId=file_id)
        fh = io.FileIO(local_notebook_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request_drive)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
    except Exception as e:
        # If the download fails, print a specific error message
        return jsonify({'error': f'An error occurred while downloading the file: {e}'}), 500

    try:
        # Execute the downloaded notebook with papermill
        pm.execute_notebook(
            local_notebook_path,
            output_path,
            parameters={
                'start_date': start_date,
                'end_date': end_date
            }
        )
        # Load the output file and return its contents
        with open('/tmp/final_data.json', 'r') as f:
            output_data = json.load(f)
        
        return jsonify({'data': output_data}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred during papermill execution: {e}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))