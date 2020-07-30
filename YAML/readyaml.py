#!/usr/bin/env python

#oneliner
#python -c 'import yaml,pprint;pprint.pprint(yaml.load(open(file).read()))'


import yaml
import pprint

fname = raw_input("Enter Filename: ")

fo=open(fname)

print(yaml.load(fo.read()))

