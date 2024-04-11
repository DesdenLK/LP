myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]
myUnfoldr f x = case f x of
    Just (x, nx) -> x : myUnfoldr f nx
    Nothing -> []
    

myReplicate :: a -> Int -> [a]
myReplicate x n = myUnfoldr (\b -> if b == 0 then Nothing else Just(x, b-1)) n

myIterate :: (a -> a) -> a -> [a]
myIterate f x = myUnfoldr (\x -> Just(x , f x)) x


myMap :: (a -> b) -> [a] -> [b]
myMap f llista = myUnfoldr applyF llista
    where
        applyF [] = Nothing
        applyF (y:ys) = Just(f y, ys)

data Bst a = Empty | Node a (Bst a) (Bst a)

instance (Show a) => Show (Bst a) where
    show Empty = "."
    show (Node x l r) = "(" ++ show x ++ " " ++ show l ++ " " ++ show r ++ ")"
 
add :: Ord a => a -> (Bst a) -> (Bst a)
add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y          = Node y (add x l) r
    | x > y          = Node y l (add x r)
    | otherwise = Node y l r

adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
adder (tree, []) = Nothing
adder (tree ,x:xs) = Just(tree' , (tree', xs))
    where 
        tree' = add x tree


