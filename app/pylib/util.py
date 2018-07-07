
def span(p, l):
  first_bad = len(l) #TODO
  for i, el in enumerate(l):
    if not p(el):
      first_bad = i
      break
  return l[:first_bad], l[first_bad:]