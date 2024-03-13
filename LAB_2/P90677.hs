myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ x [] = x
myFoldl f x (val:llista) = myFoldl f (f x val) llista

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ x [] = x
myFoldr f x (val:llista) = f val (myFoldr f x llista)


myIterate :: (a -> a) -> a -> [a]
myIterate f x = x : myIterate f (f x)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil p f x
    | p x = x
    | otherwise = myUntil p f (f x)

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f llista = foldr (\c i -> (f c):i) [] llista

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter f llista = foldr (\c i -> if f c then c:i else i) [] llista

myAll :: (a -> Bool) -> [a] -> Bool
myAll f llista = and $ map f llista

myAny :: (a -> Bool) -> [a] -> Bool
myAny f llista = or $ map f llista

myZip :: [a] -> [b] -> [(a, b)]
myZip _ [] = []
myZip [] _ = []
myZip (x:xs) (y:ys) = (x,y) : (myZip xs ys)


myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = foldr (\(x,y) a -> (f x y):a) [] (myZip xs ys)