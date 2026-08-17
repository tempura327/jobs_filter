from jobs_filter.mappers.search import SearchJobsMapper
from jobs_filter.schemas.search import SearchJobsResponse
from jobs_filter.services.one_o_four import OneOFourService


class SearchJobsApplication:
  def __init__(self, one_o_four_service: OneOFourService, cake_service):
    self.one_o_four = one_o_four_service
    self.cake = cake_service

  def execute(self, req) -> SearchJobsResponse:
    # 轉換成各個service需要的payload
    one_o_four_payload = SearchJobsMapper.to_one_o_four_service(req)
    cake_payload = SearchJobsMapper.to_cake_service(req)

    one_o_four_res = self.one_o_four.search(one_o_four_payload)
    cake_res = self.cake.search(cake_payload)

    data = [*one_o_four_res.data, *cake_res.data]

    return SearchJobsResponse(
      data=data, page=max(one_o_four_res.page, cake_res.page), page_size=len(data)
    )
