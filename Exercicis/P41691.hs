mult :: [Double] -> [Double] -> [Double]
mult l1 l2 = calcula p1 p2
    where
        n = length p1
        p1 = l1
        p2 = l2 ++ (take n $ repeat 0)


calcula :: [Double] -> [Double] -> [Double]
calcula [] _ = repeat 0
calcula (p:ps) p2 = zipWith (+) ((map (*p) p2)) n
    where
        n = (calcula ps ([0] ++ p2))