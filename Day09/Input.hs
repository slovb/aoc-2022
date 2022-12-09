module Day09.Input ( readInput ) where

import Day09.Move ( Move(..) )

readInput :: [String] -> [Move]
readInput input = map read input :: [Move]
