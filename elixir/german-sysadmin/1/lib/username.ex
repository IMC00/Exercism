defmodule Username do
  def sanitize(username) do
    # ä becomes ae
    # ö becomes oe
    # ü becomes ue
    # ß becomes ss

    # Please implement the sanitize/1 function
    case username  do
      ~c"" -> ~c""
      [?ä | rest] -> ~c"ae" ++ sanitize(rest)
      [?ö | rest] -> ~c"oe" ++ sanitize(rest)
      [?ü | rest] -> ~c"ue" ++ sanitize(rest)
      [?ß | rest] -> ~c"ss" ++ sanitize(rest)
      [head | tail] when head in ~c"qwertyuiopasdfghjklzxcvbnm_" -> [head] ++ sanitize(tail)
      _ -> sanitize(tl(username))
    end
  end
end

# Username.sanitize(~c"öoqweqweqwe")
