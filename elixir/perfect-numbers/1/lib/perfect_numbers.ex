defmodule PerfectNumbers do
  @doc """
  Determine the aliquot sum of the given `number`, by summing all the factors
  of `number`, aside from `number` itself.

  Based on this sum, classify the number as:

  :perfect if the aliquot sum is equal to `number`
  :abundant if the aliquot sum is greater than `number`
  :deficient if the aliquot sum is less than `number`
  """
  @spec classify(number :: integer) :: {:ok, atom} | {:error, String.t()}
  def classify(number) when number < 1, do: {:error, "Classification is only possible for natural numbers."}


  def classify(number) do
    sum_factors = factors(number)
    cond do
      number == sum_factors -> {:ok, :perfect}
      number < sum_factors -> {:ok, :abundant}
      number > sum_factors -> {:ok, :deficient}

    end
  end

  defp factors(1), do: 0
  defp factors(number) do
    1..number-1
    |> Enum.filter(&(rem(number, &1) == 0))
    |> List.foldr(0, fn x, acc -> acc + x end)
  end

end
