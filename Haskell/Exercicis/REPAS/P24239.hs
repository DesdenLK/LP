roman2int :: String -> Int
roman2int [x] = parse x
roman2int (x:y:p)
    | parse x < parse y = - (parse x) + roman2int (y:p)
    | otherwise = parse x + roman2int (y:p)



roman2int' :: String -> Int
roman2int' w = sum $ map (\(x,y) -> if x < y then -x else x) l
    where
        nums = map parse w
        l = zip nums (tail $ nums ++ [0])

arrels :: Float -> [Float]
arrels x = scanl taylor x $ repeat x

taylor :: Float -> Float -> Float
taylor prev x = 0.5*(prev + x / prev)

arrel :: Float -> Float -> Float
arrel x e = aprox e (arrels x)

aprox :: Float -> [Float] -> Float
aprox e (x1:x2:p)
    | abs(x1-x2) <= e = x2
    | otherwise = aprox e (x2:p)



parse :: Char -> Int
parse 'I' = 1
parse 'V' = 5
parse 'X' = 10
parse 'L' = 50
parse 'C' = 100
parse 'D' = 500
parse 'M' = 1000


data LTree a = Leaf a | Node (LTree a) (LTree a)

instance (Show a) => Show (LTree a) where
    show (Leaf a) = "{" ++ show a ++ "}"
    show (Node l r) = "<" ++ show l ++ "," ++ show r ++ ">"


build :: [a] -> LTree a
build x = build2 $ map Leaf x

build2 :: [LTree a] -> LTree a
build2 [x] = x
build2 x = 
    Node (build2 $ take l x) (build2 $ drop l x)
    where
        l = div (length x + 1) 2

zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a,b))
zipLTrees (Leaf x) (Leaf y) = Just(Leaf(x,y))
zipLTrees (Node l r) (Node l2 r2) = do
    ld <- zipLTrees l l2
    rd <- zipLTrees r r2
    return (Node ld rd)
zipLTrees _ _ = Nothing
