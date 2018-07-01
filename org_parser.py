import os
import difflib
import json

from node import Node
from parse import unshow

def get_headings(lines):
  headings = []
  for i, line in enumerate(lines, 1):
    if line.startswith('*'):
      stars, heading = line.split(' ', 1)
      headings.append((len(stars), i, heading[:-1]))

  return headings


def parse_file(filename):
  with open(filename) as f:
    lines = f.readlines()
  
  headings = [(0, 0, filename + '\n')] + get_headings(lines)
  tree = unshow(headings)

  areas = get_areas(tree, lines)
  for area, node in zip(areas, tree.fold()):
    begin, end = area
    node.text = lines[begin:end - 1] # gather_text(begin, end, lines)
    
  return tree


def get_areas(tree, lines):
  line_numbers = [t.i for t in tree.fold()]
  line_areas = list(zip(line_numbers, line_numbers[1:])) + [(line_numbers[-1], len(lines))]
  return line_areas


