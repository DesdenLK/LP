data Nat = Z | S Nat deriving Show

rec :: a -> (Nat -> a -> a) -> Nat -> a
rec base step Z = base
rec base step (S n) = step n (rec base step n)

isEven :: Nat -> Bool       -- indica si un natural és parell o no
isEven = rec base step
    where
        base = True
        step _ prev = not prev

add :: Nat -> Nat -> Nat    -- retorna la suma de dos naturals
add = rec base step
    where
        base = (\x -> x)
        step _ f x = S (f x)

mul :: Nat -> Nat -> Nat   -- retorna el producte de dos naturals
mul = rec base step
    where
        base = (\x -> Z)
        step _ f x = add x (f x)

fact :: Nat -> Nat          -- retorna el factorial d’un natural
fact = rec base step
    where
        base = S(Z)
        step s x = mul (S s) x