insert :: [Int] -> Int -> [Int]
insert [] x = [x]
insert (p:xs) x
    | x < p = [x] ++ [p] ++ xs
    | otherwise = [p] ++ insert xs x

isort :: [Int] -> [Int]
isort [] = []
isort (p:xs) = insert (isort xs) p

remove :: [Int] -> Int -> [Int]
remove [] _ = []
remove (p:xs) x
    | p == x = xs
    | otherwise = p : remove xs x

ssort :: [Int] -> [Int]
ssort [] = []
ssort llista = 
    let minVal = minimum llista
    in
        minVal : ssort(remove llista minVal)

merge :: [Int] -> [Int] -> [Int]
merge x [] = x
merge [] y = y
merge (p:ps) (x:xs)
    | p <= x = p : merge ps (x:xs)
    | otherwise = x : merge (p:ps) xs


msort :: [Int] -> [Int]
msort [] = []
msort llista 
    | long == 0 = llista
    | otherwise = merge (msort llista1) (msort llista2)
    where 
        l = length llista
        long = div l 2
        llista1 = take long llista
        llista2 = drop long llista

qsort :: [Int] -> [Int]
qsort [] = []
qsort (p:xs) = (qsort menors) ++ [p] ++ (qsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]

genQsort :: Ord a => [a] -> [a]
genQsort [] = []
genQsort (p:xs) = (genQsort menors) ++ [p] ++ (genQsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]