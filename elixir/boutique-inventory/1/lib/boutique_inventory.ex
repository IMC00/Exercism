defmodule BoutiqueInventory do
  def sort_by_price(inventory), do: Enum.sort(inventory, fn x, y -> x[:price] <= y[:price]  end)

  def with_missing_price(inventory), do: Enum.filter(inventory, fn x -> x[:price] == nil  end)

  def update_names(inventory, old_word, new_word), do:
    Enum.map(inventory, fn x -> Map.update!(x, :name, fn name -> Regex.replace(~r/#{old_word}/, name, new_word)  end)  end)

  def increase_quantity(item, count), do:
    Map.update!(item, :quantity_by_size, fn map_qt -> Map.new(Enum.map(map_qt, fn {key, value} -> {key, value + count}  end)) end)

  def total_quantity(item), do:
    Enum.reduce(item[:quantity_by_size], 0, fn {_, value}, acc -> acc + value  end)
end
