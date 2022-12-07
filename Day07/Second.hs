module Day07.Second where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day07.Input ( readInput, MyFiles(..), getSize )

folders :: MyFiles -> [Int]
folders (MyFile _ _) = []
folders (MyFolder _ size children)
    = size : concatMap folders children

solve :: Int -> MyFiles -> Int
solve missing files = minimum candidates
    where candidates = filter (>= missing) $ folders files

main :: IO ()
main = do
    let filename = "Day07/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let files = readInput xs
    -- print files
    let total = 70000000 - getSize files
    let req = 30000000
    let missing = req - total
    let solution = solve missing files
    print solution
    hClose handler
