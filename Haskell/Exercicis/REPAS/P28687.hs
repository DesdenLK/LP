import Data.Ratio

factorial :: Integer -> Rational
factorial n = (product [1,2..n]) % 1


termes_cosinus :: Rational -> [Rational]
termes_cosinus a = [(-1)^n * ((a ^ (2*n)) / factorial(2*n)) | n <- [0,1..100]]

cosinus :: Rational -> Rational -> Rational
cosinus a e = sum $ filter (\x -> abs(x) >= e) $ termes_cosinus a