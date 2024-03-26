qsort :: [Int] -> [Int]
qsort [] = []
qsort (p:xs) = (qsort menors) ++ [p] ++ (qsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]

qsort2 :: [Int] -> [Int]
qsort2 [] = []
qsort2 (p:xs) = (qsort2 majors) ++ [p] ++ (qsort2 menors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]


minProd :: [Int] -> [Int] -> Int
minProd [] _ = 0
minProd l1 l2 = prodesc (qsort l1) (qsort2 l2)

prodesc :: [Int] -> [Int] -> Int
prodesc [] [] = 0
prodesc (x:l1) (y:l2) = x*y + prodesc l1 l2