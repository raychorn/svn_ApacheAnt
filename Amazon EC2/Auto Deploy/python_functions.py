from pant.pant import ant, target

@target(depends="setup,sourcefile_is_empty,virtualBoxHome_is_empty,sourcefile_does_not_exist,virtualBoxHome_does_not_exist,sourcefile_ext_not_expected")
def pythonTarget():
	"""Python project ptarget"""
	ant.echo("pythonTarget")
	
def str_replace(propname,source,ext,target_ext):
	"""Replace function for strings"""
	ant.echo("(str_replace) :: propname=%s"%(propname))
	ant.echo("(str_replace) :: source=%s"%(source))
	ant.echo("(str_replace) :: ext=%s"%(ext))
	ant.echo("(str_replace) :: target_ext=%s"%(target_ext))
	expected_ext = '.%s'%(ext)
	ant.echo("(str_replace) :: expected_ext=%s"%(expected_ext))
	new_ext = '.%s'%(target_ext)
	ant.echo("(str_replace) :: new_ext=%s"%(new_ext))
	if (source.endswith(expected_ext)):
		ant.property(propname, source.replace(expected_ext,new_ext))
	else:
		ant.property(propname, '*UNDEFINED*')

def normalize(propname,source,target):
	"""Normalizes a source fpath by using the filename part with the target folder name"""
	ant.echo("(normalize) :: propname=%s"%(propname))
	ant.echo("(normalize) :: source=%s"%(source))
	ant.echo("(normalize) :: target=%s"%(target))
	ant.property(propname, source)

def normalize_folder(propname,basedir,target):
	"""Normalizes a target fpath by using the basedir to make the target accessible."""
	import os
	ant.echo("(normalize_folder) :: propname=%s"%(propname))
	ant.echo("(normalize_folder) :: basedir=%s"%(basedir))
	ant.echo("(normalize_folder) :: target=%s"%(target))
	toks = target.split(os.sep)
	toks.insert(0,os.path.dirname(basedir).split(os.sep)[0])
	ant.property(propname, os.sep.join(toks))

def dirname(propname,source):
	"""dirname from an fpath"""
	import os
	ant.echo("(dirname) :: propname=%s"%(propname))
	ant.echo("(dirname) :: source=%s"%(source))
	ant.property(propname, os.path.dirname(source))

def filename(propname,source):
	"""filename from an fpath"""
	import os
	ant.echo("(dirname) :: propname=%s"%(propname))
	ant.echo("(dirname) :: source=%s"%(source))
	ant.property(propname, os.path.basename(source))

def folder_exists(propname,fpath):
	import os
	"""Check to see if a folder exists."""
	ant.echo("(folder_exists) :: propname=%s"%(propname))
	ant.echo("(folder_exists) :: fpath=%s"%(fpath))
	_exists = os.path.exists(fpath)
	ant.echo("(folder_exists) :: _exists=%s"%(_exists))
	ant.property(propname, str(_exists))

def file_exists(propname,fpath):
	folder_exists(propname,fpath)
	
def read_file(propname,filename):
	import os
	"""Check to see if a folder exists."""
	ant.echo("(read_file) :: propname=%s"%(propname))
	ant.echo("(read_file) :: filename=%s"%(filename))
	_exists = os.path.exists(filename)
	ant.echo("(read_file) :: _exists=%s"%(_exists))
	if (_exists):
		fhand = open(filename)
		txt = '\n'.join(fhand.readlines())
		fhand.close()
	ant.property(propname, txt)
	