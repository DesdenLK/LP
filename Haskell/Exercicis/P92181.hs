import Data.List (subsequences)

analyze :: Int -> Either Int Bool
analyze n 
    | l > 12 = Left l
    | otherwise = Right (isPerfect n p)
    where
        p = [x | x <- [1..(div n 2)], n `mod` x == 0]
        l = length p

isPerfect :: Int -> [Int] -> Bool
isPerfect n divisors = any (==n) [sum s | s <- subsequences divisors]