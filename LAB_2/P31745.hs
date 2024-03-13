flatten :: [[Int]] -> [Int]
flatten llistes = foldl (++) [] llistes

myLength :: String -> Int
myLength l = sum $ map (const 1) l


myReverse :: [Int] -> [Int]
myReverse l = foldl (flip(:)) [] l


firstWord :: String -> String
firstWord a = takeWhile (\x -> x /= ' ') $ dropWhile (\x -> x == ' ') a

countIn :: [[Int]] -> Int -> [Int]
countIn lists x = map (countElem x) lists

countElem :: Int -> [Int] -> Int
countElem x = length . filter (== x)


