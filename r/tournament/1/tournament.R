tournament <- function(input) {
  cosa <- strsplit(input, ";") #|> unlist()
  cosa <- cosa[sapply(cosa, (function(x) length(x)==3))]
  teams <- cosa |> sapply((function(x) x[1:2])) |> c() |> unique() |> sort()
  a <- vector( "integer" , 4 ) 
  
  result <- data.frame(Team = teams, MP = c(a), W = c(a), D = c(a), L=c(a), P=c(a))
  rownames(result) <- result$Team
  for(match in cosa){
    if(length(match) != 3) next
    score <- match[3]
    
    if(!(score %in% list("win", "loss", "draw"))) next
    result[match[1], "MP"] <- result[match[1], "MP"] + 1
    result[match[2], "MP"] <- result[match[2], "MP"] + 1
    if(score == "win") {
      result[match[1], "W"] <- result[match[1], "W"] + 1
      result[match[2], "L"] <- result[match[2], "L"] + 1
      
      result[match[1], "P"] <- result[match[1], "P"] + 3
    } else if (score == "loss") {
      result[match[2], "W"] <- result[match[2], "W"] + 1
      result[match[1], "L"] <- result[match[1], "L"] + 1
      
      result[match[2], "P"] <- result[match[2], "P"] + 3     
    } else if (score == "draw"){
      result[match[2], "D"] <- result[match[2], "D"] + 1
      result[match[1], "D"] <- result[match[1], "D"] + 1
      
      result[match[2], "P"] <- result[match[2], "P"] + 1   
      result[match[1], "P"] <- result[match[1], "P"] + 1   
    }
  }
  rownames(result) <- NULL
  
  result <- result[order(result$P, decreasing = TRUE),]
  rownames(result) <- NULL
  result
}
