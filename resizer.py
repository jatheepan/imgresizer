import os
import sys

from progress.bar import IncrementalBar
from wand.image   import Image

def resize():
  arguments_array  = sys.argv
  if ( len( arguments_array ) < 3 ):
    raise ValueError( 'Required parameters are missing.' )

  source_files_dir = arguments_array[1]
  output_files_dir = arguments_array[2]
  percentage       = float( arguments_array[3] if len( arguments_array ) >= 4 else 25 ) / 100
  files            = os.listdir( source_files_dir )
  bar              = IncrementalBar( 'Resizing', max = len( files ))

  for filename in files:
    if( filename.endswith(('.jpg', '.JPG')) is False ):
      continue

    with Image( filename=os.path.join( source_files_dir, filename )) as img:
      width  = int( img.width * percentage )
      height = int( img.height * percentage )

      with img.clone() as image_clone:
        image_clone.resize( width, height )
        image_clone.save( filename=os.path.join( output_files_dir, filename ))
        bar.next()

  bar.finish()

if __name__ == '__main__':
  resize()
