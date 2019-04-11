import os
import sys

descriptor = """This is a tool that creates a replca of a given file structure in a new location. All the files are empty/zero copies. It is a useful and fast way of making a very portable copy of a file system to help arrangement planning and other analysis"""


def main(argv=None):

	if argv:
		input_folder = argv[0]
		output_folder = argv[1]
	else:	
  
    ### edit here for your input folder"""
		input_folder = r"W:\Who Slapped John"
		
    ### edit here for your output folder"""
    output_folder = r"junk"

	file_list = []

	folder_counter = 0
	files_counter = 0
  
	for root, subs, fs in os.walk(input_folder):
		for s in subs:
			new_s = os.path.join(root, s).replace(input_folder, output_folder)
      ### checking step to make sure we can't over write the original by accident
			if new_s != os.path.join(root, s):
				folder_counter += 1
				try:
					os.makedirs(new_s)
				except FileExistsError:
					pass

		for f in fs:
			new_f = os.path.join(root, f).replace(input_folder, output_folder)
      ### checking step to make sure we can't over write the original by accident
			if new_f != os.path.join(root, f):
				with open(new_f, 'wb') as data:
					files_counter +=1

	
	print (f'Copying from "{input_folder}"')
	print (f'To "{output_folder}"')
	print (f"Made {folder_counter} folders ")
	print (f"Made {files_counter} folders ")


if __name__ == '__main__':
	main(sys.argv[1:])
