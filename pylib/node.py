
def html(d, l=0):
  heading = f"<h{l}>{d['v']}</h{l}>\n"
  # <pre>, <p>, <div>, <textarea>
  style = ""#f'style="margin-left:{l*10}px"'
  text = f"<div {style}><pre>{''.join(x for x in d['t'])}</pre></div>"
  children = "".join([c.make_into_html(l + 1) for c in d['c']])
  return heading + text + children


def str(d, l=0):
    heading = l * "  " + d['v'] + '\n'
    text = "".join(l * "  " + x for x in d['t'])
    children = "".join([c.str(l + 1) for c in d['c']])
    return heading + text + children


def org(d, l=0):
  heading = l * "*" + " " + d['v'] + '\n'
  text = "".join(d['t'])
  children = "".join([org(c, l + 1) for c in d['c']])
  return heading + text + children


def fold(d) -> list:
    l = []
    l.append(d)
    for c in d['c']:
      l += fold(c)
    return l