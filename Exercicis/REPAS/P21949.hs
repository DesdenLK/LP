torres :: Int -> [String] -> [(String, String)]
torres 0 _ = []
torres n (origen:desti:auxiliar:p) =
    torres (n-1) (origen:auxiliar:desti:p) ++
    [(origen, desti)] ++
    torres (n-1) (auxiliar:desti:origen:p)


main :: IO()
main = do
    input <- getLine
    let c = torres (read $ head $ words input) (tail $ words input)
    mapM_ (\(x,y) -> putStrLn $ x ++ " -> " ++ y) c
    