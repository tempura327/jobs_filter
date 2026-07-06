from fastapi import APIRouter

from jobs_filter.schemas.search import SearchJobsPayload, SearchJobResponse

# https://fastapi.tiangolo.com/zh-hant/tutorial/path-params/
router = APIRouter()


# 撈多平台的職缺
@router.post('search', response_model=SearchJobResponse)
async def search_jobs(item: SearchJobsPayload) -> SearchJobResponse:
  # TODO: call service
  return item
