myMap :: (a -> b) -> [a] -> [b]
myMap f llista = [f x | x <- llista]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter p llista = [x | x <- llista, p x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f llista1 llista2 = [f x y| (x,y) <- zip llista1 llista2]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify llista1 llista2 = [(x,y) | x <- llista1, y <- llista2, mod x y == 0]

factors :: Int -> [Int]
factors n = [x | x <- [1..n], mod n x == 0]