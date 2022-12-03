module Day03.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Char ( ord, isUpper )

value :: Char -> Int
value c
    | isUpper c = 27 + ord c - ord 'A' 
    | otherwise = 1 + ord c - ord 'a'

findDuplicate :: String -> String -> String -> Char
findDuplicate (x:xs) y z
    | x `elem` y && x `elem` z = x
    | otherwise = findDuplicate xs y z

score :: String -> String -> String -> Int
score x y z = value dup
    where
        dup = findDuplicate x y z

solve :: [String] -> Int
solve [] = 0
solve (x:y:z:xs) = score x y z + solve xs

main :: IO ()
main = do
    let filename = "Day03/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let input = lines contents
    print input
    let solution = solve input
    print solution
    hClose handler
