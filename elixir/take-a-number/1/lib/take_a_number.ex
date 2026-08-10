defmodule TakeANumber do

  def loop(state \\ 0) do
    receive do
      {:report_state, pid} ->
        send(pid, state)
        loop(state)
      {:take_a_number, pid} ->
        send(pid, state+1)
        loop(state+1)
      :stop ->
        -1
      _ ->
        loop(state)
    end
  end

  def start() do
    spawn(fn -> loop() end)
  end
end
