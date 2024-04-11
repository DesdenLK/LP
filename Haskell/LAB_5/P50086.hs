data Queue a = Queue [a] [a] deriving (Show)

instance Eq a => Eq (Queue a)
    where
        (Queue l1 l2) == (Queue l3 l4) = (l1 ++ reverse l2) == (l3 ++ reverse l4)


instance Functor (Queue) where
    fmap f (Queue [] []) = Queue [] []
    fmap f (Queue [] llista) = Queue [] (fmap f llista)
    fmap f (Queue llista []) = Queue (fmap f llista) []
    fmap f (Queue l1 l2) = Queue (fmap f l1) (fmap f l2)

instance Applicative(Queue) where
    pure x = push x (create)
    (Queue [] []) <*> q = (create)
    f <*> q = concatQueue (fmap (top f) q) (pop f <*> q)

instance Monad (Queue) where
    return x = push x (create)
    q >>= f = flatQueue $ fmap f q

concatQueue :: Queue a -> Queue a -> Queue a
concatQueue (Queue f1 s1) (Queue f2 s2) = (Queue total [])
    where
        total = t1 ++ t2
        t1 = f1 ++ (reverse s1)
        t2 = f2 ++ (reverse s2)

flatQueue :: Queue (Queue a) -> Queue a
flatQueue (Queue [] []) = (create)
flatQueue q = concatQueue (top q) (flatQueue (pop q))

create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push x (Queue l1 l2) = Queue l1 ([x] ++ l2)

pop :: Queue a -> Queue a
pop (Queue [] []) = Queue [] []
pop (Queue [] l2) = Queue (tail $ reverse l2) []
pop (Queue l1 l2) = Queue (tail l1) l2

top :: Queue a -> a
top (Queue [] l2) = last l2
top (Queue l1 _) = head l1

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty (Queue l1 l2) = False



translation :: Num b => b -> Queue b -> Queue b
translation x c = fmap (+x) c

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter f q = do
    qf <- q
    if f qf then return qf else (create)