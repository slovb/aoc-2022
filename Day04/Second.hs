module Day04.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Char ( ord, isUpper )

import Day04.Input ( readInput )
import Day04.Range ( Range, overlap )

score :: (Range, Range) -> Int
score (a, b) | overlap a b = 1
             | otherwise = 0

solve :: [(Range, Range)] -> Int
solve = sum . map score

main :: IO ()
main = do
    let filename = "Day04/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let input = readInput xs
    print input
    let solution = solve input
    print solution
    hClose handler
