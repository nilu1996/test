File "upload_s3.py", line 72, in <module>
    zip_file_path = create_zip_folder(local_logs_path, old_logs)
  File "upload_s3.py", line 15, in create_zip_folder
    zipf.write(os.path.join(local_path, file), file)
  File "/usr/lib64/python2.7/zipfile.py", line 824, in __exit__
    self.close()
  File "/usr/lib64/python2.7/zipfile.py", line 1371, in close
    " would require ZIP64 extensions")
zipfile.LargeZipFile: Central directory offset would require ZIP64 extensions
