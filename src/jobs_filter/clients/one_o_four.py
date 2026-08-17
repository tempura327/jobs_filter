import httpx
from fake_useragent import UserAgent

from jobs_filter.schemas.search import OneOFourSearchPayload, OneOFourSearchResponse
from jobs_filter.common.utils import get_query_string

BASE_URL = 'https://www.104.com.tw/'

ua = UserAgent()


class OneOFourClient:
  def __init__(self):
    self.current_page = 0
    self.last_page = None

  @staticmethod
  def __get_headers(url):
    return {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Encoding': 'gzip, deflate, br, zstd',
      'Accept-Language': 'en,en-US;q=0.9,zh-TW;q=0.8,zh;q=0.7',
      'Connection': 'keep-alive',
      # 把中文轉unicode，避免keyword有中文時，會報latin-1的錯誤
      'Referer': url.encode('unicode_escape').decode('utf-8'),
      # 防擋爬蟲
      'User-Agent': ua.random,
    }

  def search(self, payload: OneOFourSearchPayload) -> OneOFourSearchResponse | None:
    if self.last_page is not None and payload['page'] > self.last_page:
      raise Exception('There is no next page.')

    try:
      query_string = get_query_string(dict(payload))
      url = f'{BASE_URL}jobs/search/api/jobs?{query_string}'
      headers = self.__get_headers(url)

      response = httpx.get(url, headers=headers)

      response.raise_for_status()

      res: OneOFourSearchResponse = response.json()
      page_info = res['metadata']['pagination']

      self.current_page = page_info['currentPage']

      if self.last_page is None:
        self.last_page = page_info['lastPage']

      return res

    except httpx.HTTPError as http_err:
      raise RuntimeError(f'HTTP Error: {http_err}') from http_err

    except Exception as err:
      raise RuntimeError(f'Exception: {err}') from err
