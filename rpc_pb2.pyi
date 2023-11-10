from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["id", "interface", "money", "clock", "bank_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    BANK_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    interface: str
    money: int
    clock: int
    bank_id: int
    def __init__(self, id: _Optional[int] = ..., interface: _Optional[str] = ..., money: _Optional[int] = ..., clock: _Optional[int] = ..., bank_id: _Optional[int] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ["id", "interface", "result", "balance", "clock"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    interface: str
    result: str
    balance: int
    clock: int
    def __init__(self, id: _Optional[int] = ..., interface: _Optional[str] = ..., result: _Optional[str] = ..., balance: _Optional[int] = ..., clock: _Optional[int] = ...) -> None: ...

class Req(_message.Message):
    __slots__ = ["stop"]
    STOP_FIELD_NUMBER: _ClassVar[int]
    stop: bool
    def __init__(self, stop: bool = ...) -> None: ...

class Rep(_message.Message):
    __slots__ = ["stopped"]
    STOPPED_FIELD_NUMBER: _ClassVar[int]
    stopped: bool
    def __init__(self, stopped: bool = ...) -> None: ...
