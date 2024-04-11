roman2int :: String -> Int
roman2int w = solver $ map parse w
    where
        solver :: [Int] -> Int
        solver [] = 0
        solver [x] = x
        solver (x:y:xs)
            | x < y = (y-x) + solver xs
            | otherwise = x + solver (y:xs)


parse :: Char -> Int
parse 'I' = 1
parse 'V' = 5
parse 'X' = 10
parse 'L' = 50
parse 'C' = 100
parse 'D' = 500
parse 'M' = 1000

roman2int' :: String -> Int
roman2int' w = solver $ map parse w
    where
        solver :: [Int] -> Int
        solver x = sum $ zipWith op x (tail x ++ [0])
            where
                op :: Int -> Int -> Int
                op act next
                    | act < next = -act
                    | otherwise = act

arrels :: Float -> [Float]
arrels x = scanl taylor x $ repeat x
    where
        taylor :: Float -> Float -> Float
        taylor prev x = (prev + (x / prev)) / 2

arrel :: Float -> Float -> Float
arrel x e = arrel' e $ arrels x
    where
        arrel' :: Float -> [Float] -> Float
        arrel' e (x1:x2:xs) 
            | abs(x1-x2)  <= e = x2
            | otherwise = arrel' e (x2:xs)

data LTree a = Leaf a | Node (LTree a) (LTree a)

instance (Show a) => Show (LTree a) where
    show (Leaf a) = "{" ++ show a ++ "}"
    show (Node l r) = "<" ++ show l ++ "," ++ show r ++ ">"

build :: [a] -> LTree a
build x = build' $ map Leaf x
    where
        build' :: [LTree a] -> LTree a
        build' [x] = x
        build' x = Node (build' $ take l x) (build' $ drop l x)
            where
                l = div (length x + 1) 2

zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a, b))
zipLTrees (Leaf x) (Leaf y) = Just (Leaf (x, y))
zipLTrees (Node t1 t2) (Node u1 u2) = do
    lt1 <- zipLTrees t1 u1
    lt2 <- zipLTrees t2 u2
    return (Node lt1 lt2)
zipLTrees _ _ = Nothing