# storage.py

from django.conf import settings
from django.core.files.storage import Storage
from supabase import create_client, Client
import supabase

class SupabaseStorage(Storage):
    def __init__(self, bucket_name="media", **kwargs):
        self.bucket_name = bucket_name

        self.supabase: Client = create_client("https://gfkdddxopclvcurvlvpn.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdma2RkZHhvcGNsdmN1cnZsdnBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA5NjAyODYsImV4cCI6MjAyNjUzNjI4Nn0.gJQhvKiBEFSvhODf8SDk0SXeV1wwDTF_ECDSqYSfV4s"
)
        self.storage_client = self.supabase.storage.from_(self.bucket_name)

    def _open(self, name, mode="rb"):
        # Implement the method to open a file from Supabase
        pass

    def _save(self, name, content):
        # Implement the method to save a file to Supabase
        content_file = content.file
        content_file.seek(0)  # Move the file pointer to the beginning
        content_bytes = content_file.read()
        
        data = self.supabase.from_(self.bucket_name).upload(
            name, content_bytes, {"content-type": content.content_type}
        )
        return data.json()["Key"]  # name/path of the file

    def exists(self, name):
        # Implement the method to check if a file exists in Supabase
        pass

    def url(self, name):
        # Implement the method to return the URL for a file in Supabase
        return f"https://gfkdddxopclvcurvlvpn.supabase.co/storage/v1/object/public/{name}"