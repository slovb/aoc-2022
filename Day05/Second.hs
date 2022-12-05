module Day05.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day05.Input ( readBuckets, readInstructions )

change :: [[Char]] -> (Int, Int, Int) -> [[Char]]
change buckets (amount, bucketA, bucketB) = do
    let get n = buckets!!(n - 1)
    let moved = take amount $ get bucketA
    let newA = drop amount $ get bucketA
    let newB = moved ++ get bucketB
    let bucket n | n == bucketA = newA
                 | n == bucketB = newB
                 | otherwise = get n
    [bucket n | n <- [1..length buckets]]

solve :: [[Char]] -> [(Int, Int, Int)] -> [[Char]]
solve buckets [] = buckets
solve buckets ins = foldl change buckets ins

output :: [[Char]] -> String
output = map head

main :: IO ()
main = do
    let filename = "Day05/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    -- print xs
    let (bs, _:is) = span (/= "") xs
    -- print bs
    -- print is
    let buckets = readBuckets bs
    print buckets
    let instructions = readInstructions is
    -- print instructions
    -- let tmp = change buckets $ head instructions
    -- print tmp
    let solution = solve buckets instructions
    print solution
    print $ output solution
    hClose handler
