sumMultiples35 :: Integer -> Integer
sumMultiples35 n = sumMultiples n 3 + sumMultiples n 5 - sumMultiples n 15
    where
        sumMultiples :: Integer -> Integer -> Integer
        sumMultiples n x = x * (div (n-1) x) * ((div (n-1) x)+1) `div` 2

fibonacci :: Int -> Integer
fibonacci n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fst k + snd k 
    where 
        k = auxFib (0,1) (fromIntegral(n), 2)

auxFib :: (Integer, Integer) -> (Integer,Integer) -> (Integer,Integer)
auxFib (fib0, fib1) (n, limit)
    | n == limit = (fib0, fib1)
    | otherwise = auxFib (fib1, (fib0+fib1)) (n, (limit+1))



isPalindromic :: Integer -> Bool
isPalindromic n = esPalindrom (show n)

esPalindrom :: String -> Bool
esPalindrom [] = True
esPalindrom [x] = True
esPalindrom llista 
    | (head llista) /= (last llista) = False
    | otherwise = esPalindrom $ tail $ init llista

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


largestPrimeFactor :: Int -> Int
largestPrimeFactor n
    | n == 1 = 1
    | isPrime n = n
    | otherwise = getLargestPrime n n

getLargestPrime ::  Int -> Int -> Int
getLargestPrime n number
    | (number `mod` n == 0) && isPrime n = n
    | otherwise = getLargestPrime (n-1) number

sumEvenFibonaccis :: Integer -> Integer
sumEvenFibonaccis n = evenFibo 0 n

evenFibo :: Integer -> Integer -> Integer
evenFibo n limit 
    | t >= limit = 0
    | even t = t + evenFibo (n+1) limit
    | otherwise = evenFibo (n+1) limit
    where
        t = fibonacci $ fromIntegral n
    


    