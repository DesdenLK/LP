getOutput :: String -> String
getOutput nom
    | (head $ reverse nom) == 'a' = "Hola maca!"
    | (head $ reverse nom) == 'A' = "Hola maca!"
    | otherwise = "Hola maco!"


main :: IO()
main = do
    nom <- getLine
    let t = getOutput nom
    putStrLn t
