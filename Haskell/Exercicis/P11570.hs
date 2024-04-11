data Avi = Avi {
    nom :: [Char],
    edat :: Int,
    despeses :: [Int]
    } deriving (Show)

promigDespeses :: Avi -> Int
promigDespeses avi = round ((fromIntegral $ sum $ despeses avi) / (fromIntegral $ length $ despeses avi))

edatsExtremes :: [Avi] -> (Int, Int)
edatsExtremes l =  (x, y)
    where 
        r = map (\x -> edat x) l
        x = minimum r
        y = maximum r

sumaPromig :: [Avi] -> Int
sumaPromig l = sum $ map promigDespeses l

maximPromig :: [Avi] -> Int
maximPromig l = maximum $ map promigDespeses l

despesaPromigSuperior :: [Avi] -> Int -> ([Char], Int)
despesaPromigSuperior [] _ = ("", 0)
despesaPromigSuperior (a:as) k
    | promigDespeses a > k = (nom a, edat a)
    | otherwise = despesaPromigSuperior as k