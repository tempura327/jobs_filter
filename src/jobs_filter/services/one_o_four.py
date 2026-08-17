from jobs_filter.clients.one_o_four import OneOFourClient
from jobs_filter.schemas.search import (
  OneOFourSearchPayload,
  OneOFourSearchResponse,
  JobData,
  SalaryType,
)


class SearchService:
  def __init__(self, one_o_four_client: OneOFourClient):
    self.one_o_four = one_o_four_client

  @staticmethod
  def __filter_valid_jobs(
    data: list[OneOFourSearchResponse], options
  ) -> list[OneOFourSearchResponse]:
    is_negotiation_acceptable = options.get('is_negotiation_acceptable', False)
    base = options.get('base', 0)

    res = []

    for item in data:
      min_val = float(item.get('salaryLow') or 0)
      max_val = float(item.get('salaryHigh') or 0)

      if (is_negotiation_acceptable and min_val == 0 and max_val == 0) or (
        (min_val >= base) or (min_val <= base < max_val)
      ):
        res.append(item)

    return res

  @staticmethod
  def __get_salary_type(typeCode: int) -> SalaryType | None:
    if typeCode == 40:
      return SalaryType.day

    if typeCode == 50:
      return SalaryType.month

    if typeCode == 60:
      return SalaryType.year

    return None

  @staticmethod
  def __format_job(data: OneOFourSearchResponse) -> JobData:
    title = data.get('jobName', '')
    company = data.get('custName', {})

    min_val = float(data.get('salaryLow') or 0)
    max_val = float(data.get('salaryHigh') or 0)

    job_link = data.get('link', {}).get('job')
    salary_type = SearchService.__get_salary_type(data.get('s10', 10))

    return JobData(
      title=title,
      company=company,
      link=job_link,
      min_salary=min_val,
      max_salary=max_val,
      salary_type=salary_type,
    )

  def search(self, payload: OneOFourSearchPayload) -> list[JobData]:
    data = self.one_o_four.search(payload)

    target_jobs = self.__filter_valid_jobs(
      data or [],
      {'is_negotiation_acceptable': bool(payload.get('scneg', 1)), 'base': payload.get('scmin', 0)},
    )
    target_jobs_count = len(target_jobs)

    if target_jobs_count < 1:
      return []

    formatted_jobs = list(map(self.__format_job, target_jobs))

    return formatted_jobs
