from jobs_filter.schemas.search import (
  SearchJobsPayload,
  OneOFourSearchPayload,
  CakeSearchPayload,
)


PER_PAGE = 50


class SearchJobsMapper:
  @staticmethod
  def to_one_o_four_service(req: SearchJobsPayload) -> OneOFourSearchPayload:
    return {
      # TODO
      'pageSize': PER_PAGE,
    }

  @staticmethod
  def to_cake_service(req: SearchJobsPayload) -> CakeSearchPayload:

    return {
      # TODO
      'per_page': PER_PAGE,
    }
