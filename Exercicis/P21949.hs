hanoi :: Int -> String -> String -> String -> [(String, String)]
hanoi 0 origen desti auxiliar = []
hanoi 1 origen desti auxiliar = [(origen, desti)]
hanoi n origen desti auxiliar = hanoi (n-1) origen auxiliar desti ++
                                [(origen, desti)] ++
                                hanoi (n-1) auxiliar desti origen

prepareInput :: [String] -> [(String, String)]
prepareInput (c:a1:a2:a3:xs) = hanoi (read c) a1 a2 a3

main ::IO()
main = do
    text <- getContents
    let w = words text
    let c = prepareInput w
    mapM_(\(a,b) -> putStrLn $ a ++ " -> " ++ b) c
