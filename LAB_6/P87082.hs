imc :: [String] -> String
imc (nom:pes:h:llista) = nom ++ ": " ++ index (read pes) (read h)

index:: Float -> Float -> String
index pes h
    | (pes / (h * h)) < 18 = "magror"
    | (pes / (h * h)) < 25 = "corpulencia normal"
    | (pes / (h * h)) < 30 = "sobrepes"
    | (pes / (h * h)) < 40 = "obesitat"
    | otherwise = "obesitat morbida"
        


main :: IO()
main = do
    line <- getLine
    if line /= "*" then do
        putStrLn $ imc (words line)
        main
    else 
        return()