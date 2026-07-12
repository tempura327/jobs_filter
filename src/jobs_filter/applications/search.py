from jobs_filter.mappers.search import SearchJobsMapper
from jobs_filter.schemas.search import SearchJobsResponse


class SearchJobsApplication:
  def __init__(self, one_o_four_service, cake_service):
    self.one_o_four = one_o_four_service
    self.cake = cake_service

  def execute(self, req) -> SearchJobsResponse:
    # 轉換成各個service需要的payload
    one_o_four_payload = SearchJobsMapper.to_one_o_four_service(req)
    cake_payload = SearchJobsMapper.to_cake_service(req)

    one_o_four_result = self.one_o_four.search(one_o_four_payload)
    cake_result = self.cake.search(cake_payload)

    return [*one_o_four_result, *cake_result]
