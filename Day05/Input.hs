module Day05.Input ( readBuckets, readInstructions ) where

readBuckets :: [String] -> [[Char]]
readBuckets input = do
    let names:rows = reverse input
    let last_name = last $ words names
    let num = read last_name :: Int
    [readBucket (i * 4 - 3) rows | i <- [1..num]]

readBucket :: Int -> [String] -> [Char]
readBucket i = filter (/= ' ') . map (!!i)
-- readBucket i [] = []
-- readBucket i (row:rows) | row!!i == ' ' = []
--                         | otherwise = c:readBucket i rows
--                         where
--                             c = row!!i

readInstructions :: [String] -> [(Int, Int, Int)]
readInstructions = map readInstruction

readInstruction :: String -> (Int, Int, Int)
readInstruction input = (amount, bucketA, bucketB)
    where
        grab = span (/= ' ')
        (_, _:rest0) = grab input
        (part0, _:rest1) = grab rest0
        amount = read part0
        (_, _:rest2) = grab rest1
        (part1, _:rest3) = grab rest2
        bucketA = read part1
        (_, _:part2) = grab rest3
        bucketB = read part2
