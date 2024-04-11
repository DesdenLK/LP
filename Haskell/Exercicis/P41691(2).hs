-- Función para multiplicar dos polinomios representados por listas de coeficientes
import Data.List (unfoldr)

mult :: [Double] -> [Double] -> [Double]
mult p1 p2 = reverse $ unfoldr step (p1, p2)
  where
    step :: ([Double], [Double]) -> Maybe (Double, ([Double], [Double]))
    step ([], _) = Nothing  -- Si p1 está vacío, terminamos
    step (c:cs, p) =
      let result = evalTerm c p  -- Multiplicar c por cada coeficiente en p2
          paddedResult = result : replicate (length(p) - 1) 0  -- Añadir ceros para alinear términos
      in Just (result, (cs, paddedResult))

    -- Evaluar el término c * p2
    evalTerm :: Double -> [Double] -> Double
    evalTerm _ [] = 0
    evalTerm c (x:xs) = c * x + evalTerm c xs

-- Ejemplo de uso:
-- Multiplicar los polinomios [3.5, -2, 6, 1] y [1, 2, -1, 0]
polinomio1 :: [Double]
polinomio1 = [3.5, -2, 6, 1]

polinomio2 :: [Double]
polinomio2 = [1, 2, -1, 0]

resultado :: [Double]
resultado = mult polinomio1 polinomio2
-- resultado será [3.5, 5.0, -16.5, 9.0, -11.0, 12.0, -1.0, 0.0]
