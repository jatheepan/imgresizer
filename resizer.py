import os
import sys

from progress.bar import IncrementalBar
from wand.image   import Image

arguments_array  = sys.argv
if ( len( arguments_array ) < 3 ):
  raise ValueError( 'Required parameters are missing.' )

source_files_dir = arguments_array[1]
output_files_dir = arguments_array[2]
files            = os.listdir( source_files_dir )
bar              = IncrementalBar( 'Resizing', max = len( files ) )

for filename in files:
  with Image( filename=source_files_dir + '/' + filename ) as img:
    width  = int( img.width * 0.25 )
    height = int( img.height * 0.25 )

    with img.clone() as image_clone:
      image_clone.resize( width, height )
      image_clone.save( filename=output_files_dir + '/' + filename + ''.format( img ) )
      bar.next()
bar.finish()
