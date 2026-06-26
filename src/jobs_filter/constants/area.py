taipei_districts = [
  {'id': '6001001001', 'full': 'Zhongzheng District, Taipei City, Taiwan'},
  {'id': '6001001002', 'full': 'Datong District, Taipei City, Taiwan'},
  {'id': '6001001003', 'full': 'Zhongshan District, Taipei City, Taiwan'},
  {'id': '6001001004', 'full': 'Songshan District, Taipei City, Taiwan'},
  {'id': '6001001005', 'full': 'Daan District, Taipei City, Taiwan'},
  {'id': '6001001006', 'full': 'Wanhua District, Taipei City, Taiwan'},
  {'id': '6001001007', 'full': 'Xinyi District, Taipei City, Taiwan'},
  {'id': '6001001008', 'full': 'Shilin District, Taipei City, Taiwan'},
  {'id': '6001001009', 'full': 'Beitou District, Taipei City, Taiwan'},
  {'id': '6001001010', 'full': 'Neihu District, Taipei City, Taiwan'},
  {'id': '6001001011', 'full': 'Nangang District, Taipei City, Taiwan'},
  {'id': '6001001012', 'full': 'Wenshan District, Taipei City, Taiwan'},
]

new_taipei_districts = [
  {'id': '6001002001', 'full': 'Wanli District, New Taipei City, Taiwan'},
  {'id': '6001002002', 'full': 'Jinshan District, New Taipei City, Taiwan'},
  {'id': '6001002003', 'full': 'Banqiao District, New Taipei City, Taiwan'},
  {'id': '6001002004', 'full': 'Xizhi District, New Taipei City, Taiwan'},
  {'id': '6001002005', 'full': 'Shenkeng District, New Taipei City, Taiwan'},
  {'id': '6001002006', 'full': 'Shiding District, New Taipei City, Taiwan'},
  {'id': '6001002007', 'full': 'Ruifang District, New Taipei City, Taiwan'},
  {'id': '6001002008', 'full': 'Pingxi District, New Taipei City, Taiwan'},
  {'id': '6001002009', 'full': 'Shuangxi District, New Taipei City, Taiwan'},
  {'id': '6001002010', 'full': 'Gongliao District, New Taipei City, Taiwan'},
  {'id': '6001002011', 'full': 'Xindian District, New Taipei City, Taiwan'},
  {'id': '6001002012', 'full': 'Pinglin District, New Taipei City, Taiwan'},
  {'id': '6001002013', 'full': 'Wulai District, New Taipei City, Taiwan'},
  {'id': '6001002014', 'full': 'Yonghe District, New Taipei City, Taiwan'},
  {'id': '6001002015', 'full': 'Zhonghe District, New Taipei City, Taiwan'},
  {'id': '6001002016', 'full': 'Tucheng District, New Taipei City, Taiwan'},
  {'id': '6001002017', 'full': 'Sanxia District, New Taipei City, Taiwan'},
  {'id': '6001002018', 'full': 'Shulin District, New Taipei City, Taiwan'},
  {'id': '6001002019', 'full': 'Yingge District, New Taipei City, Taiwan'},
  {'id': '6001002020', 'full': 'Sanchong District, New Taipei City, Taiwan'},
  {'id': '6001002021', 'full': 'Xinzhuang District, New Taipei City, Taiwan'},
  {'id': '6001002022', 'full': 'Taishan District, New Taipei City, Taiwan'},
  {'id': '6001002023', 'full': 'Linkou District, New Taipei City, Taiwan'},
  {'id': '6001002024', 'full': 'Luzhou District, New Taipei City, Taiwan'},
  {'id': '6001002025', 'full': 'Wugu District, New Taipei City, Taiwan'},
  {'id': '6001002026', 'full': 'Bali District, New Taipei City, Taiwan'},
  {'id': '6001002027', 'full': 'Tamsui District, New Taipei City, Taiwan'},
  {'id': '6001002028', 'full': 'Sanzhi District, New Taipei City, Taiwan'},
  {'id': '6001002029', 'full': 'Shimen District, New Taipei City, Taiwan'},
]

nested_cities_and_districts = [
  {
    'id': '6001000000',
    'full': 'Taiwan',
    'cities': [
      {
        'id': '6001001000',
        'full': 'Taipei City, Taiwan',
        'short': 'TPE',
        'districts': taipei_districts,
      },
      {
        'id': '6001002000',
        'full': 'New Taipei City, Taiwan',
        'short': 'NWT',
        'districts': new_taipei_districts,
      },
      # TODO: 只先準備了雙北的資料，其餘縣市待補
    ],
  }
]
