absValue :: Int -> Int
absValue n
    | n >= 0 = n
    | otherwise = -n

power :: Int -> Int -> Int
power _ 0 = 1
power x p
    | even p = y * y
    | otherwise = y * y * x
    where
        y = power x p_halved
        p_halved = div p 2

isPrime :: Int -> Bool
isPrime n
    | n == 0 = False
    | n == 1 = False
    | n == 2 = True
    | otherwise = getPrime n 2

getPrime :: Int -> Int -> Bool
getPrime n i
    | i > limit = True
    | mod n i == 0 = False
    | otherwise = getPrime n (i+1)
    where
        limit = floor (sqrt (fromIntegral n))

slowFib :: Int -> Int
slowFib n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = slowFib (n-1) + slowFib (n-2) 

quickFib :: Int -> Int
quickFib n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fst k + snd k 
    where 
        k = auxFib (0,1) (n, 2)

auxFib :: (Int, Int) -> (Int,Int) -> (Int,Int)
auxFib (fib0, fib1) (n, limit)
    | n == limit = (fib0, fib1)
    | otherwise = auxFib (fib1, (fib0+fib1)) (n, (limit+1))