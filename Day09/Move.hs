module Day09.Move ( Move(..), step, walk, journey ) where

import Data.Char ( isDigit )

import Day09.Direction ( Direction(..) )

import Day09.Position ( Position )

data Move = Move Direction Int deriving (Show)

instance Read Move where
    readsPrec _ input = [(Move direction length, rest1)]
        where
            (part0, _:rest0) = span (/= ' ') input -- ignore the space
            direction = read part0 :: Direction
            (part1, rest1) = span isDigit rest0
            length = read part1 :: Int

step :: Position -> Direction -> Position
step (x, y) UP = (x, y - 1)
step (x, y) DOWN = (x, y + 1)
step (x, y) LEFT = (x - 1, y)
step (x, y) RIGHT = (x + 1, y)

walk :: Position -> Move -> [Position]
walk p (Move dir 0) = [p]
walk p (Move dir length) = newP:rest
    where
        newP = step p dir
        rest = walk newP (Move dir (length - 1))

journey :: [Position] -> [Move] -> [Position]
journey past [] = past
journey past (move:moves) = do
    let pos = last past
    let present = walk pos move
    journey (past ++ present) moves
