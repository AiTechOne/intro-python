# Tarea 2:

# 1. Guardar en una variable el largo de la lista original e imprimirla.
# 2. Encontrar todos los tipos de datos de la lista y crear sublistas con estos datos. PISTA -> Son 5 sublistas.
# 3. Imprimir el largo de cada sublista generada: Ejemplo: "Se encontraron 200 datos de tipo decimal", "Se encontraron 20 datos de tipo boolean", etc.
# 4. Buscar el número entero mayor y menor de la lista de enteros e imprimirlo.
# 5. Calcular la suma de todos los elementos de tipo int e imprimir.
# 6. Buscar el número decimal mayor y menor de la lista de decimales de la lista e imprimirlo.
# 7. Calcular la suma de todos los elementos de tipo float e imprimir.
# 8. Buscar el string más corto de la lista. Almacenarlo en una variable y luego imprimirlo e imprimir su número de caracteres.
# 9. Buscar el string más largo de la lista. Almacenarlo en una variable y luego imprimirlo e imprimir su número de caracteres.
# 10. BONUS: crear una lista nueva que tenga N valores de cada sublista siendo N el largo de la sublista más corta encontrada (del punto 3).
# Ejemplo: si hay 10 elementos de tipo None, entonces crear una lista con 50 elementos, teniendo 10 de None, 10 enteros, decimales.. etc.

import random


