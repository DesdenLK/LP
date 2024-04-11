i2s :: String -> Int
i2s w = read w

main :: IO()
main = do
    contents <- getContents
    let c = sum $ map i2s (words contents)
    print(c)