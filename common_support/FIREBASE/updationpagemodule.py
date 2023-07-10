import threading
import requests
from datetime import timezone, datetime
import os
import sys
import zipfile
import urllib.request
import platform
from time import sleep
from shutil import move, rmtree
from firebase_admin import storage

from common_support.FIREBASE.firebase_initializer import initialize_app

version = "0"
if os.getenv("lazafron_version"):
    version = os.getenv("lazafron_version")


def check_for_updates_clicked():
    down = threading.Thread(name='scanning', target=lambda: upgrade_function())
    down.start()

# C:\LAZAFRON\CLIENT APPLICATIONS\RASPBERRY\NewLayout\packages\FIREBASE\update\updationpagemodule.py


def upgrade_function():
    # Check for internet connection
    if not check_internet_connection():
        print("No internet connection. Cannot check for upgrades.")
        return

    # Initialize the app
    initialize_app()

    # Get the storage bucket
    storage_bucket = storage.bucket()

    # Get the list of files in the upgrades folder
    files = storage_bucket.list_blobs(prefix='win_upgrades/')

    # Iterate over the files
    print("curr version",version)
    for file in files:
        name = str(file.name).rsplit('/', 1)[1]

        # Check if the file is a .zip file
        if not name.endswith(".zip"):
            continue

        try:
            # Extract the version number from the file name
            version_of_file = int(name.split(".", 2)[0])
            print(version_of_file)

            # Compare the version number to the current version number
            if version_of_file > int(version):
                # Generate a signed URL for the file that expires in 1 hour
                curr_time = int(datetime.now(tz=timezone.utc).timestamp())
                generate_signed_url = storage_bucket.blob(file.name).generate_signed_url(expiration=curr_time + 3600)

                # Download and extract the file
                download_and_fetch(generate_signed_url, name)

                # Exit the function
                return

        except Exception as e:
            print(f"Error occured: {e}")


def download_and_fetch(generate_signed_url: str, filename: str) -> None:
    print("Downloading file...")
    urllib.request.urlretrieve(generate_signed_url, filename)
    print("File downloaded.")

    with zipfile.ZipFile(filename) as zip_file:
        zip_file.extractall(path=f"{os.getenv('lazafron_pathtodir')}/targetdir")
    os.remove(filename)

    extracted_folder = filename.split(".")[0]
    extracted_path = f"{os.getenv('lazafron_pathtodir')}/targetdir/{extracted_folder}"
    for src_dir, dirs, files in os.walk(extracted_path):
        dst_dir = src_dir.replace(extracted_path, os.getenv("lazafron_pathtodir"))
        os.makedirs(dst_dir, exist_ok=True)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file) and not os.path.samefile(src_file, dst_file):
                os.remove(dst_file)
            move(src_file, dst_dir)
    rmtree(f"{os.getenv('lazafron_pathtodir')}/targetdir")

    print("Upgraded.")



def check_internet_connection():
    url = "http://www.lazafron.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout,verify=False)
        print("Connected to the Internet")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        return False
