# this is a stub function that takes a natural_number
# and should return the difference-of-squares as described
# in the README.md
difference_of_squares <- function(natural_number) {
  i <- 0
  n1 <- 0
  n2 <- 0
  while(i <= natural_number) {
    n1 <- n1 + i
    n2 <- n2 + i^2
    i <- i + 1
  }
  result <- n1^2-n2
  return(result)
}


