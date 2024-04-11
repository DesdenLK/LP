countIf :: (Int -> Bool) -> [Int] -> Int
countIf f llista = length (filter f llista)

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam x fs = [map f x | f <- fs]

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 n fs = map (\x -> [f x | f <- fs ]) n

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl b f x llista = foldl f x $ filter b llista

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert _ [] x = [x]
insert f (l:llista) x
    | f l x = l : insert f llista x
    | otherwise = x : l : llista

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort _ [] = []
insertionSort f (l:llista) = insert f (insertionSort f llista) l