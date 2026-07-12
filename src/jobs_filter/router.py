from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Literal

# https://fastapi.tiangolo.com/zh-hant/tutorial/path-params/
router = APIRouter()


# 撈多平台的職缺
class SearchJobsPayload(BaseModel):
  title: str
  # TODO: definite const and use it here
  districts: list[str] | None = None
  min_salary: float = Field(100, gt=0)
  max_salary: int | None = Field(default=None, gt=0)
  salary_type: Literal['month', 'year'] = Field(default='month')
  is_negotiation_acceptable: bool = Field(default=True, description='是否接受面議')


@router.post('search')
async def search_jobs(item: SearchJobsPayload):
  # TODO: call service
  return item
