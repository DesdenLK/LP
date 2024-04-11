myLength :: [Int] -> Int
myLength [] = 0
myLength (_:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum n = maximum n

average :: [Int] -> Float
average n = fromIntegral(sum(n) `div` length n)

buildPalindrome :: [Int] -> [Int]
buildPalindrome llista = reverse(llista)  ++ llista

remove :: [Int] -> [Int] -> [Int]
remove [] y = []
remove x [] = x
remove (p:xs) y
    | elem p y = [] ++ remove xs y
    | otherwise = [p] ++ remove xs y

flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ flatten xs

primeDivisors :: Int -> [Int]
primeDivisors n
    | n <= 1 = []
    | isPrime n = [n]
    | otherwise = getDivisors n [2 .. div n 2]

getDivisors :: Int -> [Int] -> [Int]
getDivisors _ [] = []
getDivisors n (p:xs)
    | null xs && isPrime p && mod n p == 0 = [p]
    | mod n p == 0 && isPrime p = [p] ++ getDivisors n xs
    | otherwise = [] ++ getDivisors n xs

isPrime :: Int -> Bool
isPrime x
  | x <= 1 = False
  | otherwise = all (\y -> x `mod` y /= 0) [2 .. floor (sqrt (fromIntegral x))]

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens [] = ([],[])
oddsNevens llista = (senars, parells)
    where
        senars = [x|x <- llista, mod x 2 /= 0]
        parells = [x|x <- llista, mod x 2 == 0]

