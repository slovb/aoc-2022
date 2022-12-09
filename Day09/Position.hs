module Day09.Position ( Position, areAdjacent, followPositions ) where

import Day09.Direction ( Direction(..) )

type Position = (Int, Int)

areAdjacent :: Position -> Position -> Bool
areAdjacent (x, y) (u, v) = abs(u - x) <= 1 && abs(v - y) <= 1

followPositions :: [Position] -> [Position] -> [Position]
followPositions past [] = past
followPositions past (p:ps) = do
    let current = last past
    let newP = hop current p -- incorrect
    if areAdjacent p current then
        followPositions past ps
    else
        followPositions (past ++ [newP]) ps

hop :: Position -> Position -> Position
hop (x, y) (u, v)
    | areAdjacent (x, y) (u, v) = (x, y)
    | (u - x) > 0 && (v - y) > 0 = (x + 1, y + 1)
    | (u - x) < 0 && (v - y) > 0 = (x - 1, y + 1)
    | (u - x) > 0 && (v - y) < 0 = (x + 1, y - 1)
    | (u - x) < 0 && (v - y) < 0 = (x - 1, y - 1)
    | (u - x) > 0 = (x + 1, y)
    | (u - x) < 0 = (x - 1, y)
    | (v - y) > 0 = (x, y + 1)
    | (v - y) < 0 = (x, y - 1)
