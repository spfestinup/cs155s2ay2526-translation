"""
CS 155 S2 AY2526
8 May 2026 Lab: AST to three-address code (TAC) translator
Fill in the TODO sections.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Int:
    value: int


@dataclass
class Var:
    name: str


@dataclass
class BinOp:
    left: object
    op: str
    right: object


@dataclass
class Assign:
    name: str
    expr: object


@dataclass
class Print:
    expr: object


@dataclass
class Seq:
    stmts: List[object]


@dataclass
class If:
    cond: object
    then_branch: object
    else_branch: object


@dataclass
class While:
    cond: object
    body: object


temp_counter = 0
label_counter = 0


def reset_counters():
    global temp_counter, label_counter
    temp_counter = 0
    label_counter = 0


def fresh_temp() -> str:
    global temp_counter
    temp_counter += 1
    return f"t{temp_counter}"


def fresh_label(prefix: str = "L") -> str:
    global label_counter
    label_counter += 1
    return f"{prefix}{label_counter}"


def translate_expr(expr, out: List[str]) -> str:
    if isinstance(expr, Int):
        # TODO: create a fresh temporary, emit "temp = literal", return the temp
        pass

    if isinstance(expr, Var):
        # TODO: variables can usually be used directly
        pass

    if isinstance(expr, BinOp):
        # TODO:
        # 1. translate left
        # 2. translate right
        # 3. create a fresh temp
        # 4. emit "temp = left op right"
        # 5. return the temp
        pass

    raise TypeError(f"Unknown expression node: {type(expr).__name__}")


def translate_stmt(stmt, out: List[str]) -> None:
    if isinstance(stmt, Assign):
        # TODO: translate the expression, then emit "name = value"
        return

    if isinstance(stmt, Print):
        # TODO: translate the expression, then emit "print value"
        return

    if isinstance(stmt, Seq):
        # TODO: translate each statement in order
        return

    if isinstance(stmt, If):
        # TODO:
        # - translate condition
        # - make else and end labels
        # - emit conditional branch
        # - translate then branch
        # - jump to end
        # - emit else label
        # - translate else branch
        # - emit end label
        return

    if isinstance(stmt, While):
        # TODO:
        # - create start and end labels
        # - emit start label
        # - translate condition
        # - emit conditional exit
        # - translate body
        # - jump back to start
        # - emit end label
        return

    raise TypeError(f"Unknown statement node: {type(stmt).__name__}")


def generate_tac(program) -> List[str]:
    reset_counters()
    out: List[str] = []
    translate_stmt(program, out)
    return out


# Suggested test program
program = Seq([
    Assign("x", Int(3)),
    Assign("y", BinOp(Var("x"), "+", BinOp(Int(4), "*", Int(2)))),
    Print(Var("y")),
])

if __name__ == "__main__":
    tac = generate_tac(program)
    for line in tac:
        print(line)
