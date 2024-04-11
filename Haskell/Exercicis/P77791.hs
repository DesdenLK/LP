import Data.List
import Data.Function

serieCollatz :: Integer -> [Integer]
serieCollatz 1 = [1]
serieCollatz k = calcula_serie [k]

calcula_serie :: [Integer] -> [Integer]
calcula_serie p 
    | last p == 1 = p
    | even $ last p = calcula_serie (p ++ [((last p) `div` 2)])
    | otherwise = calcula_serie (p ++ [3*(last p)+1])

collatzMesLlarga :: Integer -> Integer
collatzMesLlarga k = maximum $ map (\x -> toInteger(length(serieCollatz x))) [1..k]

representantsCollatz :: [Integer] -> [Integer]
representantsCollatz ns = findMin [1..(collatzMesLlarga $ last ns)] l
    where
        l = map (\x -> (x, toInteger $ length $ serieCollatz x)) ns

findMin :: [Integer] -> [(Integer, Integer)] -> [Integer]
findMin [] _ = []
findMin (p:ps) l
    | r /= [] = [minimum $ map (fst) $ r] ++ findMin ps l
    | otherwise = [] ++ findMin ps l
    where
        r = filter (\x -> snd x == p) l

classeCollatz :: Integer -> Either Int [Integer]
classeCollatz n 
    | t > 35 = Left t
    | otherwise = Right (filter (\x -> (length $ serieCollatz x) == t) [1..1000])
    where
        t = length $ serieCollatz n
