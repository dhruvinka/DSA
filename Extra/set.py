# add(self, object, /)
#  |      Add an element to a set.
#  |
#  |      This has no effect if the element is already present.
#  |
#  |  clear(self, /)
#  |      Remove all elements from this set.
#  |
#  |  copy(self, /)
#  |      Return a shallow copy of a set.
#  |
#  |  difference(self, /, *others)
#  |      Return a new set with elements in the set that are not in the others.
#  |
#  |  difference_update(self, /, *others)
#  |      Update the set, removing elements found in others.
#  |
#  |  discard(self, object, /)
#  |      Remove an element from a set if it is a member.
#  |
#  |      Unlike set.remove(), the discard() method does not raise
#  |      an exception when an element is missing from the set.
#  |
#  |  intersection(self, /, *others)
#  |      Return a new set with elements common to the set and all others.
#  |
#  |  intersection_update(self, /, *others)
#  |      Update the set, keeping only elements found in it and all others.
#  |
#  |  isdisjoint(self, other, /)
#  |      Return True if two sets have a null intersection.
#  |
#  |  issubset(self, other, /)
#  |      Report whether another set contains this set.
#  |
#  |  issuperset(self, other, /)
#  |      Report whether this set contains another set.
#  |
#  |  pop(self, /)
#  |      Remove and return an arbitrary set element.
#  |
#  |      Raises KeyError if the set is empty.
#  |
#  |  remove(self, object, /)
#  |      Remove an element from a set; it must be a member.
#  |
#  |      If the element is not a member, raise a KeyError.
#  |
#  |  symmetric_difference(self, other, /)
#  |      Return a new set with elements in either the set or other but not both.
#  |
#  |  symmetric_difference_update(self, other, /)
#  |      Update the set, keeping only elements found in either set, but not in both.
#  |
#  |  union(self, /, *others)
#  |      Return a new set with elements from the set and all others.
#  |
#  |  update(self, /, *others)
#  |      Update the set, adding elements from all others.
#  |



all methods of dict


# clear(self, /)
#  |      Remove all items from the dict.
#  |
#  |  copy(self, /)
#  |      Return a shallow copy of the dict.
#  |
#  |  get(self, key, default=None, /)
#  |      Return the value for key if key is in the dictionary, else default.
#  |
#  |  items(self, /)
#  |      Return a set-like object providing a view on the dict's items.
#  |
#  |  keys(self, /)
#  |      Return a set-like object providing a view on the dict's keys.
#  |
#  |  pop(self, key, default=<unrepresentable>, /)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |
#  |      If the key is not found, return the default if given; otherwise,
#  |      raise a KeyError.
#  |
#  |  popitem(self, /)
#  |      Remove and return a (key, value) pair as a 2-tuple.
#  |
#  |      Pairs are returned in LIFO (last-in, first-out) order.
#  |      Raises KeyError if the dict is empty.
#  |
#  |  setdefault(self, key, default=None, /)
#  |      Insert key with a value of default if key is not in the dictionary.
#  |
#  |      Return the value for key if key is in the dictionary, else default.
#  |
#  |  update(...)
#  |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
#  |      If E is present and has a .keys() method, then does:  for k in E.keys(): D[k] = E[k]
#  |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#  |      In either case, this is followed by: for k in F:  D[k] = F[k]
#  |
#  |  values(self, /)
#  |      Return an object providing a view on the dict's values.
#  |
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |
#  |  __class_getitem__(object, /)
#  |      See PEP 585
#  |
#  |  fromkeys(iterable, value=None, /)
#  |      Create a new dictionary with keys from iterable and values set to value.