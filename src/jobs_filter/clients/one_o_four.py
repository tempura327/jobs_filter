import httpx
from fake_useragent import UserAgent

from jobs_filter.schemas.search import OneOFourSearchPayload
from jobs_filter.common.utils import get_query_string

BASE_URL = 'https://www.104.com.tw/'

ua = UserAgent()


class OneOFourClient:
  def __init__(self):
    self.current_page = 0
    self.has_next_page = True

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

  def search(self, payload: OneOFourSearchPayload):
    if not self.has_next_page and payload.page > self.current_page:
      raise Exception('There is no next page.')

    try:
      query_string = get_query_string(payload)
      url = f'{BASE_URL}jobs/search/api/jobs?{query_string}'
      headers = self.__get_headers(url)

      response = httpx.get(url, headers=headers)

      response.raise_for_status()

      data = response.json()
      raw_data = data.get('data', [])

      self.current_page += 1

      if len(raw_data) < payload.page_size:
        self.has_next_page = False

      return raw_data

    except httpx.exceptions.HTTPError as http_err:
      print(f'HTTP Error: {http_err}. {response.text}')

    except Exception as err:
      print(f'Exception: {err}')
