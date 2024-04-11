myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]
myUnfoldr f x = case f x of
    Nothing -> []
    Just(x, nx) -> x:myUnfoldr f nx


myReplicate :: a -> Int -> [a]
myReplicate x n = myUnfoldr (\n -> if n == 0 then Nothing else Just(x, n-1)) n

myIterate :: (a -> a) -> a -> [a]
myIterate f x = myUnfoldr (\x -> Just(x, f x)) x

myMap :: (a -> b) -> [a] -> [b]
myMap f l = myUnfoldr applyF l
    where
        applyF [] = Nothing
        applyF (y:ys) = Just(f y, ys)


data Bst a = Empty | Node a (Bst a) (Bst a)
 
add :: Ord a => a -> (Bst a) -> (Bst a)
add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y          = Node y (add x l) r
    | x > y          = Node y l (add x r)
    | otherwise = Node y l r

instance (Show a) => Show (Bst a) where
    show Empty = "."
    show (Node a l r) = "(" ++ show a ++ " " ++ show l ++ " " ++ show r ++ ")"

adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
adder (_, []) = Nothing
adder (tree ,(x:xs)) = Just(a, (a, xs))
    where
        a = add x tree