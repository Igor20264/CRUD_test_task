# AUTOGENERATED FROM 'queries/get_password.edgeql' WITH:
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
class GetPasswordResult(NoPydanticValidation):
    id: uuid.UUID
    password: str


async def get_password(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> GetPasswordResult | None:
    return await executor.query_single(
        """\
        select User {password}
        filter User.id = <uuid>$id\
        """,
        id=id,
    )