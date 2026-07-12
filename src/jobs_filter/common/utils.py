def get_query_string(payload: dict):
  query_string = ''

  for key, value in payload.items():
    if isinstance(value, list):
      query_string = f'{query_string}&{key}={"%2C".join(value)}'
    else:
      query_string = f'{query_string}&{key}={value}'

  return f'https://www.104.com.tw/jobs/search/api/jobs?{query_string}'
