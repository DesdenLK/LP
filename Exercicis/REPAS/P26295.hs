import Data.List (sort)

count :: [String] -> [(String, Int)]
count [] = []
count (x:xs) = [(x, (num+1))] ++ count rest
    where
        num = length $ takeWhile (==x) xs
        rest = dropWhile (==x) xs

main :: IO()
main = do
    contents <- getContents
    let c = count $ sort $ words contents
    mapM_(putStrLn . (\(x,n) -> x ++ " " ++ show n)) c
