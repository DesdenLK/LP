
calcula :: [String] -> [Int] -> Either String Int
calcula [] [v] = Right v
calcula [] l = Right (head l)
calcula (x:xs) pila
    | x == "+" = calcula xs (exec_op "suma" pila)
    | x == "-" && head pila > (head $ tail pila) = Left "neg"
    | x == "-" = calcula xs (exec_op "resta" pila)
    | x == "*" = calcula xs (exec_op "mult" pila)
    | x == "/" && head pila == 0 = Left "div0"
    | x == "/" && ((head $ tail pila) `mod` head pila) /= 0 = Left "divE"
    | x == "/" = calcula xs (exec_op "div" pila)
    | otherwise = calcula xs ([read x] ++ pila)

exec_op:: String -> [Int] -> [Int]
exec_op operacio (x:y:pila)
    | operacio == "suma" = [(y+x)] ++ pila
    | operacio == "resta" = [(y-x)] ++ pila
    | operacio == "mult" = [(y*x)] ++ pila
    | operacio == "div" = [(y `div` x)] ++ pila

ev_linia :: String -> String
ev_linia w = show (calcula (words w) [])


main :: IO()
main = do
    contents <- getContents
    let c = map ev_linia (lines contents)
    mapM_ putStrLn c