lista = [
    15456.3,
    4779,
    'XtsWdn',
    'eYJcFQ',
    'dUrBVc',
    'LGdkAeC',
    9324.8,
    15434,
    True,
    6913,
    10335,
    6283,
    False,
    106.2,
    15793,
    12094.7,
    36,
    11510,
    12465,
    False,
    14546.0,
    'PEKIOMybAxtMt',
    10101,
    10701.7,
    8461.2,
    'ZzmlmDrcujJxq',
    False,
    'vmlvJW',
    3620.0,
    11479,
    8237.0,
    2608,
    17497,
    10691,
    5181.9,
    'pPUX',
    None,
    9122,
    True,
    5121,
    True,
    12934,
    7416,
    'uSrwPK',
    'sYnsBGsBoHdhI',
    'dyVdsQklUmlgX',
    10799.6,
    None,
    9042,
    'pEkvgu',
    'cIVLdBPClr',
    2054,
    4831,
    5211,
    None,
    1470.4,
    4741,
    17868.1,
    11172.0,
    652.9,
    None,
    'IlBGHt',
    8840,
    'AZKzeJ',
    'SsnaaP',
    None,
    15993.1,
    9495,
    1125,
    'eURGiC',
    980,
    12845.0,
    False,
    4255.1,
    'PMmNPI',
    10820,
    2221.6,
    'DPXDPiL',
    3487,
    True,
    9453,
    12083,
    12019,
    'KHuSwd',
    'jLXuUO',
    11940.3,
    True,
    'PtyLmP',
    None,
    8115.9,
    6344,
    False,
    'jtgAKDzODy',
    10724,
    2981,
    False,
    18948,
    'TnLeYP',
    5445.0,
    10126,
    4921,
    'HjCvaD',
    'kbeS',
    True,
    9927,
    'gbhOxdYefnMCh',
    15217.6,
    3204,
    9999.4,
    447.3,
    'lntCVq',
    6476,
    17074.6,
    'PNrANY',
    3725,
    None,
    4052.2,
    13446,
    11066,
    'jguYpn',
    None,
    None,
    False,
    8535.4,
    19804,
    8196,
    4511.8,
    18750,
    9965,
    False,
    None,
    None,
    8933,
    1853.6,
    None,
    6658,
    9868,
    73,
    7767,
    12348,
    4520,
    'VDKrVf',
    False,
    11690,
    'ztessf',
    'OxKuAf',
    469,
    'ePoSSc',
    3334,
    None,
    14700,
    2045,
    7067.7,
    True,
    None,
    False,
    13410,
    None,
    15028.0,
    19571.6,
    9200,
    1537,
    15454,
    14846.7,
    False,
    'KQtnAQ',
    None,
    3989,
    'riaJgr',
    False,
    'wXGasehIpz',
    8341,
    8977.0,
    12269.0,
    7609.1,
    'gHOlAt',
    'VuhxCu',
    17133.4,
    'zAyEIASptcfhh',
    6210,
    11526.4,
    True,
    1314,
    4031.4,
    None,
    10656.6,
    14313,
    9163.4,
    None,
    12756.7,
    15125.1,
    'btojrK',
    5187.8,
    8276,
    None,
    False,
    'GcLSHP',
    None,
    18462,
    11459,
    5253,
    'MfVPek',
    15333.8,
    19700,
    14510,
    True,
    2294,
    3344.8,
    None,
    None,
    16614.2,
    True,
    None,
    'qYhKAxq',
    'xpUM',
    14289.3,
    9086,
    None,
    7984.2,
    18405.0,
    2126.1,
    11794,
    19892,
    None,
    13387,
    335,
    True,
    10921.0,
    None,
    'OPUWjw',
    None,
    8234,
    'WlnoUw',
    None,
    19858.7,
    None,
    19684,
    14596,
    None,
    3311.8,
    19585,
    False,
    2845,
    'NynhPjg',
    'icCyoSAthfm',
    6814,
    19994,
    False,
    9815,
    None,
    False,
    12055.3,
    None,
    7140,
    False,
    15568.4,
    'XjwBQq',
    10191,
    8855,
    4590,
    3179,
    None,
    13162,
    186,
    'gOoDgWXmDn',
    5384,
    None,
    4629,
    None,
    15705.6,
    4762,
    857,
    17246.7,
    17817,
    False,
    None,
    3038,
    'NEOfaF',
    False,
    None,
    7562,
    7502.4,
    4517.2,
    17985,
    18184.3,
    9226,
    16226.0,
    'AQBCQt',
    'cSmhqC',
    True,
    3155.0,
    1970.1,
    17716.6,
    9616.1,
    'yrHiwn',
    False,
    'OsayqplhZM',
    False,
    False,
    'MVutsZ',
    1366,
    12021,
    True,
    12368.0,
    16805,
    'JCRXInrCbmzTN',
    15623,
    False,
    14054.5,
    'gyul',
    9183,
    False,
    299.5,
    1790,
    4894,
    18807,
    'hSOpTc',
    None,
    16777,
    None,
    True,
    None,
    'BIIEgB',
    False,
    2752,
    5067.1,
    11042.3,
    4754,
    'WjKXQLT',
    1198.1,
    16570,
    13002,
    17695,
    None,
    12077.8,
    None,
    True,
    5399,
    'wrDHQy',
    'fHicsi',
    18317.3,
    19619,
    'GKRjOo',
    'UZnTxH',
    'FKYetl',
    'tvzxjs',
    1774,
    None,
    5324,
    12169,
    16267,
    8148,
    False,
    7539,
    14864,
    19885.2,
    6516.2,
    'YGbbAkiDXo',
    None,
    15289,
    17136,
    None,
    19519.5,
    4333.7,
    'htEcqlhlUzu',
    'oxHqRm',
    14794,
    False,
    'lpcWxO',
    5512,
    'stFhBR',
    3558,
    'oEmPCM',
    False,
    False,
    'NtNg',
    13071,
    4829.3,
    'EzWudpL',
    14772.4,
    7425.9,
    'QpmMNRuJBEprO',
    'auOHst',
    6342,
    'crppEGZ',
    2292.4,
    'TebaSRMqwnYKC',
    17374,
    3388,
    None,
    None,
    'BadxkAK',
    834.3,
    'ZCosfgGayJKxR',
    754,
    14812,
    6008,
    None,
    'tGqOwjNGXQ',
    'OWYHnr',
    7676,
    'ooNGlfoHYJAeu',
    None,
    6969,
    None,
    15894,
    None,
    4949,
    'GevW',
    4171.0,
    'UGQILJw',
    1536,
    2319,
    'wiJYFs',
    None,
    None,
    18932,
    6757,
    11580,
    'rPtnPD',
    9464,
    'cGewSh',
    11773,
    5574,
    'KQitWU',
    False,
    7277.0,
    16596,
    12988,
    None,
    True,
    'PJJsgmOsat',
    'hFErTO',
    11284,
    5072.8,
    'OrotnzynWtA',
    352,
    None,
    False,
    17766.5,
    13298,
    2758,
    160,
    4991,
    'vfqQYM',
    13456,
    15334,
    'KOpJdgx',
    'LmTOPu',
    None,
    'CWfj',
    16835,
    19954.9,
    None,
    'rBEMSlxBfdBqg',
    'SVjvHJNhMH',
    15167,
    False,
    'qzifjTH',
    True,
    'PzYPvcpMlNJvG',
    'igAWpa',
    198,
    'kORyiPjGwVEFQ',
    False,
    137,
    16093.6,
    None,
    False,
    18249.4,
    None,
    6521.4,
    None,
    14882.6,
    13041,
    None,
    None,
    'OpKBov',
    'PCSnHJ',
    14156,
    'TIQWia',
    12616,
    None,
    True,
    19894.6,
    'StSfPA',
    'veiC',
    'WhqwVf',
    'qEDDzc',
    2987,
    16939.1,
    3627.8,
    16931.8,
    10342,
    19539.4,
    None,
    6786,
    'sCioJU',
    None,
    'ITFznzIlMNRaa',
    True,
    'trXtBs',
    'DzeCCN',
    17185.9,
    6812,
    8743,
    11191,
    4740.3,
    'JWodeqWKrt',
    None,
    False,
    14379,
    5009,
    'xdGuCd',
    19220,
    17112,
    None,
    'rLTZrjHihKZ',
    7321,
    'JaNDmu',
    15295,
    None,
    5958.4,
    False,
    16028,
    None,
    17243,
    None,
    True,
    True,
    None,
    9610,
    'fJDG',
    18015,
    9367,
    'klSsSm',
    None,
    'vHTVmS',
    'TRMClM',
    14013,
    None,
    None,
    12490.0,
    19389.8,
    3039,
    17086.7,
    14564.4,
    False,
    None,
    13265.2,
    11638,
    None,
    3522.3,
    'aDHlHIG',
    16313,
    None,
    None,
    'YUIDKh',
    None,
    None,
    None,
    5041,
    True,
    'XuHEyu',
    10333,
    13097,
    'oRvAdH',
    None,
    False,
    15378,
    14028,
    'xqoKjz',
    12836,
    9682.6,
    'MaYJzb',
    14617,
    True,
    'QmHPkr',
    3756,
    10750,
    'QYHEDW',
    'cftnYxf',
    5207.6,
    'XlXysk',
    False,
    10237.2,
    'YwOiYocALsilq',
    True,
    18535,
    None,
    18051,
    'nQJmpY',
    False,
    19272,
    5310.0,
    'zPgRBq',
    None,
    13032.7,
    None,
    'BPOmfC',
    17546,
    'UAJgHMfmKbMjW',
    15607.3,
    7114,
    None,
    None,
    None,
    17210,
    17082,
    'DgShUmCCcWzjR',
    415,
    5227.5,
    None,
    18569.4,
    'UxLUyF',
    False,
    True,
    False,
    False,
    'nwiakn',
    19595,
    True,
    None,
    'lYxltlhyiKWfa',
    8457.5,
    17664.4,
    'uIEedl',
    17722,
    4318,
    False,
    6549.5,
    13269.9,
    'ZGnibkG',
    False,
    'YFBhJvPcJsxpu',
    9367.3,
    10482.2,
    14383,
    'osRHfsvdlI',
    'kOVMst',
    3953.7,
    'qvflUtkwnVQ',
    None,
    'NHvrtw',
    18293,
    None,
    19294,
    19642.6,
    'vVmeaD',
    2246,
    10493,
    None,
    7666,
    'PtObrE',
    6648,
    7320,
    11341.4,
    75.4,
    13175,
    'tDKyvc',
    'GJXIef',
    16049.5,
    'aHTcWA',
    False,
    4732,
    False,
    True,
    8693.8,
    None,
    'SHAtke',
    8754,
    4787,
    12928.2,
    10499,
    'uSmJGW',
    'kPrdLA',
    None,
    'KpjUDQuncLlkM',
    'zifHFO',
    13383.5,
    18749.3,
    12063,
    'yCFsDEwCTt',
    19914.0,
    None,
    8319.8,
    None,
    10797.8,
    6544,
    10763,
    True,
    'YgUGxboHXoIUK',
    2087,
    6728,
    15767,
    False,
    5752,
    2204,
    None,
    False,
    None,
    17879.2,
    4289.6,
    'CrgNsf',
    None,
    'NUjeiH',
    1094.8,
    8113,
    12371,
    False,
    'FUQbbp',
    6915.9,
    8733,
    17885.5,
    False,
    True,
    13256,
    8206,
    'zZfgrByTXFELm',
    11388.3,
    'WFnYgE',
    17238,
    'kCaUkk',
    'iXUfzjuqtUgoK',
    1999.5,
    None,
    14853,
    2635,
    'PsSzLL',
    19107,
    1944.4,
    19680,
    12521,
    1052.7,
    False,
    6009,
    'ozCObUxzeKxAV',
    17853,
    6061.5,
    16027,
    18592,
    True,
    None,
    'iBFWWc',
    'SQYrNW',
    False,
    1393,
    18474,
    18560,
    8829,
    False,
    None,
    1071,
    12502,
    True,
    13659,
    1169.3,
    'QEHoaqCdcAv',
    'RMuEpCpxZK',
    12575,
    9589,
    None,
    2325,
    9929.7,
    'SGFQHtwNkgMHg',
    'acETvn',
    None,
    5498.4,
    'EdJdlRj',
    False,
    'urMvquF',
    16359.3,
    None,
    None,
    'iQxcxC',
    4210,
    6613,
    False,
    'VtibxN',
    None,
    3241,
    7113.0,
    'yMSPdJ',
    15687,
    9429.6,
    'kkdoqtaapQxUa',
    'qXBnIQ',
    14183,
    8212,
    False,
    10347.3,
    19997,
    None,
    6188,
    None,
    False,
    'HQBpVS',
    False,
    11700,
    17460,
    8845,
    2071,
    None,
    False,
    18623.8,
    None,
    True,
    'PiDBDvfDzyYpl',
    'VEOTHiesRTMzA',
    'sfvtyb',
    'rgytFo',
    None,
    18599,
    18482,
    10037,
    16112,
    4868.5,
    8559,
    'ugDoXA',
    18620.9,
    4934.6,
    'dytnZEzsfEXZM',
    None,
    'FfbbXki',
    None,
    7924.2,
    13098.1,
    10805,
    10866.3,
    False,
    None,
    None,
    15324,
    False,
    None,
    'ZjiNGb',
    None,
    False,
    18461,
    3917.4,
    17806.8,
    'CxhoBt',
    14278.4,
    'vKYFlZgLuhlVE',
    7236,
    'NrBqbw',
    'ZeUmeK',
    10956.0,
    18641,
    358,
    17059,
    'YhALuYGBRoz',
    7594,
    'kItsXx',
    17726,
    1515.0,
    True,
    None,
    2160,
    'FLpbJmjvRzRGd',
    18710.9,
    None,
    'qbZIzI',
    4571.1,
    'zlMDJwsghM',
    14743,
    1281,
    8984,
    14709.3,
    'vwsrkt',
    12201,
    'lGCfbX',
    False,
    'uSxUBa',
    19244,
    'IhTvsCLqYUG',
    'KjBSKgugpqTEt',
    None,
    'ZHwvZqVLiWe',
    'EovefkSqNVKQf',
    18903,
    False,
    7135,
    19612.0,
    'AFqTHq',
    19905,
    13527.5,
    False,
    7391.2,
    None,
    'tbAkNy',
    204,
    11336,
    19829,
    None,
    None,
    None,
    16378,
    19440,
    True,
    'cLAIXxCkrfpJE',
    14976,
    12477.8,
    4758.0,
    'SkSFRz',
    'bbSQsr',
    'gKQRun',
    17679,
    5483.7,
    19001.4,
    16629,
    None,
    13008,
    8804,
    'ooJqWbRoha',
    None,
    None,
    12661,
    'KUjHAK',
    3544,
    5436,
    None,
    'VnxdDG',
    None,
    12150,
    18381,
    None,
    6626.7,
    17104,
    16547,
    None,
    True,
    'dtOGet',
    False,
    'OTaLOw',
    6350,
    940,
    19877,
    19597.8,
    'OFaNeib',
    'APLZzP',
    None,
    9979,
    None,
    'HMOl',
    'GCdaDpwmMI',
    'NYmIdME',
    17889,
    8019,
    9208.1,
    False,
    False,
    None,
    'Chiekr',
    'pgBW',
    15460,
    1255.3,
    129.8,
    4549.8,
    None,
    16400,
    False,
    2825,
    None,
    12103,
    14915,
    14108,
    'HhPZLVSENPu',
    13564,
    16176,
    5010,
    'LtDbpD',
    16532,
    None,
    False,
    True,
    6205,
    983,
    None,
    False,
    'WZvbwZ',
    3221,
    False,
    False,
    'AELkJG',
    17900,
    'skFnZz',
    None,
    5775,
    'qnHZAj',
    False,
    None,
    'ieELdd',
    4303,
    2051.8,
    14789,
    13993.7,
    8049,
    8000,
    16416.8,
    19595.2,
    3018.1,
    'dXaViG',
    None,
    13728,
    'emFFFnmmPq',
    12959,
    17269.3,
    7822,
    667,
    4518,
    None,
    False,
    16496.7,
    12894,
    16477,
    'RQgOfajThz',
    13087.6,
    'MTQXSCVDXz',
    'PowAVE',
    None,
    'AgEFvz',
    4599,
    None,
    12952,
    'QuVwdc',
    'mjnhyVQxRJbxR',
    9645,
    'wrppMF',
    11272,
    1767,
    17921,
    False,
    'rLVNPjV',
    None,
    10356.1,
    17234,
    12403,
    10495,
    15770,
    'omqxbd',
    18787.9,
    'dQdxGPgFVyBXp',
    'uLQwgU',
    True,
    8472,
    2421,
    17633,
    3476.8,
    False,
    9169.7,
    14105,
    168.0,
    'bKtXaF',
    'JgtB',
    'YLaUHMY',
    None,
    6321.4,
    2011,
    None,
    3399.5,
    None,
    4927.2,
    None,
    13371.6,
    1183,
    None,
    'KZmDEC',
    9994,
    'TxqMVb',
    'PtMOYZOnSfNHf',
    7091,
    3596,
    'kpXQIxRkfI',
    10403,
    'NsdA',
    2820,
    'VgfqHwtalrK',
    None,
    18260,
    None,
    'rEFajgOiPF',
    1207,
    1940,
    13618.6,
    449.6,
    7531.6,
    6823,
    19494,
    False,
    15600,
    'VUOFVqrnVGa',
    11497.8,
    15381.5,
    None,
    'zFvmMs',
    4872,
    10724.0,
    11761,
    11202.1,
    15526.3,
    'icVywADMUO',
    6319.9,
    True,
    'cKRXdp',
    'rVNfGx',
    'bxzjta',
    11439,
    1496,
    'kndwIpftWzFph',
    False,
    'lEvx',
    1269,
    False,
    None,
    4983,
    'fWPBZW',
    4298,
    None,
    None,
    None,
    16463,
    580,
    4267.2,
    15470,
    11760.9,
    12324.1,
    None,
    None,
    10177,
    5278.9,
    18594,
    'IXvBzl',
    8778.5,
    13848,
    'vPDmfS',
    'mKxzgro',
    True,
    4276.0,
    None,
    3024.9,
    'futnAKr',
    True,
    'ZXUOYx',
    19793,
    4973,
    'PcpAiKIqfRc',
    'ZknTGe',
    17184.8,
    'pzfRFs',
    None,
    None,
    None,
    4737,
    15016,
    11251.4,
    12296,
    5801,
    None,
    17819,
    1911,
    'VZYiVgAadfvXF',
    False,
    11882.8,
    9337,
    'awmiek',
    14303,
    None,
    7745,
    False,
    False,
    15893.0,
    9559,
    19662,
    12229,
    11075,
    None,
    False,
    6433,
    18516.6,
    False,
    9985.1,
    'wHyUdq',
    8558,
    15408,
    17336.5,
    None,
    'CMwAAXvUdKG',
    'CBI',
    15662.0,
    8098.5,
    'TYKXBA',
    6012,
    18429,
    'ZHdFCrRjvy',
    'aEDJdPrTkaUkq',
    None,
    14119,
    'wkfujIHHNUxuK',
    15171,
    5391.0,
    'QpZViH',
    'UHhLsj',
    4405,
    True,
    'nySbpb',
    'mkgCZW',
    5058.2,
    4768,
    True,
    5368.9,
    None,
    'JQLbpm',
    7043.7,
    9389,
    4153,
    False,
    None,
    17505.9,
    15529,
    'UyBwZP',
    6359,
    None,
    11958.4,
    True,
    14284.5,
    False,
    False,
    7277.2,
    None,
    18645.9,
    13516.2,
    967,
    None,
    'HuOJ',
    1517.3,
    14687.0,
    'XeTfDB',
    3519,
    False,
    None,
    None,
    15044,
    False,
    None,
    False,
    12519,
    14991,
    None,
    2241,
    1773.5,
    5639,
    2962,
    7429.5,
    2781.8,
    'vnakovBWciSHv',
    19867,
    'akGpDOe',
    19532.2,
    6735.6,
    2805.1,
    False,
    'srPY',
    4945.7,
    13529,
    'VbmgmuWgYw',
    None,
    3819,
    2823,
    11695,
    False,
    'xoGsKK',
    False,
    11311,
    None,
    1872.9,
    'iCDaJz',
    False,
    19770.7,
    2940.8,
    'mmxWDm',
    'xsowbcK',
    'hmuxLSZphtBBE',
    'CpRslRGIQFfok',
    None,
    'fgwS',
    None,
    7636,
    False,
    13672,
    16816.2,
    None,
    'pcEQBQ',
    None,
    3054,
    5858,
    13733,
    14107.5,
    'HFAKWR',
    'BRsAOsHfcSD',
    14819,
    16370.3,
    4681.7,
    3672,
    None,
    13952,
    None,
    'AnyQpx',
    17698.0,
    False,
    11403,
    'hvCvMV',
    402,
    None,
    True,
    4404.9,
    17924,
    'rFIAFg',
    3237.4,
    14344.2,
    False,
    18733,
    True,
    None,
    11561,
    3118,
    7862.0,
    8776,
    16384,
    'RGrBeGkDkS',
    False,
    8137.9,
    'nvESLe',
    False,
    'oNcstI',
    False,
    'OdqDsxarVijpt',
    16268.9,
    False,
    None,
    4313,
    3830,
    'sFseko',
    None,
    16849,
    'hFiyNm',
    'RROHDBymWb',
    10280,
    3050,
    True,
    3353,
    None,
    None,
    'UbvGFf',
    True,
    1541,
    False,
    14148.4,
    1597.0,
    5788,
    1897,
    'dblJsu',
    4976.5,
    None,
    'vDqYDt',
    'NOyndW',
    False,
    None,
    1542,
    'IcbRCrx',
    8596.1,
    None,
    'uhPekl',
    None,
    None,
    'okjtkq',
    'iDTk',
    18642,
    True,
    None,
    None,
    2528.2,
    'sKQXQl',
    True,
    5580,
    'PHXbbT',
    9160,
    None,
    4300,
    'gNlyLroEMvl',
    None,
    13653,
    False,
    9280,
    13681.4,
    10279.2,
    2986.4,
    13903,
    16953,
    'xksJvo',
    737.8,
    16338,
    'lkJbVau',
    18667,
    'SWEQHg',
    13696.3,
    17962,
    None,
    False,
    2184,
    None,
    'yEsxYa',
    'PADnySPOCNd',
    'DmQMlo',
    16824,
    665.6,
    19911,
    False,
    None,
    12171,
    'FSTiro',
    6936,
    'LxzFjwA',
    15963,
    10869,
    14724,
    10470.4,
    1044,
    3153.6,
    10748,
    5051,
    None,
    13366,
    'VbnaadtEpP',
    False,
    11817.8,
    'NwLMvz',
    18204.7,
    'CepeVra',
    'BFhkpbChtsY',
    12525.8,
    3486,
    19672,
    16076,
    14338,
    'wLSTTN',
    False,
    'ssDd',
    11383,
    None,
    19632.4,
    2808.3,
    None,
    False,
    'fFkdmyI',
    695.1,
    'zERvjKS',
    7916,
    'MCKUGXCyfK',
    19594.4,
    None,
    'pViSbiQ',
    1394,
    False,
    None,
    9972.8,
    'LMGCTOvcUpHrF',
    'Yeaciy',
    19069.2,
    13117.7,
    'kXaRxb',
    19389,
    4416,
    18512.9,
    False,
    16117,
    11330,
    None,
    686,
    5312,
    False,
    18758,
    1171.3,
    'fAIKPH',
    None,
    False,
    None,
    12966,
    None,
    None,
    10083.5,
    16643.6,
    12231,
    6570,
    14325,
    17499,
    False,
    'VqdyZf',
    2516.7,
    8027,
    'rFeE',
    17530,
    10609.2,
    'hgsNKfcalvfhg',
    'mJoMHg',
    5818.0,
    8098.5,
    None,
    12480,
    3287.9,
    'NRArrd',
    'HuLflZjHYynnj',
    1723.3,
    4172.3,
    'dSEwEijuIGxdM',
    3967,
    'SrgvLK',
    'XfAdPY',
    10192.8,
    16914,
    'CTryLZ',
    False,
    2217.9,
    None,
    7758,
    5521,
    5281,
    18930.7,
    13702,
    19085,
    True,
    6733,
    None,
    12034.0,
    14947,
    11086,
    19,
    'aytQsU',
    9291.5,
    None,
    7235,
    19872,
    15252.1,
    'gCJX',
    1379,
    True,
    'WCojFAeicTH',
    'pyFyrHCmdGwfg',
    'GyNk',
    None,
    None,
    False,
    'Snywsm',
    17912,
    'GlGzgURuRkuKy',
    True,
    False,
    6145,
    None,
    'OgYYki',
    2251.3,
    False,
    None,
    7058,
    'DsGsGJ',
    False,
    None,
    'GVnACy',
    2822,
    'DEqD',
    18276,
    2271,
    'xFCMKK',
    19757.5,
    9428,
    'CqaeLtEFtW',
    5243,
    'KYdfLLt',
    19805,
    None,
    'yNhz',
    11414,
    'GEvHiYklxxk',
    True,
    'GdxLSC',
    'tHjCOQOqXA',
    14502,
    1997,
    19890,
    'GmLJFh',
    11543.1,
    False,
    'aAVuebhWcrVqH',
    None,
    None,
    3175,
    'TDmoEa',
    18291,
    9948,
    19701,
    False,
    True,
    False,
    4908.3,
    None,
    11550,
    True,
    11488,
    18664,
    None,
    14828,
    7559,
    8144,
    3783.2,
    True,
    18362,
    3544.2,
    4419,
    17292,
    3994,
    15497,
    8343,
    14881,
    2566,
    12096.1,
    18533,
    3330,
    18363,
    18621,
    False,
    'SODmGG',
    'CMdRiIDRsnWcq',
    False,
    6751.9,
    5779.6,
    9480,
    2802.2,
    None,
    11028,
    'JvLCQx',
    373,
    'lTzlWkOsra',
    None,
    7716,
    'nmCX',
    560,
    'JlSLeN',
    False,
    1893,
    9955.9,
    12425.8,
    327,
    10467,
    5321,
    'HSlYBb',
    12898.0,
    'wTAJeE',
    8992,
    False,
    False,
    15795,
    'UAkz',
    'xrfPgE',
    4485,
    12653.4,
    'SERyeK',
    19638,
    14550,
    13688,
    None,
    'VDCKtv',
    'gugywF',
    12899.1,
    17938.4,
    9765.4,
    14517.9,
    'qgqmhaEsfZ',
    10963,
    100,
    None,
    9738,
    14076,
    True,
    3605.8,
    True,
    'fpaDXd',
    'QpkBVn',
    False,
    1776,
    7605,
    2213,
    3471.6,
    'CiGumx',
    'ljrCLSDaLZWJP',
    7803.0,
    'uOrRzg',
    1895,
    'HPwLhII',
    True,
    'YsyxXrnUGMicu',
    14350,
    4701,
    None,
    9828,
    None,
    5498,
    5029.2,
    4297.0,
    17265,
    None,
    12768,
    1560,
    10887.9,
    12933.2,
    11273,
    'uufSPr',
    4941,
    'TGvxPj',
    14755.1,
    11332.0,
    7662,
    19534,
    13592,
    'YqXSrI',
    'yfVgEv',
    'YeJxvi',
    'oCHIBH',
    True,
    'hwXZwT',
    4483,
    'aYkuQc',
    7261,
    'QcBiEwh',
    9110.1,
    12256,
    3383,
    True,
    'knkwJMbXCHUhY',
    5304,
    19502,
    378,
    648,
    18007.9,
    13370,
    None,
    'KqVpGc',
    1876,
    534.1,
    11167,
    13183,
    1533,
    5906,
    'XjMGcfeEfaL',
    None,
    6768,
    479,
    13771,
    5267.9,
    False,
    15688,
    'hGPMvJxNVe',
    True,
    'xWQwvs',
    5492,
    5099,
    19090.9,
    'wJmNAU',
    None,
    None,
    1600,
    17094,
    9902.7,
    True,
    None,
    'isvVZfshATPHGNgHAitPkWIUB',
    6655,
    'NdSGRj',
    9111.4,
    5112,
    13123,
    75,
    False,
    11106,
    14261.7,
    'NhJEGmAxCFy',
    11616.6,
    None,
    None,
    16973,
    16390.1,
    None,
    'AbhTFpEEQH',
    19458,
    False,
    6803.8,
    5809.0,
    'DwpEZVq',
    3951,
    411.2,
    8138,
    4630,
    17204,
    True,
    14004,
    1729.9,
    'sJod',
    1182,
    'eQQYeB',
    'mjDCSQ',
    2776,
    'hmBjGZ',
    'HYNOWi',
    5874.0,
    10832,
    16407,
    None,
    18232,
    11855,
    2078.9,
    1171,
    3354.4,
    'KFBaTn',
    None,
    63.6,
    18554,
    1027,
    14483.3,
    18922.0,
    4821.7,
    17481,
    'ySVuaUihDC',
    None,
    False,
    'NbnTrd',
    15078,
    2828,
    8585,
    10147,
    'LPsXWzD',
    'cMcFbg',
    6724.9,
    True,
    4598.9,
    False,
    'jXDcufFWEVtGu',
    None,
    None,
    'jEgAWy',
    3243,
    16551.6,
    13203,
    'XzzJAf',
    None,
    5875,
    13321.7,
    None,
    16471.3,
    2366,
    12011,
    8750,
    5994.2,
    19850,
    8746,
    'CxATGkgkpLVib',
    14930.1,
    11987.0,
    'arwEGNxkrWE',
    7152.6,
    'bKYTemkGTgR',
    False,
    10157,
    2727,
    None,
    False,
    'OLYECl',
    'zvbWmgWrGdQfS',
    9136.7,
    'FOyDvK',
    19633.2,
    3978,
    4188,
    9420.6,
    'ODEIUx',
    'DbivgKvFykgqC',
    'hspvpX',
    'QTTKnX',
    5654,
    None,
    'aXZXrQgFJHjjV',
    6578,
    'wHWBwcYXCw',
    'ycEgwb',
    2781.7,
    4957,
    'SmHLxvbhKm',
    109,
    'KAUp',
    False,
    'KxtvIWEGlt',
    'pCYrQqedNy',
    'ScugXHgSFCNPX',
    True,
    'HdGonSY',
    None,
    None,
    2819,
    13597,
    'wHnqJM',
    'hhbvDR',
    5271.0,
    14695.6,
    18342.7,
    'RzKorTXjhQXFL',
    False,
    False,
    13370.9,
    7981.1,
    17740,
    7424.5,
    'DZsvOVV',
    18673.0,
    None,
    5678.8,
    6255.5,
    2695.6,
    'qzuhOd',
    4496,
    'cvgLgs',
    12198,
    2255.7,
    None,
    None,
    727,
    1667,
    None,
    19767,
    17084,
    'fnmxod',
    'DkXjTM',
    18792.6,
    10148.4,
    'BCwZzBV',
    7524.9,
    False,
    16512.9,
    15493,
    False,
    True,
    5559,
    'bHYKPFRxJxtIi',
    13019,
    None,
    15808,
    'EVluqlxsLv',
    11682,
    None,
    None,
    11094,
    12263,
    17537,
    8818.9,
    19825,
    6957.6,
    'yZAGdk',
    11198,
    19883.8,
    10650,
    'iYlCAYEIQn',
    741.6,
    15899,
    9275.7,
    None,
    'HSOkLY',
    7198.5,
    5981.1,
    3825.4,
    None,
    19419,
    19340,
    'elNj',
    466,
    9912.9,
    14753.3,
    'krQjsp',
    'btgFdlGEvA',
    4759,
    'yQrLUw',
    19907,
    6992,
    16242,
    14809.3,
    11976,
    9166,
    15057,
    4641,
    6258.6,
    16543,
    18592.4,
    6723,
    9453.2,
    13364.9,
    11926,
    6946,
    10364,
    9856,
    13036,
    None,
    651.6,
    16872.0,
    13712,
    16167,
    'vtPiVD',
    12193,
    'ymzqThqEoX',
    13034.6,
    8577,
    False,
    143.8,
    None,
    None,
    None,
    'GOcgaLEBgJ',
    6524.1,
    14417,
    'vebYaJ',
    'aOZXQx',
    'EdpyCF',
    19313,
    10151.5,
    None,
    16110,
    'nebc',
    'MJKcVC',
    17719,
    5356,
    'RRcjBpP',
    'Qoqlzo',
    7226.8,
    False,
    'iIFDbh',
    14324,
    2625.4,
    6960,
    'MIMzRhVIDQvaW',
    True,
    19664.7,
    14735,
    True,
    9960,
    3583.3,
    19067,
    8621,
    6335.9,
    14966.7,
    False,
    'jnFriXwsCc',
    'MUSecM',
    'wHdUXf',
    'LLiumE',
    15321.7,
    11528,
    10348,
    None,
    12080,
    8652.3,
    'dGhGraNDBW',
    'pskLtH',
    None,
    16432,
    14563,
    7315.8,
    'fhTmcqpSgPiLq',
    10785.1,
    8698.1,
    'LngMyJ',
    2289,
    None,
    None,
    'MtwDefGKPVWaE',
    15544,
    'exSLfawJbl',
    None,
    None,
    16972,
    13399,
    'QAgtBHfbheYFn',
    4625,
    'seHP',
    False,
    13636,
    None,
    'BcaOIiv',
    'rMgJxX',
    'RDkCkO',
    16103.8,
    None,
    7730.9,
    'pksUBs',
    None,
    'GenDxQ',
    19804.1,
    'TSXqos',
    False,
    'FKfGzq',
    None,
    14525,
    680,
    'ikuIpdmIqwKFclJdXnDnxJAEYc',
    None,
    None,
    18650,
    None,
    11439.5,
    'xHNzrG',
    12729.0,
    'KZlLteVpHaNxq',
    11248.6,
    None,
    18253.1,
    10481,
    'lRRDVLdiaL',
    8481,
    None,
    10163.7,
    'pghaca',
    'SQlkJz',
    False,
    'veFuIQ',
    None,
    19228,
    'jhPTnd',
    'BDdQOO',
    'hVUPga',
    'dhrrzrSdSs',
    None,
    False,
    12274,
    'tyakMp',
    None,
    'TWvMFmN',
    'JSQCkYdzlc',
    6873,
    'FvmfltS',
    5873.0,
    True,
    18439.0,
    'LnoRlt',
    False,
    'SMWX',
    'rfdLHm',
    11172.7,
    14560.6,
    13325,
    False,
    'FqrS',
    329,
    'PyrFwIHQnxeen',
    'kpjQWz',
    'fRXUuV',
    False,
    None,
    'qPqzRl',
    7272,
    None,
    None,
    17087,
    7589.0,
    18843,
    6749.5,
    'BPFXAL',
    None,
    None,
    'tXohqRleEg',
    12079,
    7880.6,
    4066,
    10219,
    False,
    'qumWJMoiBp',
    None,
    'TBBLUH',
    9132.1,
    1505.3,
    'pQBZgU',
    12132,
    7169,
    False,
    'gNWxLt',
    19871.6,
    19775.7,
    'xiCFvy',
    6473.9,
    8464.3,
    False,
    11198.4,
    None,
    8872,
    9808.0,
    8618.9,
    'MUBRsi',
    17796,
    17197.3,
    10877,
    'kEfgOVqpGbT',
    None,
    'rhwHODjLrAFse',
    'ASFQVZ',
    False,
    5049,
    6346.1,
    'NzVPoRjOkxdUU',
    7655.3,
    2324,
    2444.9,
    True,
    3736.1,
    8494,
    'vjqaTt',
    'Dfctte',
    'kQzFnV',
    10952,
    19838,
    1493.7,
    18923,
    7385,
    None,
    11925,
    'bIJbHj',
    14103,
    'fuRyrl',
    'mfRxKs',
    7748,
    1629,
    9144,
    'mGryCpW',
    True,
    406.9,
    11213,
    11250,
    9544,
    None,
    'wlvscB',
    10490,
    None,
    None,
    'UttcaORwyy',
    None,
    None,
    'HMhFQd',
    17365,
    4718,
    17608.1,
    'eCojuNNkxKq',
    8819,
    18356,
    16669,
    3186,
    None,
    12892,
    False,
    19797.5,
    None,
    'qfLPCVseNI',
    4560,
    3976,
    5834,
    None,
    None,
    16919,
    'hDWujx',
    None,
    'Owmcgd',
    None,
    'GBxCPZ',
    4885,
    'IpHFBIspnEn',
    17609,
    'dKrwhT',
    'NYDWJX',
    None,
    None,
    13662.8,
    3410,
    'BHLGQk',
    9654,
    False,
    1495.7,
    3304.4,
    True,
    'HyQXxW',
    None,
    8163.5,
    14523.2,
    'Qkwgvp',
    12536,
    None,
    16111,
    7029.5,
    'LUTUyH',
    7429,
    None,
    'BEZedM',
    5335,
    None,
    19808,
    18037,
    7555,
    'euheIrJWABq',
    None,
    'ttiaex',
    True,
    None,
    False,
    'Qned',
    8102,
    True,
    None,
    True,
    5078.9,
    18820,
    4587.9,
    6520,
    True,
    3496,
    3625,
    'xNxjwb',
    'sVlFYUItGh',
    17015,
    True,
    15040,
    True,
    848.4,
    'ZziTPEKHnOZQL',
    None,
    16742,
    None,
    2156.8,
    1492.4,
    4375,
    12494.5,
    None,
    None,
    'fNgMwlI',
    18900.1,
    None,
    19824,
    14790,
    14945,
    2224,
    13149,
    9340,
    'QIrwPqIJZqQba',
    None,
    5867.0,
    'NbFDiHbSFfWPH',
    17480.8,
    'PzFoNZ',
    6471.7,
    'dXbteX',
    9178,
    10312,
    7053,
    13171,
    'FNFIqZFucc',
    'BfvrLRAACknFM',
    False,
    'jMCPmN',
    None,
    None,
    9690,
    'reXcOg',
    16402,
    10891,
    7107.4,
    13464,
    True,
    6162,
    'xYCwvBTovIVFY',
    'EJXoQO',
    8675,
    4182.6,
    'WOpnJl',
    None,
    'whrDwNSAxWlXo',
    18241.1,
    'KLXYJlMWGGOPE',
    10986,
    'kndeYt',
    12006,
    13102,
    403,
    'TnFQdE',
    17567.4,
    18547.5,
    18517,
    3624,
    False,
    10542.5,
    6911.8,
    3256.6,
    False,
    653,
    'gtVvHI',
    None,
    'mJUsfr',
    12501,
    12602.6,
    14590,
    4846,
    'VXBbfA',
    6342.6,
    'zPQDGH',
    4693,
    6509,
    19850.3,
    'TEPGgk',
    'gnSWTMCOCxpyo',
    'zWRW',
    6531,
    6753,
    None,
    'BQPejYYUuqzNp',
    7039,
    None,
    None,
    None,
    19939,
    1818,
    17589,
    8754.1,
    None,
    True,
    'NMrj',
    'qPUaZazmRQMBH',
    'WcPfXw',
    7155,
    'IuXcRCi',
    'EHaTue',
    1144.9,
    18881.9,
    'kUqmSrHLpsPiM',
    None,
    4945.1,
    19434.3,
    19091,
    'YhqnDdWztEzzi',
    7454.0,
    'VgvOddJynESnq',
    7972,
    False,
    False,
    None,
    None,
    'QFQvjxqqAfI',
    6101,
    'UmDRQz',
    False,
    'eAMOFlzJkDTpV',
    3454.3,
    'OhGHFB',
    19826.2,
    6903.4,
    7736,
    5312.6,
    15930,
    None,
    15018.5,
    None,
    1815.2,
    5117,
    12887.3,
    None,
    None,
    None,
    7727.5,
    False,
    13767,
    7337.1,
    16720,
    8484,
    12416.3,
    None,
    3270,
    5550.6,
    None,
    9040.3,
    16796.8,
    5433,
    None,
    12996.1,
    4446,
    False,
    None,
    5793,
    13290,
    6923,
    12687,
    7651.8,
    3528,
    'LfQBZBanIBkfg',
    4381,
    1556,
    'xads',
    True,
    'qSSCCv',
    1170,
    7544.4,
    True,
    17366.2,
    'HxpNrm',
    None,
    860,
    17237.3,
    None,
    'dHaeDQ',
    True,
    'hVeyKGiWfq',
    'nYCPZYrUWdP',
    True,
    10032.1,
    1950,
    'ElBKCh',
    'vgjqck',
    5902,
    'VEaWvML',
    None,
    12015.3,
    4070,
    None,
    17221,
    10715.8,
    9621.6,
    6294,
    None,
    10155,
    None,
    False,
    3666,
    17280,
    8164.0,
    None,
    2557,
    7774,
    10138.0,
    None,
    10221,
    False,
    'AxRRGWgKiY',
    'UDxijVfnKD',
    'vEOEGM',
    14620,
    19432.1,
    'mrXlZy',
    'HOYVsb',
    True,
    19547,
    4226,
    7237.8,
    'pHcWVcWjWe',
    'lXunAptvHK',
    1062,
    2941,
    8945,
    18220,
    6559,
    True,
    6762.7,
    14594.1,
    19509.0,
    9316,
    422,
    'xCffAE',
    'rvDpqM',
    True,
    18446,
    None,
    13107.1,
    8104.1,
    None,
    'csIIos',
    10260,
    18340.8,
    'JiJV',
    None,
    19864,
    False,
    None,
    'EWNosB',
    'xgIXve',
    2603,
    None,
    15361,
    None,
    'NrTG',
    False,
    None,
    'aTxVvO',
    1246,
    8815.6,
    15961,
    10769,
    16021.5,
    13459.2,
    3253,
    15730.7,
    'HvxqjkL',
    None,
    False,
    'MprAQA',
    'pKEeqV',
    6876.4,
    10007,
    7051.0,
    3376.0,
    15848.5,
    7351,
    'rugsot',
    14087,
    'wAaVqJ',
    None,
    'eWCdlLg',
    'PpktRY',
    937.3,
    None,
    'jKQBza',
    'DHTnrg',
    9349.8,
    False,
    11819,
    1524,
    'pEEQszE',
    None,
    1068.5,
    1606.6,
    18384.7,
    12766,
    'ITejkokJJp',
    'vAQbQv',
    5405,
    None,
    14305,
    11400,
    7943,
    6904,
    'YtvyZD',
    None,
    'RHDYNMrMVCIqr',
    False,
    'zROqnN',
    None,
    None,
    10919,
    None,
    'gRIZlA',
    'VovZDN',
    'jibfUg',
    14087.7,
    None,
    'XXyWMe',
    19848.6,
    3594.0,
    15005,
    6754,
    'PQPRYx',
    False,
    12505,
    12925,
    'hBEMav',
    'YJJMbh',
    None,
    1369.9,
    11625,
    6519,
    True,
    None,
    10843.0,
    None,
    5368.4,
    'cKXRdE',
    11393,
    963.1,
    12962,
    3247.1,
    4464.9,
    None,
    'MomlEz',
    'VBsueomHJW',
    3627,
    5191,
    12058,
    True,
    'AIAEWs',
    328,
    12691,
    14333.3,
    None,
    12461,
    18045,
    True,
    None,
    18698,
    9726.9,
    9761,
    None,
    10449,
    18191,
    False,
    3169.5,
    15209,
    None,
    'jwNaql',
    True,
    11508.2,
    'WteFbg',
    8604,
    17973.5,
    False,
    7143,
    14299.5,
    14385,
    'IluzCEjIcemad',
    5391.6,
    10733.7,
    'XigAAVfJJjQHQ',
    7269,
    'VliOAN',
    1129,
    12887.0,
    7884,
    10719.5,
    8595.8,
    9807.0,
    False,
    'zsCLmi',
    1874.9,
    2104,
    11254.6,
    'ZtonXs',
    7446,
    3154,
    None,
    'zISMhHc',
    None,
    19564,
    True,
    2494,
    18408,
    18665,
    19015,
    5627.4,
    8452.9,
    5555,
    None,
    107,
    'gggydx',
    'XoQlIE',
    8445,
    8523,
    14736,
    None,
    18555.4,
    'zblqwU',
    False,
    'dBeIKS',
    13015.2,
    15451.5,
    None,
    True,
    'jsQDBm',
    5229,
    False,
    None,
    'ducdrcLgmi',
    6605.6,
    16749,
    15256,
    14520,
    'GbeSkX',
    2063.0,
    None,
    7089,
    14319,
    'YYHXwC',
    'XNfmYI',
    13474,
    -13.700000000000003,
    'rXZt',
    False,
    10551,
    'kwKNtt',
    None,
    None,
    10294,
    11603,
    'MkjHaK',
    None,
    19729,
    6560,
    3183.0,
    'gWQYIJ',
    11532,
    'qfHhdhhIiPLci',
    'vRzB',
    'NxZaVNPMBcJ',
    'nsUwGy',
    6948,
    12878,
    'FACfFC',
    False,
    'wwYJpw',
    'akur',
    11378,
    9370,
    19830.2,
    4317,
    False,
    'FcigAZN',
    None,
    'NgURYK',
    11211,
    True,
    18170.1,
    None,
    2236.7,
    12545,
    438,
    True,
    'ojZXvwfXZEi',
    True,
    True,
    'QGLrqp',
    'rwGeeA',
    'ICTc',
    None,
    'IIlmRImFkC',
    18425,
    4069,
    3930.3,
    'ctVmQnU',
    7248.3,
    11033.5,
    3462.6,
    7710.3,
    321,
    19625,
    'EfuRvv',
    4826.0,
    17872.8,
    False,
    19092.1,
    'evOfMM',
    497,
    11396,
    False,
    None,
    12114,
    None,
    18512.1,
    14085,
    7677.3,
    515,
    299.4,
    17978,
    5882,
    None,
    18809,
    'EPpaHx',
    False,
    10132,
    1623,
    'UFdDDh',
    10278,
    False,
    7480,
    3574,
    10561,
    12870,
    6633,
    False,
    13137,
    'bLgCwNm',
    'hsbITE',
    False,
    'XqsiPu',
    15303,
    13372,
    'FXhZMI',
    15249,
    10043,
    8655,
    12927,
    'kjageA',
    12454.5,
    4700.9,
    'kiJGAl',
    14621,
    'pVgkfYIjCiLOn',
    True,
    'NppZeC',
    'kplEoB',
    'HgoXMd',
    True,
    675,
    14317,
    3331,
    12134,
    None,
    11248,
    'KWYNOz',
    8499,
    'YBhMWFuYkJQnC',
    None,
    14584,
    None,
    18588,
    9307.2,
    6931,
    10529,
    4851,
    'gawnPOjzmc',
    'vhSvxU',
    None,
    9158,
    None,
    None,
    'rYkgma',
    None,
    None,
    18471.3,
    'PdbFqk',
    12921,
    None,
    9118,
    None,
    'CrEsHE',
    7434,
    19612,
    6297,
    None,
    'EpgfNFfxEkM',
    None,
    'PengZK',
    14149,
    15708,
    15043,
    9820,
    3606,
    'lcLIlK',
    None,
    'qgjptm',
    False,
    False,
    'LedbgvurTLBfd',
    False,
    6343,
    'QlhJSpHLfHboM',
    'aipIUG',
    179,
    12938.4,
    True,
    False,
    False,
    None,
    768,
    17382,
    'gSzJeUi',
    None,
    11132,
    None,
    False,
    None,
    938.3,
    19451.9,
    None,
    6353,
    4301,
    15861,
    7309,
    'nHyoup',
    10503.4,
    5867,
    3556,
    4056,
    True,
    18544,
    12855.3,
    13300,
    False,
    15654,
    4920,
    'FyML',
    'zmziEtu',
    5713,
    'TkEedA',
    None,
    True,
    18207,
    None,
    None,
    False,
]

