import os
import git

def get_headings(lines):
  headings = []
  for i, line in enumerate(lines, 1):
    if line.startswith('*'):
      headings.append((i, line))
  return headings


def make_node_from_file(filename):
  with open(filename) as f:
    lines = f.readlines()
  
  format_line = lambda i, line: f"{i:{max_digit_len}}: {line}"
  max_digit_len = len(str(len(lines)))  
  
  headings = [(0, filename + '\n')] + get_headings(lines)
  
  for h in headings:
    print(format_line(*h), end="")


def main():
  os.chdir('../notes')
  g = git.cmd.Git('.')
  print(os.getcwd())
  g.pull()
  make_node_from_file('current.org')
    

if __name__ == '__main__':
  main()