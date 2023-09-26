# AUTOGENERATED FROM 'queries/get_all_user_booking.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import datetime
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
class GetAllUserBookingResult(NoPydanticValidation):
    id: uuid.UUID
    user_id: GetAllUserBookingResultUserId
    start_time: datetime.datetime
    end_time: datetime.datetime
    comment: str | None


@dataclasses.dataclass
class GetAllUserBookingResultUserId(NoPydanticValidation):
    id: uuid.UUID


async def get_all_user_booking(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
) -> list[GetAllUserBookingResult]:
    return await executor.query(
        """\
        select Booking {user_id,start_time,end_time,comment}
        filter .user_id.id = <uuid>$user_id\
        """,
        user_id=user_id,
    )
