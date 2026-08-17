defmodule Bob do
  @spec question?(binary()) :: boolean()
  def question?(input), do:
    String.at(input, -1) == "?"

  @spec yelling?(binary()) :: boolean()
  def yelling?(input), do:
    String.upcase(input) == input and String.downcase(input) != input

  @spec silence?(any()) :: boolean()
  def silence?(""), do: true
  def silence?(_), do: false

  @spec hey(String.t()) :: String.t()
  def hey(input) do
    trimmed_input = String.trim(input)
    {question, yelling, silence} = {question?(trimmed_input), yelling?(trimmed_input), silence?(trimmed_input)}
    IO.inspect({question, yelling, silence})
    case {question, yelling, silence} do
      {_, _, true} -> "Fine. Be that way!"
      {true, true, _} -> "Calm down, I know what I'm doing!"
      {true, false, _} -> "Sure."
      {false, true, _} -> "Whoa, chill out!"
      {_, _, _} -> "Whatever."
    end
  end
end
