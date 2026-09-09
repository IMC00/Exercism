defmodule Scrabble do
  @doc """
  Calculate the scrabble score for the word.
  """
  @spec score(String.t()) :: non_neg_integer
  def score(""), do: 0
  def score(word) when word in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], do: 1
  def score(word) when word in ["D", "G"], do: 2
  def score(word) when word in ["B", "C", "M", "P"], do: 3
  def score(word) when word in ["F", "H", "V", "W", "Y"], do: 4
  def score(word) when word in ["K"], do: 5
  def score(word) when word in ["J", "X"], do: 8
  def score(word) when word in ["Q", "Z"], do: 10

  def score(word) do
    word
    |> String.trim
    |> String.capitalize
    |> String.graphemes
    |> Enum.reduce(0, &(score(&1) + &2))
  end
end
