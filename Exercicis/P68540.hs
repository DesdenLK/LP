import Data.List (sortOn)

diffSqrs :: Integer -> Integer
diffSqrs n = (t2*t2) - t1
    where
        t1 = (sum $ map (^2) $ take (fromIntegral (n)) $ iterate (+1) 1)
        t2 = (sum $ take (fromIntegral n) $ iterate (+1) 1)

sumDigits :: Integer -> Integer
sumDigits n = sum $ map (read . pure) $ show n

tartaglia :: [[Integer]]
tartaglia = iterate next [1]
    where next xs = zipWith (+) ([0] ++ xs) (xs ++ [0])

digitalRoot :: Integer -> Integer
digitalRoot n = head $ dropWhile (>9) $ iterate (sumDigits) n

pythagoreanTriplets :: Int -> [(Int, Int, Int)]
pythagoreanTriplets n = sortOn (\(a, _, _) -> a) $ [(a, b, c) | c <- [1..n], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a + b + c == n]

