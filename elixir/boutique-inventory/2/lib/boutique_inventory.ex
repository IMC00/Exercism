defmodule BoutiqueInventory do
  def sort_by_price(inventory), do:
    Enum.sort_by(inventory, & &1.price)


  def with_missing_price(inventory), do:
    Enum.filter(inventory, &(!&1.price))

  def update_names(inventory, old_word, new_word), do:
    Enum.map(inventory, fn x -> Map.update!(x, :name, fn name -> Regex.replace(~r/#{old_word}/, name, new_word)  end)  end)

  def increase_quantity(item, count) do
    updated_quantities = Map.new(item.quantity_by_size, fn {key, value} -> {key, value + count} end)
    %{item | quantity_by_size: updated_quantities}
  end

  def total_quantity(item), do:
    Enum.reduce(item[:quantity_by_size], 0, fn {_, value}, acc -> acc + value  end)
end
