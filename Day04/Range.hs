module Day04.Range where

import Data.Char ( isDigit )

data Range = Range {
    start :: Int,
    end :: Int
} deriving (Show)

newRange :: Int -> Int -> Range
newRange s e | s <= e = Range s e
             | otherwise = error "newRange: start must be less than or equal to end"

instance Read Range where
    readsPrec _ input = 
        let (part0, _:rest0) = span isDigit input -- throw away the hyphen
            start = read part0 :: Int
            (part1, rest1) = span isDigit rest0
            end = read part1 :: Int
            in
                [(newRange start end, rest1)]

contain :: Range -> Range -> Bool
a `contain` b = startA <= startB && endA >= endB
    where
        Range startA endA = a
        Range startB endB = b

overlap :: Range -> Range -> Bool
overlap a b = startA <= endB && startB <= endA
    where
        Range startA endA = a
        Range startB endB = b
