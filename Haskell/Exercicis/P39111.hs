import Data.List

type Pos = (Int, Int)

dins :: Pos -> Bool
dins (x, y) = (x > 0 && x < 9) && (y > 0 && y < 9)


moviments :: Pos -> [Pos]
moviments (x ,y) = filter dins [(x + 1, y +2 ), (x-1, y+2), (x+1,y-2), (x-1, y-2),
                    (x-2,y+1), (x-2,y-1), (x+2, y-1), (x+2, y+1)]

potAnar3 :: Pos -> Pos -> Bool
potAnar3 origen desti = desti `elem` movs3 
    where 
        movs1 = moviments origen
        movs2 = concatMap moviments movs1
        movs3 = concatMap moviments movs2


potAnar3' :: Pos -> Pos -> Bool
potAnar3' origen desti = desti `elem` m
    where m = (moviments origen >>= moviments >>= moviments)

