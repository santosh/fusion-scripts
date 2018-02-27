# increment version and save
# expects vXXX where X is an int
import sys
import os
# comp/composition and fu/fusion are availabe under fusion

file_ = "C:\\Users\\Santosh Kumar\\Desktop\\Iqra Digital Art\\Iqra_Digital_Art_v001.comp"
basename = os.path.basename(file_) # get only filename with extension
filename = os.path.splitext(basename)[0] # remove the extension
basenameWithoutVersion = '_'.join(filename.split('_')[:-1])

getFileVersion = filename.split('_')[-1] # get the vXXX part
prevVersion = int(getFileVersion[1:]) # remove v
newFileVersion = 'v' + str(prevVersion + 1).zfill(3) # increment

newFileName = '_'.join([basenameWithoutVersion, newFileVersion])

# save(newFileName)

def increment_file_version(compfile): # decide if .comp extension is trimmed separately
    """Increment file version given the comp file ending with vXXX.

    :param compfile: comp file
    :return: incremented file version name
    """
    pass
