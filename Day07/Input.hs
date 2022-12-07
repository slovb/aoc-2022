module Day07.Input ( readInput ) where

import Data.Char ( isDigit )

import Data.List ( isPrefixOf ) 

data MyFiles = EmptyNode
           | MyFile { name :: String, size :: Int }
           | MyFolder { name :: String, children :: [MyFiles] }
           deriving (Show) 

readInput :: [String] -> [MyFiles]
readInput lines = files
    where (files, _) = readLevel ([], lines)

readLevel :: ([MyFiles], [String]) -> ([MyFiles], [String])
readLevel (files, []) = (files, [])
readLevel (files, line:rest)
    | isCdUp line = (files, rest)
    | isCd line = readLevel (files ++ [folder], nextRest)
    | isFile line = readLevel (files ++ [readMyFile line], rest)
    | otherwise = readLevel (files, rest)
    where
        (folder, nextRest) = readMyFolder (line:rest)

isCdUp :: String -> Bool
isCdUp "$ cd .." = True
isCdUp _ = False

isCd :: String -> Bool
isCd line
    | "$ cd " `isPrefixOf` line = True
    | otherwise = False

readMyFolder :: [String] -> (MyFiles, [String])
readMyFolder (line:rest) = (MyFolder folderName children, nextRest)
    where
        folderName = drop 5 line
        (children, nextRest) = readLevel ([], rest)

isFile :: String -> Bool
isFile line
    | all isDigit $ take 1 line = True
    | otherwise = False

readMyFile :: String -> MyFiles
readMyFile line = MyFile name size
    where
        (sizeAsString, _:name) = span (/= ' ') line
        size = read sizeAsString :: Int
