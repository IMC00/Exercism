parse_phone_number <- function(number_string) {
  s1 <- gsub("[^0-9]", "", number_string) 
  s1 <- as.numeric(strsplit(s1, split = "")[[1]]) 
  
  if (s1[1] == 1) s1 <- s1[-1] 
  
  if (length(s1) != 10 || s1[1] < 2 || s1[4] < 2) return(NULL)
  
  result <- paste(s1, collapse = "")
  result
}
