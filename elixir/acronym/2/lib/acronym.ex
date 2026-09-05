defmodule Acronym do
  @doc """
  Generate an acronym from a string.
  "This is a string" => "TIAS"
  """

  defp remove_non_alpha(string) do
    case Regex.match?(~r/^[[:alnum:]]/, string) do
       false -> remove_non_alpha(String.slice(string, 1..-1//1))
       true -> string
    end
  end

  @spec abbreviate(String.t()) :: String.t()
  def abbreviate(string) do
    String.split(string, [" ", "-"])
    |> Enum.filter(&(&1 != ""))
    |> Enum.map(&remove_non_alpha/1)
    |> Enum.map(&String.capitalize/1)
    |> Enum.reduce("", fn x, acc -> acc <> String.at(x, 0)  end)
  end
end
