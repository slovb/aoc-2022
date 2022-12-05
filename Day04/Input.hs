module Day04.Input ( readInput ) where

import Day04.Range ( Range ) 

readInput :: [String] -> [(Range, Range)]
readInput = map readRanges

readRanges :: String -> (Range, Range)
readRanges input = (firstRange, secondRange)
    where
        (first, _:second) = span (/= ',') input
        firstRange = read first :: Range
        secondRange = read second :: Range
