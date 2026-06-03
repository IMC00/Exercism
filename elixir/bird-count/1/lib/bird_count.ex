defmodule BirdCount do
  @spec today(nonempty_maybe_improper_list()) :: any()
  def today([]), do: nil
  def today([hd | _]), do: hd

  @spec increment_day_count(any()) :: nil
  def increment_day_count([]), do: [1]
  def increment_day_count([hd | tl]), do: [hd + 1 | tl]

  def has_day_without_birds?([0 | _tl]), do: true
  def has_day_without_birds?([_ | tl]), do: has_day_without_birds?(tl)
  def has_day_without_birds?([]), do: false

  def total([hd | tl]), do: hd + total(tl)
  def total([]), do: 0

  def busy_days([]), do: 0
  def busy_days([hd | tail]) when hd > 4, do: 1 + busy_days(tail)
  def busy_days([_hd | tail]), do: busy_days(tail)

end
