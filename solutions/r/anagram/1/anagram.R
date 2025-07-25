anagram <- function(subject, candidates) {
  sortedSubject <- sort(unlist(strsplit(tolower(subject), split = "")))
  
  result <- sapply(candidates, function(candidate) {
    if(tolower(candidate) == tolower(subject)) return(FALSE)
    sortedCandidate <- sort(unlist(strsplit(tolower(candidate), split = "")))
    identical(sortedCandidate, sortedSubject)
  })
  
  if(length(names(result[result])) == 0) return(c())
  names(result[result])
}
