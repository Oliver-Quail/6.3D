import sys
import contextlib
from io import StringIO

ALLOWED_FUNCS = {
    "abs": abs,
    "aiter": aiter,
    "all": all,
    "anext": anext,
    "any": any,
    "ascii": ascii,
    "bin": bin,
    "bool": bool,
    # "breakpoint": breakpoint,
    "bytearray": bytearray,
    "bytes": bytes,
    "callable": callable,
    "chr": chr,
    "classmethod": classmethod,
    # "compile": compile,
    "complex": complex,
    "delattr": delattr,
    "dict": dict,
    "dir": dir,
    "divmod": divmod,
    "enumerate": enumerate,
    # "eval": eval,
    # "exec": exec,
    "filter": filter,
    "float": float,
    "format": format,
    "frozenset": frozenset,
    "gettattr": getattr,
    "globals": globals,
    "hasattr": hasattr,
    "hash": hash,
    # "help": help,
    "hex": hex,
    "id": id,
    # "input": input,
    "int": int,
    "isinstance": isinstance,
    "issubclass": issubclass,
    "iter": iter,
    "len": len,
    "list": list,
    "locals": locals,
    "map": map,
    "max": max,
    "memoryview": memoryview,
    "min": min,
    "next": next,
    "object": object,
    "oct": oct,
    # "open": open,
    "ord": ord,
    "pow": pow,
    "print": print,
    "property": property,
    "range": range,
    "repr": repr,
    "reversed": reversed,
    "round": round,
    "set": set,
    "setattr": setattr,
    "slice": slice,
    "sorted": sorted,
    "staticmethod": staticmethod,
    "str": str,
    "sum": sum,
    "super": super,
    "tuple": tuple,
    "type": type,
    "vars": vars,
    "zip": zip,
    # "__import__": __import__,
}


class EncrypterEvalError(Exception):
    pass


class DecrypterEvalError(Exception):
    pass


class DecryptionError(Exception):
    pass

class InvalidAlgorithmError(Exception):
    pass


def _exec(script, stdin):
    """
    Safe Python exec with stdio handing

    Returns the stdout from the python script as a string
    """

    def _input(_a=None):
        return stdin

    output = StringIO()
    loc = {"input": _input}

    with contextlib.redirect_stdout(output):
        exec(script, {"__builtins__": ALLOWED_FUNCS}, loc)

    return output.getvalue().strip()


def test_algorithm(encrypter, decrypter, plaintext):
    """
    Test the algorithm by encrypting then decrypting the given plaintext

    Throws an exception if the encryptor or decryptor cannot be executed or if
    the decrypter is unable to reproduce the plaintext

    On success the cyphertext is returned
    """
    cyphertext = ""

    try:
        cyphertext = _exec(encrypter, plaintext)

        if cyphertext == plaintext:
            raise InvalidAlgorithmError("You algorithm doesn't encrypt the data")

    except Exception as e:
        raise EncrypterEvalError("Failed to execute encrypter: " + str(e))
    try:
        if _exec(decrypter, cyphertext) != plaintext:
            raise DecryptionError(
                "The decrypted cyphertext does not match the original plaintext"
            )
    except Exception as e:
        raise DecrypterEvalError("Failed to execute decrypter: " + str(e))

    return cyphertext


if __name__ == "__main__":
    encrypter = open(sys.argv[1]).read()
    decrypter = open(sys.argv[2]).read()
    print(test_algorithm(encrypter, decrypter, "hello world"))