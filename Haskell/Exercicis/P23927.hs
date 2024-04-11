import Data.List

subllista :: [a] -> [[a]]
subllista [] = [[]]
subllista (x:xs)  = [x:rest | rest <- subllista xs] ++ subllista xs

sumEquals1 :: Int -> [Int] -> [[Int]]
sumEquals1 s [] = []
sumEquals1 s l = filter (\x -> sum x == s) (subllista l)



sumEquals2 :: Int -> [Int] -> Maybe [Int]
sumEquals2 s l 
    | r /= [] = Just (concat $ take 1 $ reverse$ sort $ r)
    | otherwise = Nothing
    where
        w = filter (\x -> sum x == s) (subllista l)
        r = no_reps w l

no_reps :: [[Int]] -> [Int] -> [[Int]]
no_reps [] _ = []
no_reps (s:subs) nums
    | cuenta s nums = s : no_reps subs nums
    | otherwise = no_reps subs nums

cuenta :: [Int] -> [Int] -> Bool
cuenta [] _ = True
cuenta (p:xs) l = (length r /= length l) && cuenta xs (r ++ tail w)
    where
        r = takeWhile (\x -> x /= p) l
        w = dropWhile (\x -> x /= p) l

sumEquals3 :: Int -> [Int] -> [[Int]]
sumEquals3 s [] = []
sumEquals3 s l = filter (\x -> sum x == s) (subllista l)