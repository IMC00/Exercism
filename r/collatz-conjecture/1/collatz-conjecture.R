collatz_step_counter <- function(nums) {
  if(any(nums < 1)) stop("All numbers in the vector must be greater than or equal to 1")
  
  sapply(nums, function(num) {
    steps <- 0
    res <- num
    while(res != 1){
      if(res %% 2 == 0){
        res <- res / 2
      } else {
        res <- 3*res + 1
      }
      steps <- steps + 1
    }
    steps
  })
}
