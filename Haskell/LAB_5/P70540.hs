data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1 :: Expr -> Int
eval1 (Val x) = x
eval1 (Add exp1 exp2) = eval1 exp1 + eval1 exp2
eval1 (Sub exp1 exp2) = eval1 exp1 - eval1 exp2
eval1 (Mul exp1 exp2) = eval1 exp1 * eval1 exp2
eval1 (Div exp1 exp2) = eval1 exp1 `div` eval1 exp2

eval2 :: Expr -> Maybe Int
eval2 (Val x) = Just x
eval2 (Add exp1 exp2) = do
    l <- eval2(exp1)
    r <- eval2(exp2)
    return (l + r)
eval2 (Sub exp1 exp2) = do
    l <- eval2(exp1)
    r <- eval2(exp2)
    return (l - r)
eval2 (Mul exp1 exp2) = do
    l <- eval2(exp1)
    r <- eval2(exp2)
    return (l * r)
eval2 (Div exp1 exp2) = do
    l <- eval2(exp1)
    r <- eval2(exp2)
    if r == 0 then Nothing else return (l `div` r)

eval3 :: Expr -> Either String Int
eval3 (Val x) = Right x
eval3 (Add exp1 exp2) = do
    l <- eval3(exp1)
    r <- eval3(exp2)
    Right (l + r)
eval3 (Sub exp1 exp2) = do
    l <- eval3(exp1)
    r <- eval3(exp2)
    Right (l - r)
eval3 (Mul exp1 exp2) = do
    l <- eval3(exp1)
    r <- eval3(exp2)
    Right (l * r)
eval3 (Div exp1 exp2) = do
    l <- eval3(exp1)
    r <- eval3(exp2)
    if r == 0 then Left "div0" else Right(l `div` r)
