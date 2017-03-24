from os import listdir
from os.path import isfile, join, isdir
import sys

def dfs_directory(root, filename, depth, formatstring):
    """ Fuction to perform DFS on Directory structure
        params: root: Path of the current subdirectory
                filename: Name of the file to be searched
                depth: Remaining depth to be explored
                formatstring: For pretty output
    """

    """Terminate search if depth is exceeded"""

    files = [f for f in listdir(root) if isfile(join(root, f))]
    files.sort()

    for f in files:
        print formatstring + "File: " + f

    """Terminal test: Test all the files for checking whether the reuqired file is found."""
    for f in files:
        if f == filename:
            return join(root, f), True

    if depth == 0:
        return None, False

    directories = [d for d in listdir(root) if isdir(join(root, d))]
    directories.sort()

    for d in directories:
        new_path = join(root, d)
        print formatstring + "Folder: " + d
        file_path, result = dfs_directory(new_path, filename, depth - 1, "|   " + formatstring)
        if result == True:
            return file_path, result

    return None, False

def iddfs_directory(root, filename, depth, formatstring):
    """ Fuction to perform ID-DFS on Directory structure
        params: root: Path of the current subdirectory
                filename: Name of the file to be searched
                depth: Remaining depth to be explored
                formatstring: For pretty output
    """

    for current_depth in xrange(depth+1):
        print "\nCurrent depth cut-off %d\n" % (current_depth)
        print "Root Directory: %s" % (root_path)
        file_path, result = dfs_directory(root_path, search_name, current_depth, formatstring)
        if result == True:
            return file_path, result, current_depth

    return None, False, depth

if __name__ == '__main__':
    argument_list = sys.argv
    search_depth  = int(argument_list[1])
    search_name = argument_list[2]
    root_path = argument_list[3]
    formatstring = "|-- "

    file_path, result, file_depth = iddfs_directory(root_path, search_name, search_depth, formatstring)
    if result == False:
        print "\nNo file found till folder depth %d" % (search_depth)
    else:
        print "\nFile found at path \"%s\" and depth %d\n" % (file_path, file_depth)
