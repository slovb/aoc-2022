module Day09.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Data.Set ( fromList )

import Day09.Input ( readInput )

import Day09.Position ( Position, followPositions )

import Day09.Move ( Move(..), journey )

solve :: [Move] -> [Position]
solve moves = tailPositions
    where
        start = (0, 0)
        headPositions = journey [start] moves
        tailPositions = followPositions [start] headPositions

main :: IO ()
main = do
    let day = "Day09"
    let test = False
    let filename = day ++ if test then "/test.txt" else "/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let moves = readInput xs
    -- print moves
    let output = solve moves
    -- print output
    let reduced = fromList output
    print $ length reduced
    hClose handler
