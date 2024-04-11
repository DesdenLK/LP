fact1 :: Integer -> Integer
fact1 0 = 1
fact1 1 = 1
fact1 n = n * fact1(n-1)

fact2 :: Integer -> Integer
fact2 n = product [1..n]

fact3 :: Integer -> Integer
fact3 n = (map fact1 $ iterate (+1) 0) !! fromIntegral n

fact4 :: Integer -> Integer
fact4 n = 
    if n < 2 then 1
    else n * fact4 (n-1)

fact5 :: Integer -> Integer
fact5 n = foldl (*) 1 (take (fromIntegral n) $ iterate (+1) 1)

fact6 :: Integer -> Integer
fact6 n = (scanl (*) 1 (iterate (+1) 1)) !! fromIntegral n

fact7 :: Integer -> Integer
fact7 n = foldr (*) 1 [1..n]

fact8 :: Integer -> Integer
fact8 n = fact' n 1
  where
    fact' 0 acc = acc
    fact' n acc = (fact' (n-1) $! (n * acc))