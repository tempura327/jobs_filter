from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import List, Literal, TypedDict

from jobs_filter.constants.area import nested_cities_and_districts, Country


class SalaryType(str, Enum):
  day = 'D'
  year = 'Y'
  month = 'M'


def extract_ids(data_list: List[Country], init_value=[]) -> list[str]:
  ids = [*init_value]

  for item in data_list:
    target_key = next((key for key, value in item.items() if isinstance(value, list)), None)

    if 'id' in item:
      ids.append(item['id'])

    if target_key:
      ids = [*ids, *extract_ids(item[target_key])]

  return ids


# https://pydantic.dev/docs/validation/latest/examples/custom_validators/
class SearchJobsPayload(BaseModel):
  title: str
  district_ids: list[str] | None = Field(default=None, description='城市或區域的代號')
  min_salary: float = Field(100, gt=0)
  salary_type: SalaryType = Field(default=SalaryType.month, description='年薪或月薪')
  is_negotiation_acceptable: bool = Field(default=True, description='是否接受面議')
  page: int

  @field_validator('district_ids', mode='after')
  @classmethod
  def check_districts(cls, value: list[str]) -> list[str]:
    area_ids = extract_ids(nested_cities_and_districts, [])

    invalid_ids = set(value) - set(area_ids)

    if len(invalid_ids) > 0:
      raise ValueError(f'The following areas are invalid: {", ".join(invalid_ids)}')

    return value


class JobData(BaseModel):
  title: str
  company: str
  link: str
  min_salary: float | None
  max_salary: float | None
  salary_type: SalaryType | None


class SearchJobsResponse(BaseModel):
  data: list[JobData]
  page: int
  page_size: int


class OneOFourOrderField(int, Enum):
  MostRelated = 15
  Latest = 16
  CompetitiveSalary = 13


class OneOFourSearchPayload(TypedDict):
  area: List[str] | None
  jobsource: str
  keyword: str
  mode: str
  order: OneOFourOrderField
  scmin: float
  # 0 means only jobs which it is non-negotiable salary should be shown.
  scneg: Literal[0, 1]
  scstrict: Literal[0, 1]
  sctp: SalaryType
  page: int
  page_size: int


class OneOFourJobLinks(TypedDict):
  job: str
  cust: str
  applyAnalyze: str


class OneOFourPageInfo(TypedDict):
  count: int
  currentPage: int
  lastPage: int
  total: int


class OneOFourSearchMetadata(TypedDict):
  pagination: OneOFourPageInfo


class OneOFourSearchData(TypedDict):
  appearDate: str
  custName: str
  description: str
  jobAddress: str
  jobAddrNo: str
  jobAddrNoDesc: str
  jobName: str
  jobType: int
  lat: float
  lon: float
  link: OneOFourJobLinks
  # salary type
  # 10: unknown
  # 40: day
  # 50: month
  # 60: year
  s10: int
  salaryLow: float
  salaryHigh: float


class OneOFourSearchResponse(TypedDict):
  metadata: OneOFourSearchMetadata
  data: list[OneOFourSearchData]


class CakeOrderField(str, Enum):
  popularity = 'popularity'
  Latest = 'latest'


class CakeSearchFilter(TypedDict):
  locations: list[str] | None


class CakeSearchPayload(TypedDict):
  query: str
  filters: CakeSearchFilter | None
  sort_by: CakeOrderField
  page: int
  per_page: int
