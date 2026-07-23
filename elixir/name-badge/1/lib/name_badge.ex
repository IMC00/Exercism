defmodule NameBadge do
  def print(id, name, department) do
    # if id do
    #   "[#{id}] - #{name} - #{String.upcase(department)}"
    # else
    #   if department do
    #     "#{name} - #{String.upcase(department)}"
    #   else
    #     "#{name} - OWNER"
    #   end
    # end
    "#{if id, do: "[#{id}] - " , else: ""}#{name} - #{if department, do: String.upcase(department), else: "OWNER"}"
    end
  end
