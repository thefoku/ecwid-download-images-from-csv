# ecwid-download-images-from-csv
Python 3 script that downloads images from the exported CSV files from Ecwid store

**How to use:**

First, we need to export the CSV file with your products:

1. Go to **Ecwid > Catalog > Products**.
2. Click **Mass Update > Export > Export All**.
3. Select where to save the file on your device.

After these steps, you'll get the CSV file with image links for the Python script to download them.

Next, let's prepare the Python script file, and run it:

1. Download the latest Python 3 version: https://www.python.org/downloads/    
2. Open the ecwid-download-images-from-csv.py file with Sublime Text.
3. In row #7 set your CSV file name instead of "example.csv"
4. In row #37, next to columns = set the same number of the “product_media_gallery_image_url” columns. (Example in the file)
5. Save the .py file, and put it and the CSV file in the same directory (folder).
6. Open the Terminal app, and go to the directory with files using the command: `cd`.
7. Run the next commands in Terminal:

/* Install the request module, required for running the script */

**pip3 install requests**

/*Run script */

**python3 ecwid-download-images-from-csv.py**

After that, in the Terminal window, you'll see the image downloading process, and the “downloaded_images” folder will be created, where all images will be kept.
