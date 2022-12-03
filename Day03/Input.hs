module Day03.Input where

readInput :: [String] -> [(String, String)]
readInput = map readSplit

readSplit :: String -> (String, String)
readSplit x = splitAt half x
    where
        half = length x `div` 2
