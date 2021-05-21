# Json-dict inPython

## 概要

これはdict。(jsonに見えるが。)
``` python
sample_dict = {
  'comment_id' : 'hoge',
  'ng_channnel' : 'https://www.youtube.com/channel/UC7AagSmHm1myp6_TiGYiNuQ',
  'ng_comment_pattern' : {
    'ng_pattern' : '00001',
    'similarity' : 0.9
  }
}

print(type(sample_dict))
```

## jsonモジュール

### json.dumps(obj)

obj->str変換する。  
objはdictでもlistでもよい。

### json.loads(file)

json->dict変換する。  
jsonファイルを読み込んでdictに変換する。

``` python
with open('../input/sample.json', mode='r') as f:
  load_json = json.load(f)
```

### json.load()

## 参考

- [PythonでJSONファイル・文字列の読み込み・書き込み:note.nkmk.me](https://note.nkmk.me/python-json-load-dump/)
- [PythonでJSON 読み込み:Qiita](https://qiita.com/kikuchiTakuya/items/53990fca06fb9ba1d8a7)