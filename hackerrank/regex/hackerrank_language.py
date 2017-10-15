# https://www.hackerrank.com/challenges/hackerrank-language

import re

languages = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"

n = int(input())

for i in range(n):
    string = input()
    if re.search(r"(:{}:|^{}:|:{}$)".format(string.split()[1], string.split()[1], string.split()[1]), languages):
        print("VALID")
    else:
        print("INVALID")
