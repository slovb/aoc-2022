module Day01.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.List ( sort )

import Day01.Blocks ( readInput)

solve :: [[Integer]] -> Integer
solve = sum . take 3 . reverse . sort . map sum

main :: IO ()
main = do
    let filename = "Day01/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let input = readInput xs
    let solution = solve input
    print solution
    hClose handler
