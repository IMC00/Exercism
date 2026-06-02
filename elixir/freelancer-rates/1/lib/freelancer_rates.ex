defmodule FreelancerRates do
  @spec daily_rate(number()) :: float()
  def daily_rate(hourly_rate) do
    hourly_rate * 8.0
  end

  def apply_discount(before_discount, discount) do
    before_discount * (100 - discount) / 100.0
  end

  def monthly_rate(hourly_rate, discount) do
    ceil(apply_discount(22.0 * daily_rate(hourly_rate), discount))
  end

  def days_in_budget(budget, hourly_rate, discount) do
    rate = apply_discount(daily_rate(hourly_rate), discount)
    days = budget / rate

    floor(days * 10) / 10.0
  end
end
