from typing import List, Tuple

from .util import span


def unshow(tuples) -> dict:
  return childify(tuples)[0]


def read_dict(d: dict, *ks):
  for k in ks:
    yield d[k]


def childify(headings: List[dict]) -> List[dict]:
  """
  @param dicts: {level, line number, heading}
  """
  if headings == []:
    return []

  # you're the first one in the list (subtree)
  curr_l, curr_i, curr_value = read_dict(headings[0], 'l', 'i', 'v')
  st = headings[1:]
  assert curr_l == 0

  # subtract one from everything after you and anything >= 0 is your child until you hit something that isn't
  pred_st = [dict(d, l=d['l']-1) for d in st]

  # then separate and make the first negative the start
  children, pred_rest = span(lambda x: x['l'] >= 0, pred_st)

  # add one to the rest to parse it in the next childify
  rest = [dict(d, l=d['l']+1) for d in pred_rest]

  # recurse - kasra  
  return [{'v': curr_value, 'i': curr_i, 'c': childify(children)}] + childify(rest)
