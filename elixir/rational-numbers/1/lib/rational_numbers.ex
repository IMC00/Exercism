defmodule RationalNumbers do
  @type rational :: {integer, integer}

  @doc """
  Add two rational numbers
  """
  @spec add(a :: rational, b :: rational) :: rational
  def add({an, ad}, {bn, bd}), do: reduce({an * bd + bn * ad, ad * bd})

  @doc """
  Subtract two rational numbers
  """
  @spec subtract(a :: rational, b :: rational) :: rational
  def subtract({an, ad}, {bn, bd}), do: add({an, ad}, {-bn, bd})

  @doc """
  Multiply two rational numbers
  """
  @spec multiply(a :: rational, b :: rational) :: rational
  def multiply({an, ad}, {bn, bd}), do: reduce({an * bn, ad * bd})

  @doc """
  Divide two rational numbers
  """
  @spec divide_by(num :: rational, den :: rational) :: rational
  def divide_by({an, ad}, {bn, bd}), do: multiply({an, ad}, {bd, bn})

  @doc """
  Absolute value of a rational number
  """
  @spec abs(a :: rational) :: rational
  def abs({n, d}), do: reduce({Kernel.abs(n), Kernel.abs(d)})

  @doc """
  Exponentiation of a rational number by an integer
  """
  @spec pow_rational(a :: rational, n :: integer) :: rational
  def pow_rational({num, den}, n) when n < 0, do: pow_rational({den, num}, -n)
  def pow_rational({num, den}, n), do: reduce({num ** n, den ** n})

  @doc """
  Exponentiation of a real number by a rational number
  """
  @spec pow_real(x :: integer, n :: rational) :: float
  def pow_real(x, {num, den}), do: :math.pow(x, num/den)

  @doc """
  Reduce a rational number to its lowest terms
  """
  @spec reduce(a :: rational) :: rational
  def reduce({n, d}) when d < 0, do: reduce({-n, -d})
  def reduce({n, d}) when d > 0 do
    g = Integer.gcd(n, d)
    {div(n, g), div(d, g)}
  end

end
