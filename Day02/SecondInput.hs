module Day02.SecondInput where

import Day02.Hand ( Hand(Rock, Paper, Scissors), stronger, weaker )

readInput :: [String] -> [(Hand, Hand)]
readInput = map readHands

readHands :: String -> (Hand, Hand)
readHands s = (left, right)
    where 
        left = readHand $ head s
        right = inverse left $ last s

readHand :: Char -> Hand
readHand 'A' = Rock
readHand 'B' = Paper
readHand 'C' = Scissors

inverse :: Hand -> Char -> Hand
inverse left 'X' = weaker left
inverse left 'Y' = left
inverse left 'Z' = stronger left
