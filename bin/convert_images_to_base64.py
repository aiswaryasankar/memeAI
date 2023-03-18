#!/usr/bin/env python3

"""
Convert images to base64 image representation.
Required for storing images in Weaviate.

Copied from https://github.com/weaviate/weaviate-examples/blob/main/nearest-neighbor-dog-search/images-to-base64.py
"""

import os
import json 
import shutil

import pathlib

SCRAPPED_MEME_DATA_FILE = 'cleaned_scrapped_meme_data.json'

def clear_base64_images():
    """
    Clear out `base64_images` directory (if it exists)
    """

    base_folder = "base64_images"

    # if the base64_images folder => delete it 
    if os.path.exists(base_folder):
        shutil.rmtree(base_folder)
    
    # create the base64_images folder
    os.mkdir(base_folder)  


def convert_images_to_base64():
    """
    Read in meme data and convert images to base64
    """

    meme_data = None
    with open(SCRAPPED_MEME_DATA_FILE, 'r') as f:
        meme_data = json.load(f)

    updated_meme_data = []

    for data in meme_data:
        filepath = data['imageURL']
        if ".DS_Store" not in filepath:
            filename = pathlib.Path(filepath).stem
            base64_filename = f"base64_images/{filename}.b64"
            os.system(f"cat {filepath} | base64 > {base64_filename}")
            updated_meme_data.append({
                'imageURL': base64_filename,
                'memeDescription': data['memeDescription']
                })

    with open(f"base64_{SCRAPPED_MEME_DATA_FILE}", 'w') as f:
        json.dump(updated_meme_data, f, indent=4)


def main():
    """
    Main function
    """

    clear_base64_images()

    print("Converting images to base64...")
    convert_images_to_base64()

    print("The images have been converted to base64.")


if __name__ == '__main__':
    main()
