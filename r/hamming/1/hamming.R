# This is a stub function to take two strings
# and calculate the hamming distance
hamming <- function(strand1, strand2) {
  if (nchar(strand1) != nchar(strand2)) stop("Something bad hapened")
  s1 <- unlist(strsplit(strand1, split = ""))
  s2 <- unlist(strsplit(strand2, split = ""))
  length(s1) - sum(nchar(s1[s1==s2]))
}