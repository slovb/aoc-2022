module Day08.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Char ( digitToInt )

readInput :: [String] -> [[Int]]
readInput = map readLine

readLine :: String -> [Int]
readLine = map digitToInt

left :: Int -> Int -> Int -> [(Int, Int)]
left limit x y = [(x - i, y) | i <- [1..(x - limit)]]

right :: Int -> Int -> Int -> [(Int, Int)]
right limit x y = [(x + i, y) | i <- [1..(limit - x)]]

up :: Int -> Int -> Int -> [(Int, Int)]
up limit x y = [(x, y - i) | i <- [1..(y - limit)]]

down :: Int -> Int -> Int -> [(Int, Int)]
down limit x y = [(x, y + i) | i <- [1..(limit - y)]]

at :: [[Int]] -> (Int, Int) -> Int
at trees (x, y) = trees !! y !! x

limitedDirections :: Int -> [Int -> Int -> [(Int, Int)]]
limitedDirections side = [limitLeft, limitRight, limitUp, limitDown]
    where
        limitLeft = left 0
        limitRight = right (side - 1)
        limitUp = up 0
        limitDown = down (side - 1)

testDirections :: [Int -> Int -> [(Int, Int)]] -> ((Int, Int) -> Int) -> Int -> Int -> Bool
testDirections dirs atTrees x y = do
    let h = atTrees (x, y)
    or [ all ((<h) . atTrees) (dir x y) | dir <- dirs ]

main :: IO ()
main = do
    let day = "Day08"
    let test = False
    let filename = day ++ if test then "/test.txt" else "/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let trees = readInput xs
    -- print trees
    let atTrees = at trees
    let side = length trees
    let dirs = limitedDirections side
    let tested = [ testDirections dirs atTrees x y | x <- [0..(side - 1)], y <- [0..(side - 1)] ]
    print $ length (filter id tested)
    hClose handler
