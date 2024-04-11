import Data.List

degree :: Eq a => [(a, a)] -> a -> Int
degree [] _ = 0
degree (x:xs) k
    | fst x == k || snd x == k = 1 + degree xs k
    | otherwise = degree xs k


degree' :: Eq a => [(a, a)] -> a -> Int
degree' l k = length $ filter (\(x,y) -> x == k || y == k) l


neighbors :: Ord a => [(a, a)] -> a -> [a]
neighbors [] _ = []
neighbors l k = l2
    where
        l1 = filter (\(x,y) -> x == k || y == k) l
        l2 = map (\(x,y) -> if x == k then y else x) l1

