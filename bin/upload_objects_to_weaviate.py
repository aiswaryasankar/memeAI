#!/usr/bin/env python3

"""
Upload images to weaviate

Copied from https://github.com/weaviate/weaviate-examples/blob/main/nearest-neighbor-dog-search/upload-data-objects.py
"""

import os
import json

import re
import weaviate

WEAVIATE_URL = os.getenv('WEAVIATE_URL')
CLIENT_CONFIG = None

if WEAVIATE_URL:
    # If a URL is provided, assume this is our remote instance
    # and check for an access token.
    access_token = os.getenv('ACCESS_TOKEN')
    if not access_token:
        raise ValueError("ACCESS_TOKEN environment variable not set. " \
            "This is needed to log into the Weaviate instance.")
    CLIENT_CONFIG = weaviate.AuthBearerToken(
        access_token=access_token,
        expires_in=300 # this is in seconds, by default 60s
        )
else:
    WEAVIATE_URL = 'http://localhost:8080'

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required for uploading objects to Weaviate")

CLIENT = weaviate.Client(WEAVIATE_URL,
                        auth_client_secret=CLIENT_CONFIG,
                        additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY})

print(f"Connecting to a weaviate instance at the following URL: {WEAVIATE_URL}")

BASE64_SCRAPPED_MEME_DATA_FILE = 'base64_cleaned_scrapped_meme_data.json'

def set_up_batch():
    """
    Prepare batching configuration to speed up deleting and importing data.
    """

    CLIENT.batch.configure(
        batch_size=10, 
        dynamic=True,
        timeout_retries=3,
        callback=None
        )
    
def delete_memes():
    """
    Remove all objects from the Memes collection.
    This is useful if we want to rerun the import with different memes.
    """

    with CLIENT.batch as batch:
        batch.delete_objects(
            class_name="Meme", 
            where={
                "operator": "NotEqual",
                "path": ["description"],
                "valueText": "x"
            },
            output="verbose")

def import_data():
    """
    Process all images in [base64_images] folder and import
    them into Memes collection
    """

    meme_data = None
    with open(BASE64_SCRAPPED_MEME_DATA_FILE, 'r') as f:
        meme_data = json.load(f)

    with CLIENT.batch as batch:
        # Iterate over all .b64 files in the base64_images folder
        for data in meme_data:
            filepath = data['imageURL']
            with open(filepath, 'r') as file:
                file_lines = file.readlines()

            base64_encoding = " ".join(file_lines)
            base64_encoding = base64_encoding.replace("\n", "").replace(" ", "") 

            # remove .b64 to get the original file name
            image_file = filepath.replace(".b64", "")

            # remove image file extension and swap - for " " to get the breed name
            meme_name = re.sub(".(jpg|jpeg|png)", "", image_file).replace("-", " ")

            # The properties from our schema
            data_properties = {
                'filename': meme_name,
                'filepath': image_file,
                'description': data['memeDescription'],
                'image': base64_encoding
                }

            batch.add_data_object(data_properties, "Meme")

def main():
    """
    Main function
    """

    print("Setting up data batches...")
    set_up_batch()
    
    print("Delete memes from current instance...")
    delete_memes()

    print("Importing data....")
    import_data()

    print("All objects have been uploaded to Weaviate.")

if __name__ == "__main__":
    main()
