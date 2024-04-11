ones :: [Integer]
ones = iterate id 1

nats :: [Integer]
nats = iterate (+1) 0

ints :: [Integer]
ints =  0 : ints' 1
    where
        ints' x = x : -x : ints'(x+1)

triangulars :: [Integer]
triangulars = 0 : triangulars' 1
    where
        triangulars' x = (sum $ takeWhile (< (x+1)) nats) : triangulars' (x+1)

factorials :: [Integer]
factorials = scanl (*) 1 (iterate (+1) 1)

fibs :: [Integer]
fibs = fibs' 0 1
    where fibs' m n = m : fibs' n (m+n)

primes :: [Integer]
primes = garbell (iterate (+1) 2)
    where 
        garbell (x:xs) = x : garbell [p | p <- xs, mod p x /= 0] 

hammings :: [Integer]
hammings = 1 : merge3 (map(*2) hammings) (map (*3) hammings) (map (*5) hammings)
    where
        merge3 xs ys zs = merge xs (merge ys zs)
        merge [] xs = xs
        merge xs [] = xs
        merge (x:xs) (y:ys)
            | x < y = x : merge xs (y:ys)
            | x > y = y : merge (x:xs) ys
            | otherwise = y : merge xs ys

look :: [Char] -> Integer

look [] = 0
look [_] = 1
look (c1:c2:s)
    | c1 == c2 = 1 + (look (c2:s))
    | otherwise = 1

say :: [Char] -> [Char]

say [] = []
say s = (show count) ++ (head s) : (say (drop (fromIntegral count) s)) where count = look s

lookNsay :: [Integer]

lookNsay = iterate (read . say . show) 1

tartaglia :: [[Integer]]

tartaglia = iterate next [1]
    where next xs = zipWith (+) ([0] ++ xs) (xs ++ [0])
