nats :: [Int]
nats = iterate (+1) 1

divisors :: Int -> [Int]
divisors n = [x | x <- (take n nats), n `mod` x == 0]


nbDivisors :: Int -> Int
nbDivisors n = length $ divisors n

moltCompost :: Int -> Bool
moltCompost n =  null [x | x <- [1..(n-1)], nbDivisors x >= nbDivisors n]