####Comienzo
largo_lista = len(lista)
print(f"La lista contiene los siguientes elementos: {largo_lista}")

lista_str = []
lista_int = []
lista_float = []
lista_bool = []
lista_NoneType = []

palabra_mas_corta = "dsadsadsadsadsadasdasdsadsadsadsadsadsadsa"
palabra_mas_larga = ""

entero_menor = 100000000
entero_mayor = -100000000
suma_enteros = 0

decimal_menor = 1000000000000000000000000000.0
decimal_mayor = -100000000000000000000000000.0
suma_decimal = 0.0

asignar_primer_decimal = True

for variable in lista:
    if type(variable) is str:
        lista_str.append(variable)
        if len(variable) < len(palabra_mas_corta):
            palabra_mas_corta = variable
        if len(variable) > len(palabra_mas_larga):
            palabra_mas_larga = variable

    elif type(variable) is int:
        lista_int.append(variable)
        suma_enteros += variable
        if variable > entero_mayor:
            entero_mayor = variable
        if variable < entero_menor:
            entero_menor = variable

    elif type(variable) is float:
        lista_float.append(variable)
        if asignar_primer_decimal == True:
            asignar_primer_decimal = False
            decimal_menor = variable
            decimal_mayor = variable

        suma_decimal += variable
        if variable > decimal_mayor:
            decimal_mayor = variable
        if variable < decimal_menor:
            decimal_menor = variable

    elif type(variable) is bool:
        lista_bool.append(variable)

    elif variable == None:
       lista_NoneType.append(variable)

