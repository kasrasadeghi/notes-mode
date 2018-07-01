from typing import List, Tuple

from util import span
from node import Node


def unshow(tuples) -> Node:
  return childify(tuples)[0]


def childify(tuples: List[Tuple[int, int, str]]) -> List[Node]:
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