module Day09.Direction ( Direction (..), readDirection ) where

data Direction = UP | DOWN | LEFT | RIGHT deriving (Show)

instance Read Direction where
    readsPrec _ input = [(dir, rest)]
        where
            (part:rest) = input
            dir = readDirection part

readDirection :: Char -> Direction
readDirection 'U' = UP
readDirection 'D' = DOWN
readDirection 'L' = LEFT
readDirection 'R' = RIGHT
