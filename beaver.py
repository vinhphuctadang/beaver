import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

BEAVER_DIR = os.path.dirname (os.path.realpath (__file__))
BEAVER_TEMPLATE_FOLDER = BEAVER_DIR + '/template/'
NAME_LIMIT = 64
TEMPLATE_LIST = []


# TODO: Cache init
def init ():
	if not os.path.isdir (BEAVER_TEMPLATE_FOLDER):
		os.mkdir (BEAVER_TEMPLATE_FOLDER)
	root, dirs, files = next (os.walk (BEAVER_TEMPLATE_FOLDER))
	TEMPLATE_LIST = files
	pass

def printList ():
	root, dirs, files = next (os.walk (BEAVER_TEMPLATE_FOLDER))
	for file in files:
		print (file)
	print (f'{bcolors.OKGREEN}[SUCCESS] Total {len (files)} template(s) found{bcolors.ENDC}')
'''
	save template src->dst
	where:
		src indicates path/to/src
		dst indicates name of template
'''
def this (src, dest = ''):
	if dest == '':
		dest = os.path.basename (src)
	dest = os.path.basename (dest)

	try:
		f = open (src, 'r', encoding='utf8')
	except Exception as e:
		print (f'{bcolors.FAIL}[ERROR] Cannot open "{src}"{bcolors.ENDC}')
		return
	
	ABS_DEST_PATH = BEAVER_TEMPLATE_FOLDER + dest;
	info = f.read ()
	f.close ()

	if os.path.isfile (ABS_DEST_PATH):
		confirm = input ('There is a template "{}" existed, override [y/n]?'.format (dest))
		if confirm.lower () != 'y':
			print (f'{bcolors.FAIL}[ERROR] No template saved{bcolors.ENDC}')
			return
	try:
		g = open (ABS_DEST_PATH, 'w')
		g.write (str (info))
		g.close ()	
	except Exception as e: 
		print (f'{bcolors.FAIL}[ERROR] Cannot modify {ABS_DEST_PATH}{bcolors.ENDC}')
		return 
	
	print (f'{bcolors.OKGREEN}[SUCCESS] Made template name "{dest}"{bcolors.ENDC}')
	pass

def make (src, dest=''):

	src = os.path.basename (src)
	saved_base_name = src
	if dest == '':
		dest = src
	src = BEAVER_TEMPLATE_FOLDER + src
	
	if len (dest) > NAME_LIMIT:
		print (f'{bcolors.FAIL}[ERROR] Reject to store template having name with more than {NAME_LIMIT} characters{bcolors.ENDC}')
		return
	ABS_DEST_PATH = dest

	try:
		f = open (src, 'r', encoding='utf8')		
	except Exception as e:
		print (f'{bcolors.FAIL}[ERROR] No template named "{saved_base_name}" found {bcolors.ENDC}')
		return
	
	info = f.read ()
	f.close ()
	try:
		g = open (ABS_DEST_PATH, 'a+')
		if (g.tell () > 0):
			g.write ("\n")
		g.write (str (info))
		g.close ()
	except Exception as e:
		print ('[ERROR]', e)
		return
	print (f'{bcolors.OKGREEN}[SUCCESS] File append to "{ABS_DEST_PATH}"{bcolors.ENDC}')

def interface ():
	import argparse
	import sys
	parser = argparse.ArgumentParser()
	parser.add_argument("--list", help='list saved template', action="store_true")
	parser.add_argument("--save", help='store following file as template', action="store_true")
	parser.add_argument('source', type=str, nargs='?', help='source template or source file', default='template')
	parser.add_argument('dest', type=str, nargs='?', help='destination template or destination file', default='code')
	args = parser.parse_args(sys.argv[1:])

	blSave = args.save
	blList = args.list

	if blList:
		printList ()
	elif blSave:
		src  = args.source
		dst  = args.dest
		this (src, dst)
	else:
		src  = args.source
		dst  = args.dest
		make (src, dst)
def main ():
	interface ()
	pass

if __name__ == "__main__":
	init ()
	main ()
	pass