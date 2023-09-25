# AUTOGENERATED FROM 'queries/delete_user.edgeql' WITH:
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
class DeleteUserResult(NoPydanticValidation):
    id: uuid.UUID


async def delete_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
    name: str,
) -> DeleteUserResult | None:
    return await executor.query_single(
        """\
        delete User
        filter .id = <uuid>$id and .username = <str>$name\
        """,
        id=id,
        name=name,
    )