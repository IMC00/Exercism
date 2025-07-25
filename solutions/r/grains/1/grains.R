square <- function(n) {
  if (min(n) < 1 || max(n) > 64) stop("Something bad hapened")
  2^(n-1)
}

total <- function() {
  sum(square(1:64))
}

