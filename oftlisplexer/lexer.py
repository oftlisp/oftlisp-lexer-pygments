from pygments.lexer import RegexLexer, words
from pygments.token import *

operator_syms = [
    "+", "-", "*", "/", "%", "=", "<", "<=", ">", ">=", "\\", "@", "<-"
]
operator_words = ["lambda", "len", "mod"]
builtins = [
    "assert", "assert-eq", "concat", "cond", "cons", "eq", "first", "fold",
    "head", "if", "last", "list", "map", "nil", "progn", "second", "show",
    "strcat", "tail", "third"
]
decls = [
    "def", "defmacro", "defn", "defvar"
]
namespace = [
    "import", "import-macros", "module"
]

symbol_start_chars = "a-zA-Z+\\./\\$\\?\\*#:=<>_-"
symbol_chars = "0-9" + symbol_start_chars

class OftlispLexer(RegexLexer):
    """A Pygments lexer for OftLisp."""
    name = "OftLisp"
    aliases = ["oftlisp"]
    filename = ["*.oft"]

    tokens = {
        "root": [
            (";.*?$", Comment.Single),
            ("\\s", Whitespace),
            ("'\\([^)]*?\\)", Literal),
            ("'[{}][{}]*".format(symbol_start_chars, symbol_chars), Literal),
            ("[()',`]", Punctuation),
            ("\"([^\"]|\\\")*?\"", String),
            ("\\d+(\\.\\d)?", Number),
            ("[{}][{}]*\\?".format(symbol_start_chars, symbol_chars), Operator.Word),
            (words(operator_syms, suffix="[^{}]".format(symbol_chars)), Operator),
            (words(operator_words, suffix="[^{}]".format(symbol_chars)), Operator.Word),
            (words(builtins, suffix="[^{}]".format(symbol_chars)), Name.Builtin),
            (words(decls, suffix="\\b"), Keyword.Declaration),
            (words(namespace, suffix="\\b"), Keyword.Namespace),
            ("[{}][{}]*".format(symbol_start_chars, symbol_chars), Name)
        ]
    }
