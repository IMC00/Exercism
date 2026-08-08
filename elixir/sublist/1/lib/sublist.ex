defmodule Sublist do
  @doc """
  Returns whether the first list is a sublist or a superlist of the second list
  and if not whether it is equal or unequal to the second list.
  """
  def is_sublist([], _), do: true
  def is_sublist([a | tail1], [a | tail2]), do: is_sublist(tail1, tail2)
  def is_sublist(_, _), do: false

  def is_superlist(list1, list2), do: (if is_sublist(list2, list1), do: true, else: false)

  def compare(list, list), do: :equal
  def compare([_a | tail], tail), do: :superlist
  def compare(tail, [_a | tail]), do: :sublist

  def compare(list1, list2) when length(list1) < length(list2), do:
    (if is_sublist(list1, list2), do: :sublist, else: compare(list1, tl(list2)))
  def compare(list1, list2) when length(list1) > length(list2), do:
    (if compare(list2, list1) == :sublist, do: :superlist, else: compare(tl(list1), list2))
  def compare(_, _), do: :unequal

end
