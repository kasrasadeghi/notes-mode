import os
import difflib

import org_parser

def output_diff():
  with open('current.org') as x:
    with open('current_out.org') as y:
      with open('diff.html', 'w+') as outfile:
        xs, ys = x.readlines(), y.readlines()
        
        # max_line_length = max(len(l) for l in xs + ys)
        differ = difflib.HtmlDiff(tabsize=2, wrapcolumn=100)
        html = differ.make_file(xs, ys)
        outfile.write(html)

def main():
  print('parsing', os.getcwd())
  tree = org_parser.parse_file('current.org')
  with open('current_out.org', "w+") as f:
    f.write(tree.org())
  # with open('notes.html', "w+") as f:
    # f.write(tree.make_into_html())
  
  from pprint import pprint
  pprint(tree.json())

  output_diff()
    

if __name__ == '__main__':
  main()