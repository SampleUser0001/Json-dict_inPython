# -*- coding: utf-8 -*-
import json

sample_dict = {
  'comment_id' : 'hoge',
  'ng_channnel' : 'https://www.youtube.com/channel/UC7AagSmHm1myp6_TiGYiNuQ',
  'ng_comment_pattern' : {
    'ng_pattern' : '00001',
    'similarity' : 0.9
  }
}

sample_list = ['hoge', 'piyo']

if __name__ == '__main__':
  print(type(sample_dict)) # dict
  print(sample_dict)

  # json.dumps()
  sample_str = json.dumps(sample_dict)
  print(type(sample_str)) # str
  print(sample_str)
  
  print(sample_dict["comment_id"])
  # こちらはdictではないのでエラーになる。
  # print(sample_str["comment_id"])

  # 相手がlistでも使える。
  print(type(sample_list)) # list
  print(type(json.dumps(sample_list))) # str
  print(json.dumps(sample_list))
  
  # json.load()
  with open('../input/sample.json', mode='r') as f:
    load_json = json.load(f)

  print(type(load_json)) # dict
  print(load_json)
