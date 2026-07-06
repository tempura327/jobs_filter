from fastapi import APIRouter, Depends

from jobs_filter.schemas.search import SearchJobsPayload, SearchJobsResponse
from jobs_filter.applications.search import SearchJobsApplication

# https://fastapi.tiangolo.com/zh-hant/tutorial/path-params/
router = APIRouter()


def get_search_service():
  return SearchJobsApplication(
    # TODO: 把services放進來
  )


@router.post('search', response_model=SearchJobsResponse, description='撈多平台的職缺')
async def search_jobs(
  req: SearchJobsPayload, app_service: SearchJobsApplication = Depends(get_search_service)
) -> SearchJobsResponse:
  # 因為需要搜多個平台API做整合，所以透過mapper做payload的整理，並用application layer來控制流程
  return app_service.execute(req)
