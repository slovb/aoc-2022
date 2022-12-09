module Day09.Position ( Position, distance, areAdjacent, followPositions ) where

import Day09.Direction ( Direction(..) )

type Position = (Int, Int)

distance :: Position -> Position -> Int
distance (x, y) (u, v) = abs (u - x) + abs (v - y)

areAdjacent :: Position -> Position -> Bool
areAdjacent (x, y) (u, v) = abs(u - x) <= 1 && abs(v - y) <= 1

followPositions :: [Position] -> Position -> [Position] -> [Position]
followPositions past _ [] = past
followPositions past headPrevious (p:ps) = do
    let current = last past
    if areAdjacent p current then
        followPositions past p ps
    else
        followPositions (past ++ [headPrevious]) p ps
