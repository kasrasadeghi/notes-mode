import os
from unshow import unshow, Node
import difflib

def get_headings(lines):
  headings = []
  for i, line in enumerate(lines, 1):
    if line.startswith('*'):
      stars, heading = line.split(' ', 1)
      headings.append((len(stars), i, heading[:-1]))

  return headings


def make_node_from_file(filename):
  with open(filename) as f:
    lines = f.readlines()
  
  headings = [(0, 0, filename + '\n')] + get_headings(lines)
  tree = unshow(headings)

  areas = get_areas(tree, lines)
  for area, node in zip(areas, fold(tree)):
    begin, end = area
    node.text = lines[begin:end - 1] # gather_text(begin, end, lines)
    
  return tree


def get_areas(tree, lines):
  line_numbers = [t.i for t in fold(tree)]
  line_areas = list(zip(line_numbers, line_numbers[1:])) + [(line_numbers[-1], len(lines))]
  return line_areas


def fold(tree: Node) -> list:
  l = []
  l.append(tree)
  for c in tree.c:
    l += fold(c)
  return l


def output_diff():
  with open('current.org') as x:
    with open('current_out.org') as y:
      with open('diff.html', 'w+') as outfile:
        xs, ys = x.readlines(), y.readlines()
        
        max_line_length = max(len(l) for l in xs + ys)
        differ = difflib.HtmlDiff(tabsize=2, wrapcolumn=max_line_length)
        html = differ.make_file(xs, ys, context=False)
        outfile.write(html)


def main():
  print(os.getcwd())
  tree = make_node_from_file('current.org')
  with open('current_out.org', "w+") as f:
    f.write(tree.org())
  # with open('notes.html', "w+") as f:
    # f.write(tree.make_into_html())

  output_diff()  
    

if __name__ == '__main__':
  main()