largo_lista_str = len(lista_str)
print(f"Se encontraron {len(lista_str)} datos de tipo str")

largo_lista_int = len(lista_int)
print(f"Se encontraron {len(lista_int)} datos de tipo int")

largo_lista_float = len(lista_float)
print(f"Se encontraron {len(lista_float)} datos de tipo float")

largo_lista_bool = len(lista_bool)
print(f"Se encontraron {len(lista_bool)} datos de tipo bool")

largo_lista_NoneType =  len(lista_NoneType)
print(f"Se encontraron {largo_lista_NoneType} datos de tipo NoteType ")

print(f"El numero entero mayor es: {entero_mayor} y el numero entero menor es: {entero_menor}")
print(f"La suma total de enteros es: {suma_enteros}")

print(f"El numero decimal mayor es: {decimal_mayor} y el numero decimal menor es: {decimal_menor}")
print(f"La suma total de decimales es: {suma_decimal}")

print(f"la palabra mas corta es: {len(palabra_mas_corta)} {palabra_mas_corta}")
print(f"la palabra mas larga es: {len(palabra_mas_larga)} {palabra_mas_larga}")

lista_nueva = lista_str[:300] + lista_float[:300] + lista_bool[:300] + lista_int[:300] + lista_NoneType[:300]
print(f"La lista nueva contiene: {len(lista_nueva)} datos")