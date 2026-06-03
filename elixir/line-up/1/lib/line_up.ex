defmodule LineUp do
  defp ending_number(number) do
    cond do
      String.ends_with?(number, "1") and not String.ends_with?(number, "11") -> "st"
      String.ends_with?(number, "2") and not String.ends_with?(number, "12") -> "nd"
      String.ends_with?(number, "3") and not String.ends_with?(number, "13") -> "rd"
      true -> "th"
    end
  end

  @doc """
  Formats a full ticket sentence for the given name and number, including
  the person's name, the ordinal form of the number, and fixed descriptive text.
  """
  @spec format(name :: String.t(), number :: pos_integer()) :: String.t()
  def format(name, number) do
    "#{name}, you are the #{Integer.to_string(number) <> ending_number(Integer.to_string(number))} customer we serve today. Thank you!"
  end
end
