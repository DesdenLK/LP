fromStringtoInt :: [String] -> [Int]
fromStringtoInt [] = []
fromStringtoInt (x:xs) = read x : fromStringtoInt xs


main :: IO()
main = do
    contents <- getContents
    let c = sum $ fromStringtoInt $ words contents
    print(c)