# AUTOGENERATED FROM 'queries/reset_username.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class ResetUsernameResult(NoPydanticValidation):
    id: uuid.UUID


async def reset_username(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
    username: str,
) -> ResetUsernameResult | None:
    return await executor.query_single(
        """\
        update User
        filter .id = <uuid>$id
        set {
          updated := datetime_of_statement(),
          username := <str>$username
        }\
        """,
        id=id,
        username=username,
    )
