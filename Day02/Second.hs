module Day02.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day02.Hand ( Hand, handScore, vsScore )

import Day02.SecondInput ( readInput )

score :: (Hand, Hand) -> Integer
score (left, right) = vsScore left right + handScore right

solve :: [(Hand, Hand)] -> Integer
solve = sum . map score

main :: IO ()
main = do
    let filename = "Day02/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let input = readInput xs
    print input
    let solution = solve input
    print solution
    hClose handler
