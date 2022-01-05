import ezsheets
import sys

file_name = sys.argv[1]

gs = ezsheets.upload(file_name)
url = gs.url
to_download = ezsheets.Spreadsheet(url)
to_download.downloadAsCSV()
