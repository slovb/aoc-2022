module Day10.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day10.Op ( Op, readOp, simulate )

solve :: [Op] -> Int
solve ops = sum records
    where
        xs = simulate [1] ops
        extract xs i = (xs !! (i - 1)) * i
        records = map (extract xs) [20, 60, 100, 140, 180, 220]
    
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
    print output
    hClose handler
