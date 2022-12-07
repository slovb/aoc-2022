module Day07.First where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day07.Input ( readInput, MyFiles(..) )

solve :: Int -> MyFiles -> Int
solve i (MyFile _ _) = i
solve i (MyFolder _ size children) = i + x + y
    where
        x | size <= 100000 = size | otherwise = 0
        y = sum $ map (solve 0) children

main :: IO ()
main = do
    let filename = "Day07/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let files = readInput xs
    -- print files
    let solution = solve 0 files
    print solution
    hClose handler
