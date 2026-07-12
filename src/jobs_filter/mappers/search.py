from jobs_filter.schemas.search import (
  SearchJobsPayload,
  OneOFourSearchPayload,
  CakeSearchPayload,
  OneOFourOrderField,
  CakeOrderField,
)
from jobs_filter.constants.area import nested_cities_and_districts, Country, City, District

PER_PAGE = 50

ONE_O_FOUR_JOB_SOURCE = 'joblist_search'
ONE_O_FOUR_SEARCH_MODE = 's'
ONE_O_FOUR_IS_STRICT = 1


class SearchJobsMapper:
  @staticmethod
  def to_one_o_four_service(req: SearchJobsPayload) -> OneOFourSearchPayload:
    return {
      'area': req.district_ids,
      'jobsource': ONE_O_FOUR_JOB_SOURCE,
      'keyword': req.title,
      'mode': ONE_O_FOUR_SEARCH_MODE,
      # 15代表以符合度排序
      'order': OneOFourOrderField.Latest,
      'scmin': req.min_salary,
      # 0為排除面議
      'scneg': int(req.is_negotiation_acceptable),
      'scstrict': ONE_O_FOUR_IS_STRICT,
      'sctp': req.salary_type,
      'page': req.page,
      'pageSize': PER_PAGE,
    }

  def _get_area_name_by_id(data: Country | City | District, target_id: str) -> str:
    if 'id' in data and data['id'] == target_id:
      return data['full']

    if ('cities' not in data) and ('districts' not in data):
      return ''

    target_key = 'cities' if 'cities' in data else 'districts'

    for current_data in data.get(target_key, []):
      found_name = SearchJobsMapper._get_area_name_by_id(current_data, target_id)
      if found_name:
        return found_name
    return ''

  @staticmethod
  def to_cake_service(req: SearchJobsPayload) -> CakeSearchPayload:
    area_fullnames = []

    for id in req.district_ids or []:
      area_name = SearchJobsMapper._get_area_name_by_id(nested_cities_and_districts[0], id)

      if len(area_name) > 0:
        area_fullnames.append(area_name)

    return {
      # Cake不支援關鍵字中間有空格、逗點
      'query': req.title,
      'filters': {
        'locations': area_fullnames,
      },
      'sort_by': CakeOrderField.Latest,
      'page': req.page,
      'per_page': PER_PAGE,
    }
