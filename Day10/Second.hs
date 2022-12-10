module Day10.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day10.Op ( Op, readOp, simulate )

draw :: String -> Int -> [Int] -> String
draw s i [] = s
draw s 40 xs = draw (s ++ ['\n']) 0 xs
draw s i (x:xs) = draw (s ++ [char]) (i + 1) xs
    where
        lit x i = i == (x - 1) || i == x || i == (x + 1)
        char = if lit x i then '#' else ' '

solve :: [Op] -> String
solve ops = draw [] 0 xs
    where
        xs = simulate [1] ops
    
main :: IO ()
main = do
    let day = "Day10"
    let test = False
    let filename = day ++ if test then "/test.txt" else "/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let ops = map readOp xs
    let output = solve ops
    putStrLn output
    hClose handler
