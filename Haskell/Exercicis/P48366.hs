eval1 :: String -> Int
eval1 w = evalua [] $ words w
    where
        evalua (p:ps) [] = p
        evalua p (x:xs)
            | x == "+" = (\(p1:p2:ps) -> evalua((p2+p1):ps) xs) p
            | x == "-" = (\(p1:p2:ps) -> evalua((p2-p1):ps) xs) p
            | x == "*" = (\(p1:p2:ps) -> evalua((p2*p1):ps) xs) p
            | x == "/" = (\(p1:p2:ps) -> evalua((p2`div`p1):ps) xs) p
            | otherwise = evalua((read x):p) xs

eval2 :: String -> Int
eval2 w = (\(x:xs) -> x) $ foldl (evaluar) [0] $ words w
    where
        evaluar p e
            | e == "+" = (\(p1:p2:ps) -> ((p2+p1):ps)) p
            | e == "-" = (\(p1:p2:ps) -> ((p2-p1):ps)) p
            | e == "*" = (\(p1:p2:ps) -> ((p2*p1):ps)) p
            | e == "/" = (\(p1:p2:ps) -> ((p2`div`p1):ps)) p
            | otherwise = (read e): p

fsmap :: a -> [a -> a] -> a 
fsmap x fs = foldl (\p f -> f p) x fs

divideNconquer::(a -> Maybe b) -> (a -> (a,a)) -> (a -> (a,a) -> (b,b) -> b) -> a -> b
divideNconquer base divide conquer x
    | f (base x) = conquer x (divide x) (divideNconquer base divide conquer (fst $ divide x),divideNconquer base divide conquer (snd $ divide x))
    | otherwise = (\(Just y) -> y) (base x)
        where
            f Nothing = True
            f _ = False

quickSort::[Int]->[Int]
quickSort l = divideNconquer base divide conquer l
    where
        base [] = Just []
        base [x] = Just [x]
        base _ = Nothing
        divide x = ((filter ((x!!(div (length x) 2))>) x),(filter ((x!!(div (length x) 2))<) x))
        conquer x _ con = (fst con)++(filter ((x!!(div (length x) 2))==) x)++(snd con)

data Racional = Racional Integer Integer

instance Show Racional where
    show r = (show $ numerador r) ++ "/" ++ (show $ denominador r)

instance Eq Racional where
    (Racional x y) == (Racional s t) = x*t == y*s


racional :: Integer -> Integer -> Racional
racional num dem = Racional num dem

numerador :: Racional -> Integer
numerador (Racional num dem) = div num $ gcd num dem

denominador :: Racional -> Integer
denominador (Racional num dem) = div dem $ gcd num dem

data Tree a = Node a (Tree a) (Tree a)
recXnivells :: Tree a -> [a]
recXnivells t = recXnivells' [t]
    where recXnivells' ((Node x fe fd):ts) = x:recXnivells' (ts ++ [fe, fd])

racionals :: [Racional]
racionals = racionals' [(Racional 1 1)]
    where racionals' ((Racional a b):ts) = (Racional a b):(racionals' (ts ++ [(Racional a (a+b)), (Racional (a+b) b)]))


            

