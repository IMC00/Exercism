defmodule KitchenCalculator do
  @spec get_volume({any(), any()}) :: any()
  def get_volume({_, amount}), do: amount

  @spec to_milliliter(
          {:cup, number()}
          | {:fluid_ounce, number()}
          | {:milliliter, number()}
          | {:tablespoon, number()}
          | {:teaspoon, number()}
        ) :: {:milliliter, number()}
  def to_milliliter({:milliliter, amount}), do: {:milliliter, 1 * amount}
  def to_milliliter({:cup, amount}), do: {:milliliter, 240* amount}
  def to_milliliter({:fluid_ounce, amount}), do: {:milliliter, 30 * amount}
  def to_milliliter({:teaspoon, amount}), do: {:milliliter, 5  * amount}
  def to_milliliter({:tablespoon, amount}), do: {:milliliter, 15 * amount}



  def from_milliliter({:milliliter, amount}, :milliliter), do: {:milliliter, amount}
  def from_milliliter({:milliliter, amount}, :cup), do: {:cup, amount / 240}
  def from_milliliter({:milliliter, amount}, :fluid_ounce), do: {:fluid_ounce, amount / 30}
  def from_milliliter({:milliliter, amount}, :teaspoon), do: {:teaspoon, amount / 5}
  def from_milliliter({:milliliter, amount}, :tablespoon), do: {:tablespoon, amount / 15}


  def convert(volume_pair, unit), do: from_milliliter(to_milliliter(volume_pair), unit)
end
