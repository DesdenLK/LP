fizzBuzz :: [Either Int String]
fizzBuzz = fizz 0

fizz :: Int -> [Either Int String]
fizz x
    | (x `mod` 3 == 0) && (x `mod` 5 == 0) = Right "FizzBuzz" : fizz (x+1)
    | (x `mod` 3 == 0) = Right "Fizz" : fizz (x+1)
    | (x `mod` 5 == 0) = Right "Buzz" : fizz (x+1)
    | otherwise = Left x : fizz(x+1)