import Data.List

countWords :: [String] -> [(String, Int)]
countWords [] = []
countWords (x:xs) = [(x, t + 1)] ++ countWords (dropWhile (==x) xs)
    where
        t = (length $ takeWhile (==x) xs)

main :: IO()
main = do
    text <- getContents
    let w = sort $ words text
    let c = countWords w
    mapM_ (\(word, count) -> putStrLn $ word ++ " " ++ show count) c


