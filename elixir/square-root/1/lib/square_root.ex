defmodule SquareRoot do

  # defp heron(number) do
  #   heron(number, number/2, number)
  # end

  defp heron(est1, est2, _) when abs(est1 - est2) < 0.1, do: round(est2)
  defp heron(_, est2, number), do: heron(est2, (est2 + number/est2)/2, number)
  @doc """
  Calculate the integer square root of a positive integer
  """
  @spec calculate(radicand :: pos_integer) :: pos_integer
  def calculate(radicand) do
      heron(radicand, radicand/2, radicand)
  end
end
