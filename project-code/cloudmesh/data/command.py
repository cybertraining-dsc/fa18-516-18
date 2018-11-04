"""Data Manager.

Usage:
  cm4 data add FILE
  cm4 data add SERVICE FILE
  cm4 data get FILE
  cm4 data get FILE DEST_FOLDER
  cm4 data del FILE
  cm4 data (ls | dir)
  cm4 set cloud=CLOUD
  cm4 set group=GROUP
  cm4 set role=ROLE
  cm4 set host=HOSTNAME
  cm4 set cluster=CLUSTERNAME
  cm4 set experiment=EXPERIMENT
  cm4 (-h | --help)
  cm4 --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --config      Location of a cmdata.yaml file
  --vm_list=<list_of_vms>  List of VMs separated by commas ex: node-1,node-2

Description:
   put a description here

Example:
   put an example here
"""
from docopt import docopt


def main():
    """
    Main function for the Vagrant Manager. Processes the input arguments.
    """
    version = 1.0
    arguments = docopt(__doc__, version=version)
    if arguments['data'] and arguments['add']:
        file = arguments['FILE']
        print('Hello', file)


if __name__ == "__main__":
    main()