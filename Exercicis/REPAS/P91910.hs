multEq :: Int -> Int -> [Int]
multEq x y = iterate (x*y*) 1

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
selectFirst [] _ _ = []
selectFirst _ [] _ = []
selectFirst l l2 [] = filter (\x -> x `elem` l2) l
selectFirst (x:xs) l2 l3
    | abans x l2 l3 = x : selectFirst xs l2 l3
    | otherwise = selectFirst xs l2 l3

abans :: Int -> [Int] -> [Int] -> Bool
abans _ [] _ = False
abans x l2 [] = x `elem` l2
abans x (a:as) (b:bs)
    | x == a = True
    | x == b = False
    | otherwise = abans x as bs


myIterate :: (a -> a) -> a -> [a]
myIterate f x = scanl (\a b -> f a) x [1..]


type SymTab a = String -> Maybe a

empty :: SymTab a
empty = (\x -> Nothing)

get :: SymTab a -> String -> Maybe a
get t s = t s

set :: SymTab a -> String -> a -> SymTab a
set t k v = (\s -> if s == k then Just v else t s)

data Expr a
     = Val a
     | Var String
     | Sum (Expr a) (Expr a)
     | Sub (Expr a) (Expr a)
     | Mul (Expr a) (Expr a)
     deriving Show

eval :: (Num a) => SymTab a -> Expr a -> Maybe a
eval t (Val a) = Just a
eval t (Sum a b) = op (+) (eval t a) (eval t b)
eval t (Sub a b) = op (-) (eval t a) (eval t b)
eval t (Mul a b) = op (*) (eval t a) (eval t b)
eval t (Var s) = t s

op :: (Num a) => (a -> a -> a) -> Maybe a -> Maybe a -> Maybe a
op f x y
    |isN x || isN y = Nothing
    | otherwise = (\(Just a) (Just b) -> (Just (f a b))) x y
    where
        isN Nothing = True
        isN _ = False
