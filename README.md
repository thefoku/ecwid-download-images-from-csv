# ecwid-download-images-from-csv
Python 3 script that downloads images from the exported CSV files from Ecwid store

How to use:

1. Download the latest Python 3 version: https://www.python.org/downloads/    
2. Open the ecwid-download-images-from-csv.py file with Sublime.
3. In row #7 set your CSV file name instead of "example.csv"
4. In row #37, next to columns = set the same number of the “product_media_gallery_image_url” columns. (Example in the file)
5. Save the .py file, and put in this and CSV file in the same directory (folder).
6. Open the Terminal app, and go to the directory with files usng command: `cd`.
7. Run the next commands in Terminal:

/*Install the request module, requires for running the script*/
pip3 install requests

/*Run script */
python3 ecwid-download-images-from-csv.py

After that, in the Terminal window, you'll see the image downloading process, and the “downloaded_images” folder will be created, where all images will be kept.
