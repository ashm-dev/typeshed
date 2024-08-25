from _typeshed import Incomplete
from functools import partial
from typing import Final

DEBUG: Final[bool]
SCRAMBLE_LENGTH: Final[int]
sha1_new: partial

def scramble_native_password(password: str | bytes | None, message: str | bytes | None) -> bytes: ...
def _my_crypt(message1: str | bytes, message2: str | bytes) -> bytes: ...

_nacl_bindings: bool

def _init_nacl() -> None: ...
def _scalar_clamp(s32: bytes) -> bytearray: ...
def ed25519_password(password: str | bytes, scramble: str | bytes) -> bytes: ...
def _roundtrip(conn, send_data: bytes): ...
def _xor_password(password: bytes, salt: bytes) -> bytes: ...
def sha2_rsa_encrypt(password: bytes, salt: bytes, public_key: bytes) -> bytes: ...
def sha256_password_auth(conn, pkt): ...
def scramble_caching_sha2(password: bytes, nonce: bytes) -> bytes: ...
def caching_sha2_password_auth(conn, pkt) -> Incomplete | None: ...
