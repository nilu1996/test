  File "test.py", line 72, in <module>
    zip_file_path = create_zip_folder(local_logs_path, old_logs)
  File "test.py", line 12, in create_zip_folder
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
NameError: global name 'zipfile' is not defined
