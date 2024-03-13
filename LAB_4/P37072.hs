data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

size :: Tree a -> Int
size Empty = 0
size (Node a fe fd) = 1 + size fe + size fd

height :: Tree a -> Int 
height Empty = 0
height (Node a fe fd) = 1 + max (height fe) (height fd)

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty = True
equal Empty (Node x _ _) = False
equal (Node x _ _) Empty = False
equal (Node x fex fdx) (Node y fey fdy) = (x == y) && (equal fex fey) && (equal fdx fdy)

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic Empty _ = False
isomorphic _ Empty = False
isomorphic (Node x fex fdx) (Node y fey fdy)
    | x /= y = False
    | otherwise = ((equal fex fey) && (equal fdx fdy)) || ((equal fex fdy) && (equal fdx fey))

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node x fe fd) = [x] ++ preOrder fe ++ preOrder fd

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node x fe fd) = postOrder fe ++ postOrder fd ++ [x]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node x fe fd) = inOrder fe ++ [x] ++ inOrder fd

breadthFirst :: Tree a -> [a]
breadthFirst t = auxiliarQueue [t]


auxiliarQueue :: [Tree a]  -> [a]
auxiliarQueue [] = [] 
auxiliarQueue ((Node x fe fd):xs) =  x : (auxiliarQueue (xs ++ [fe,fd]))
auxiliarQueue (Empty:xs) = auxiliarQueue xs

build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build [x] [y] = Node x Empty Empty
build (r:pre) inord = Node r (build lpre linord) (build rpre rinord)
    where
        linord = takeWhile (/=r) inord
        rinord = tail $ dropWhile(/=r) inord
        lastn = last linord
        lpre = takeWhile (/=lastn) pre ++ [lastn]
        rpre = tail $ dropWhile (/=lastn) pre

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap f Empty Empty = Empty
overlap _ a Empty = a
overlap _ Empty a = a
overlap f (Node x fex fdx) (Node y fey fdy) = Node (f x y) (overlap f fex fey) (overlap f fdx fdy)