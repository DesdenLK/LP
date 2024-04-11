evalua_operacio:: [String] -> [Int] -> Either String Int
evalua_operacio [] [v] = Right v
evalua_operacio [] l = Right (head l)
evalua_operacio (x:xs) pila
    | x == "+" = evalua_operacio xs (exec_op "suma" pila)
    | x == "-" && (head $ tail pila) < (head pila) = Left "neg"
    | x == "-" = evalua_operacio xs (exec_op "resta" pila)
    | x == "*" = evalua_operacio xs (exec_op "mult" pila)
    | x == "/" && head pila == 0 = Left "div0"
    | x == "/" && mod (head $ tail pila) (head pila) /= 0 = Left "divE"
    | x == "/" = evalua_operacio xs (exec_op "div" pila)
    | otherwise = evalua_operacio xs ([read x] ++ pila)

exec_op:: String -> [Int] -> [Int]
exec_op operacio (x:y:pila)
    | operacio == "suma" = [(y+x)] ++ pila
    | operacio == "resta" = [(y-x)] ++ pila
    | operacio == "mult" = [(y*x)] ++ pila
    | operacio == "div" = [(y `div` x)] ++ pila

ev_linia:: String -> Either String Int
ev_linia linea = evalua_operacio (words linea) []


main:: IO()
main = do
    content <- getContents
    let t = map ev_linia (lines content)
    mapM_ (putStrLn . show) t