module Day07.First where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day07.Input ( readInput )

main :: IO ()
main = do
    let filename = "Day07/test.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let files = readInput xs
    print files
    hClose handler
