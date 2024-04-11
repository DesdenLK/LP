import Data.List
import Data.Ord

votsMinim :: [([Char], Int)] -> Int -> Bool
votsMinim [] _ = False
votsMinim (p:ps) k
    | snd p  <= k = True
    | otherwise = votsMinim ps k

candidatMesVotat :: [([Char], Int)] -> [Char]
candidatMesVotat v = fst $ maximumBy (comparing snd) v

votsIngressos :: [([Char], Int)] -> [([Char], Int)] -> [[Char]]
votsIngressos v i = filter (\x -> not(x `elem` i2)) v2
    where
        v2 = map (fst) v
        i2 = map (fst) i


rics :: [([Char], Int)] -> [([Char], Int)] -> [[Char]]
rics v i = take 3 format
    where
        iOrd = map fst $ sortBy (flip $ comparing snd) i
        v2 = map fst v
        format = map (\x -> if x `elem` v2 then x ++ "*" else x ++ "") iOrd