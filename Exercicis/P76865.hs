data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show)

instance Foldable Tree where
    foldr f x Empty = x
    foldr f x (Node a l r) =
        f a (foldr f (foldr f x r) l)

avg :: Tree Int -> Double
avg tree = 
    let (sum, count) = foldr (\x (s,c) -> (s + fromIntegral x, c + 1)) (0,0) tree
    in sum / count

cat :: Tree String -> String
cat t = 
    let s = foldr (\x acc -> if null acc then x else x ++ " " ++ acc) "" t
    in s