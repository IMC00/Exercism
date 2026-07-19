defmodule ResistorColorTrio do
  @color_codes %{
    :black => 0,
    :brown => 1,
    :red => 2,
    :orange => 3,
    :yellow => 4,
    :green => 5,
    :blue => 6,
    :violet => 7,
    :grey => 8,
    :white => 9,
  }

  @metric [:ohms, :kiloohms, :megaohms, :gigaohms]

  def add_label(number, unit) do
    if number > 999 do
      add_label(number / 1000, unit+1)
    else
      {number, Enum.at(@metric, unit)}
    end
  end

  @doc """
  Calculate the resistance value in ohms from resistor colors
  """
  @spec label(colors :: [atom]) :: {number, :ohms | :kiloohms | :megaohms | :gigaohms}
  def label([tens, units, magnitude | _]) do
    add_label((10*@color_codes[tens] + @color_codes[units]) * 10**@color_codes[magnitude], 0)
  end
end
