

data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show)

instance Foldable Tree where
    foldr f x Empty = x
    foldr f  x (Node a l r) = f a (foldr f (foldr f x r) l)

avg :: Tree Int -> Double
avg tree =
    let (sum, count) = foldr (\x (s,c) -> (fromIntegral x + s, c + 1)) (0,0) tree
    in sum / count

cat :: Tree String -> String
cat tree = foldr (\x acc -> if acc ==  "" then x else x ++ " " ++ acc) "" tree