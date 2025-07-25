word_count <- function(input) {
  words <- gsub("[^0-9a-zA-Z']+", " ", input) |> strsplit(split = " ") |> unlist() |> tolower()
  
  words <- gsub("^'|'$", "", words)

  words <- words[words != ""]

  result <- as.list(table(words))

  return(result)
}
