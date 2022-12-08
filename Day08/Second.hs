module Day08.Second (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Char ( digitToInt )

type Position = (Int, Int)

type StepGenerator = Position -> [Position]

type PositionMap = Position -> Int

newtype Limit = Limit Int
unLimit :: Limit -> Int
unLimit (Limit limit) = limit

readInput :: [String] -> [[Int]]
readInput = map readLine

readLine :: String -> [Int]
readLine = map digitToInt

at :: [[Int]] -> PositionMap
at trees (x, y) = trees !! y !! x

left :: Limit -> StepGenerator
left (Limit limit) (x, y) = [(x - i, y) | i <- [1..(x - limit)]]

right :: Limit -> StepGenerator
right (Limit limit) (x, y) = [(x + i, y) | i <- [1..(limit - x)]]

up :: Limit -> StepGenerator
up (Limit limit) (x, y) = [(x, y - i) | i <- [1..(y - limit)]]

down :: Limit -> StepGenerator
down (Limit limit) (x, y) = [(x, y + i) | i <- [1..(limit - y)]]

limitedDirections :: Limit -> [StepGenerator]
limitedDirections limit = [limitLeft, limitRight, limitUp, limitDown]
    where
        limitLeft = left (Limit 0)
        limitRight = right limit
        limitUp = up (Limit 0)
        limitDown = down limit

count :: Int -> [Int] -> Int
count h heights = do
    let (x, y) = span (<h) heights
    length x + (if null y then 0 else 1)

scoreDirections :: [StepGenerator] -> PositionMap -> Position -> Int
scoreDirections dirs atTrees p = do
    let h = atTrees p
    let heightLists = [ map atTrees (dir p) | dir <- dirs ]
    product [ count h heightList | heightList <- heightLists ]

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
    let lim = length trees - 1
    let dirs = limitedDirections (Limit lim)
    let scored = [ scoreDirections dirs atTrees (x, y) | x <- [0..lim], y <- [0..lim] ]
    print $ maximum scored
    hClose handler
