module Day01.Blocks (groupBlocks, readBlocks, readInts, readInput) where

groupBlocks :: [[String]] -> [String] -> [String] -> [[String]]
groupBlocks blocks [] [] = blocks
groupBlocks blocks block [] = groupBlocks (blocks ++ [block]) [] []
groupBlocks blocks block ("":xs) = groupBlocks (blocks ++ [block]) [] xs
groupBlocks blocks block (x:xs) = groupBlocks blocks (block ++ [x]) xs

readBlocks :: [String] -> [[String]]
readBlocks xs = do
    groupBlocks [] [] xs

readInts :: [String] -> [Integer]
readInts = map read

readInput :: [String] -> [[Integer]]
readInput xs = map readInts (readBlocks xs)
