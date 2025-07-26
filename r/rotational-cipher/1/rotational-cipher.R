auxFunction <- function(x, key){
  res <- x
  if(res > 64 &&  res < 91){
    res <- res + key
    if(res > 90) res <- res-26
  } else if (res > 96 &&  res < 123) {
    res <- res + key
    if(res > 122) res <- res-26
  }
  return(res)
}

rotate <- function(text, key) {
  rotateWithKey <- function(x) auxFunction(x, key)
  utf8ToInt(text) |> sapply(rotateWithKey) |> intToUtf8()
}