import Data.List

type Pos = (Int, Int)

dins :: Pos -> Bool
dins (x,y) = (x > 0 && x < 9) && (y > 0 && y < 9)


moviments :: Pos -> [Pos]
moviments (x,y) = filter dins [(x-2,y+1),(x-1,y+2),(x+1,y+2),(x+2,y+1),
                    (x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1)]

potAnar3 :: Pos -> Pos -> Bool
potAnar3 p1 p2 = p2 `elem` r3
    where
        r = moviments p1
        r2 = concatMap moviments r
        r3 = concatMap moviments r2

potAnar3' :: Pos -> Pos -> Bool
potAnar3' p1 p2 = p2 `elem` r
    where r = moviments p1 >>= moviments >>= moviments
