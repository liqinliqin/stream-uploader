from ytupload import Upload
from argparse import ArgumentParser
import os
import ntpath 
if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("--directory", required=True, help="Folder to parse and upload")

	args = parser.parse_args()
	if not os.path.exists(args.directory):
		exit("Please specify a valid folder using the --directory parameter.")
	uploaded = []
	uploaded_files_fn = os.path.join(args.directory,'uploaded_files.txt')
	if os.path.isfile(uploaded_files_fn):
		uploaded_files_file = open(uploaded_files_fn,'a+')
		uploaded = uploaded_files_file.read().splitlines() 
	else:
		uploaded_files_file = open(uploaded_files_fn,'w')
	filenames = [os.path.join(args.directory,fn) for fn in next(os.walk(args.directory))[2]]
	filenames.remove(os.path.join(args.directory,'uploaded_files.txt'))
	for uploaded_fn in uploaded:
		if uploaded_fn in filenames:
			filenames.remove(uploaded_fn)
	for filename in filenames:
		upload_args = { 'file': filename , 'title' : ntpath.basename(filename)[:-4], 'description': None , 'tags' : None , 'category' : None, 'privacyStatus': 'private'}	
		Upload(upload_args)
		uploaded_files_file.write(filename+'\n')

	
	#Upload(args)
