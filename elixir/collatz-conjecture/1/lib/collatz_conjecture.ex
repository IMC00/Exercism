defmodule CollatzConjecture do

  defp aux_calc({1, steps}), do: {1, steps}
  defp aux_calc({n, steps}) when rem(n, 2) == 0, do: aux_calc({div(n, 2), steps + 1})
  defp aux_calc({n, steps}) when rem(n, 2) == 1, do: aux_calc({3*n+1, steps + 1})

  @doc """
  calc/1 takes an integer and returns the number of steps required to get the
  number to 1 when following the rules:
    - if number is odd, multiply with 3 and add 1
    - if number is even, divide by 2
  """
  @spec calc(input :: pos_integer()) :: non_neg_integer()
  def calc(n) when n > 0 do
    {1, res} = aux_calc({n, 0})
    res
  end

end
