
class Node:
  def __init__(self, v, i, c, text=[]):
    self.v = v # heading
    self.i = i # line number
    self.c = c # children
    self.text = text
  
  def __str__(self):
    return self.str()

  def str(self, l=0):
    heading = l * "  " + self.v + '\n'
    text = "".join(l * "  " + x for x in self.text)
    children = "".join([c.str(l + 1) for c in self.c])
    return heading + text + children

  def html(self, l=0):
    heading = f"<h{l}>{self.v}</h{l}>\n"
    # <pre>, <p>, <div>, <textarea>
    style = ""#f'style="margin-left:{l*10}px"'
    text = f'<div {style}><pre>{"".join(x for x in self.text)}</pre></div>'
    children = "".join([c.make_into_html(l + 1) for c in self.c])
    return heading + text + children
  
  def json(self, l=0):
    d = {
      'heading': self.v,
      'text': self.text,
      'children': [c.json(l + 1) for c in self.c]
    }

    return d
  
  def org(self, l=0):
    heading = l * "*" + " " + self.v + '\n'
    text = "".join(self.text)
    children = "".join([c.org(l + 1) for c in self.c])
    return heading + text + children

  def fold(self) -> list:
    l = []
    l.append(self)
    for c in self.c:
      l += c.fold()
    return l

