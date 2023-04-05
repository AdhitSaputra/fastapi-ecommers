from math import ceil
from typing import Generic, TypeVar, Sequence

from fastapi_pagination import Params, Page
from fastapi_pagination.bases import AbstractPage, AbstractParams

DataType = TypeVar("DataType")
T = TypeVar("T")

class PageBase(Page[T], Generic[T]):
    pages: int
    next_page: int | None
    previous_page: int | None

class IResponsePage(AbstractPage[T], Generic[T]):
    message: str = ""
    meta: dict = {}
    data: PageBase[T]

    __params_type__ = Params  # Set params related to Page

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        total: int,
        params: AbstractParams,
    ) -> PageBase[T] | None:
        if params.size is not None and total is not None and params.size != 0:
            pages = ceil(total / params.size)
        else:
            pages = 0

        return cls(
            data=PageBase(
                items=items,
                page=params.page,
                size=params.size,
                total=total,
                pages=pages,
                next_page=params.page + 1 if params.page < pages else None,
                previous_page=params.page - 1 if params.page > 1 else None,
            )
        )


class IGetResponsePaginated(IResponsePage[DataType], Generic[DataType]):
    message: str = "Data got correctly"