import Data.List

degree :: Eq a => [(a, a)] -> a -> Int
degree [] _ = 0
degree ((x,y):xs) num
    | x == num || y == num = 1 + degree xs num
    | otherwise = 0 + degree xs num

degree' :: Eq a => [(a, a)] -> a -> Int
degree' l n = length l2
    where
        l2 = filter (\(x,y) -> x == n || y == n) l

neighbors :: Ord a => [(a, a)] -> a -> [a]
neighbors l n = sort (m2 ++ m1)
    where
        l2 = filter (\(x,y) -> x == n || y == n) l
        m1 = filter (\x -> x /= n) $ map (\(x,y) -> y) l2
        m2 = filter (\x -> x /= n) $ map (\(x,y) -> x) l2