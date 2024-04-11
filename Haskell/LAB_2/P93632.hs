eql :: [Int] -> [Int] -> Bool 
eql llista1 llista2
    | length llista1 /= length llista2 = False
    | otherwise = and $ zipWith (==) llista1 llista2


prod :: [Int] -> Int 
prod llista = product llista


prodOfEvens :: [Int] -> Int 
prodOfEvens llista = prod $ filter even llista

powersOf2 :: [Int]
powersOf2 = iterate (*2) 1


scalarProduct :: [Float] -> [Float] -> Float
scalarProduct llista1 llista2 = sum $ zipWith(*) llista1 llista2