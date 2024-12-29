from typing import Any

import click

class FieldId:
    SEPARATOR: str

    def __init__(
        self,
        command_index: int,
        param_index: int,
        param_type: str,
        click_type: str,
        nargs: int,
        form_type: str,
        name: str,
        key: str | None = None,
    ): ...
    @classmethod
    def from_string(cls, field_info_as_string: str) -> FieldId: ...

class NotSupported(ValueError): ...

class BaseInput:
    param_type_cls: type | None
    def __init__(self, ctx: click.Context, param: click.Parameter, command_index: int, param_index: int) -> None: ...
    def is_supported(self) -> bool: ...
    @property
    def fields(self) -> dict[str, Any]: ...
    @property
    def type_attrs(self) -> dict[str, Any]: ...
    def _to_cmd_line_name(self, name: str) -> str: ...
    def _build_name(self, name: str): ...

class ChoiceInput(BaseInput): ...
class FlagInput(BaseInput): ...
class IntInput(BaseInput): ...
class FloatInput(BaseInput): ...
class FolderInput(BaseInput): ...
class FileInput(BaseInput): ...
class EmailInput(BaseInput): ...
class PasswordInput(BaseInput): ...
class TextAreaInput(BaseInput): ...
class DefaultInput(BaseInput): ...

INPUT_TYPES: list[type]
_DEFAULT_INPUT: list[type]

def get_input_field(ctx: click.Context, param: click.Parameter, command_index, param_index) -> dict[str, Any]: ...