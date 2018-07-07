import os
import difflib
import json

from typing import List
from .node import fold
from .parse import unshow

def get_headings(lines) -> List[dict]:
  headings = []
  for i, line in enumerate(lines, 1):
    if line.startswith('*'):
      stars, heading = line.split(' ', 1)
      headings.append({'l': len(stars), 'i': i, 'v': heading[:-1]})

  return headings


def parse_dir(dirname):
  assert os.path.isdir(dirname), dirname + ' is not a directory in ' + os.getcwd()
  
  nodes = []
  for filename in os.listdir(dirname):
    # path = os.path.join(dirname, filename)
    path = dirname + '/' + filename

    if os.path.isfile(path):
      nodes.append(parse_file(path))

    elif os.path.isdir(path):
      nodes.append(parse_dir(path))
    
    else:
      return {'error': path + " is neither file nor directory in " + os.getcwd()}
      # with open(path) as f:
        # nodes.append({'v': filename, 'i': 0, 'c': [], 't': f.readlines()})
  
  return {'v': dirname + '/', 'i': 0, 'c': nodes, 't': []}
  

def parse_file(path):
  assert os.path.isfile(path), path + ' is not a file in ' + os.getcwd()

  with open(path) as f:
    lines = f.readlines()
  
  filename = path.rsplit('/', 1)[1]

  headings = [{'l': 0, 'i': 0, 'v': filename}] + get_headings(lines)
  tree = unshow(headings)

  areas = get_areas(tree, lines)
  for area, node in zip(areas, fold(tree)):
    begin, end = area
    node['t'] = lines[begin:end - 1]
  
  for node in fold(tree):
    del node['i']
    
  return tree


def pathify(node, path=""):
  if not path.endswith('/'):
    path += '/'
  mypath = path + node['v']
  node['path'] = mypath
  for c in node['c']:
    pathify(c, mypath)
  return node


def levelify(node, l=0):
  node['l'] = l
  for c in node['c']:
    levelify(c, l+1)
  return node


def get_areas(tree, lines):
  line_numbers = [t['i'] for t in fold(tree)]
  line_areas = list(zip(line_numbers, line_numbers[1:])) + [(line_numbers[-1], len(lines))]
  return line_areas


