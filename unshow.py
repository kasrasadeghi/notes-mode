
class Node:
  def __init__(self, v, i, c):
    self.v = v # heading
    self.i = i # line number
    self.c = c # children
    self.text = ""
  
  def __str__(self):
    return self.str()

  def str(self, l=0):
    heading = l * "  " + self.v + '\n'
    text = "".join(l * "  " + x for x in self.text)
    children = "".join([c.str(l + 1) for c in self.c])
    return heading + text + children

  def make_into_html(self, l=0):
    heading = f"<h{l}>{self.v}</h{l}>\n"
    # <pre>, <p>, <div>, <textarea>
    style = ""#f'style="margin-left:{l*10}px"'
    text = f'<div {style}><pre>{"".join(x for x in self.text)}</pre></div>'
    children = "".join([c.make_into_html(l + 1) for c in self.c])
    return heading + text + children


def unshow(tuples) -> Node:
  # get levels for headers
  tree = childify(tuples)[0]
  return tree


def span(p, l):
  first_bad = len(l) #TODO
  for i, el in enumerate(l):
    if not p(el):
      first_bad = i
      break
  return l[:first_bad], l[first_bad:]


def childify(tuples):
  """
  @param tuples: (level, line number, heading)
  """
  if tuples == []:
    return []

  # you're the first one in the list (subtree)
  curr_l, curr_i, curr_value = tuples[0]
  st = tuples[1:]
  assert curr_l == 0

  # subtract one from everything after you and anything >= 0 is your child until you hit something that isn't
  pred_st = [(l - 1, i, v) for l, i, v in st]

  # then separate and make the first negative the start
  children, pred_rest = span(lambda x: x[0] >= 0, pred_st)

  # add one to everything again to get it back to normal
  rest = [(l + 1, i, v) for l, i, v in pred_rest]

  # recurse - kasra  
  return [Node(curr_value, curr_i, childify(children))] + childify(rest)