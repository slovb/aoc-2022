module Day05.Input ( readBuckets, readInstructions ) where

readBuckets :: [String] -> [[Char]]
readBuckets input = do
    let rows = init input
    let n = length (head rows) `div` 4
    [readBucket (i * 4 + 1) rows | i <- [0..n]]

readBucket :: Int -> [String] -> [Char]
readBucket i = filter (/= ' ') . map (!!i)

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
