import Data.Ratio

factorial :: Integer -> Rational
factorial n = product [1 % 1, 2 % 1 .. n % 1]

termes_cosinus :: Rational -> [Rational]
termes_cosinus alpha = [(-1)^n * (alpha^(2*n)) / (factorial (2*n))| n <- [0..]]


cosinus :: Rational -> Rational -> Rational
cosinus alpha epsilon = sum [x | x <- take 100 $ termes_cosinus alpha, abs(x) >= epsilon]
