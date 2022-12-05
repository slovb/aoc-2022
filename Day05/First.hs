module Day05.First (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

import Day05.Input ( readBuckets, readInstructions )

change :: [[Char]] -> (Int, Int, Int) -> [[Char]]
-- change buckets (0, _, _) = buckets
change buckets (amount, bucketA, bucketB) = do
    let get i = buckets!!(i - 1)
    let moved = take amount $ reverse $ get bucketA
    let newA = reverse . drop amount $ reverse $ get bucketA
    let newB = get bucketB ++ moved
    let buck i | i == bucketA = newA
               | i == bucketB = newB
               | otherwise = get i
    [buck i | i <- [1..length buckets]]
    -- change bs (amount - 1, bucketA, bucketB)
    

solve :: [[Char]] -> [(Int, Int, Int)] -> [[Char]]
solve buckets [] = buckets
solve buckets ins = foldl change buckets ins

output :: [[Char]] -> String
output = map last

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
    -- print buckets
    let instructions = readInstructions is
    -- print instructions
    let solution = solve buckets instructions
    -- print solution
    print $ output solution
    hClose handler
