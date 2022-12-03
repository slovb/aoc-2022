module Day03.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Char ( ord, isUpper )

import Day03.Input ( readInput )

findDuplicate :: String -> String -> Char
findDuplicate (x:xs) y
    | x `elem` y = x
    | otherwise = findDuplicate xs y

value :: Char -> Int
value c
    | isUpper c = 27 + ord c - ord 'A' 
    | otherwise = 1 + ord c - ord 'a'

score :: (String, String) -> Int
score (a, b) = value dup
    where
        dup = findDuplicate a b

solve :: [(String, String)] -> Int
solve = sum . map score

main :: IO ()
main = do
    let filename = "Day03/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let input = readInput xs
    print input
    let solution = solve input
    print solution
    hClose handler
