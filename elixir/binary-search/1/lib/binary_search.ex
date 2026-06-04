defmodule BinarySearch do
  @doc """
    Searches for a key in the tuple using the binary search algorithm.
    It returns :not_found if the key is not in the tuple.
    Otherwise returns {:ok, index}.
  """

  @spec search(tuple, integer) :: {:ok, integer} | :not_found
  def search(numbers, key) do
    search(numbers, key, 0, tuple_size(numbers) - 1)
  end

  defp search(_numbers, _key, left, right) when left > right do
    :not_found
  end

  defp search(numbers, key, left, right) do
    mid = div(left + right, 2)
    value = elem(numbers, mid)

    cond do
      value == key -> {:ok, mid}
      value < key -> search(numbers, key, mid + 1, right)
      value > key -> search(numbers, key, left, mid - 1)
    end
  end
end
