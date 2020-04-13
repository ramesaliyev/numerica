from re import sub

def fn(txt):
  def call(x=0, **keywords):
    fn = txt
    fn = fn.replace('^', '**')

    keywords['x'] = x

    for k in keywords:
      k = str(k)
      v = str(keywords[k])
      fn = sub(r'(\d+?)' + k, r'\g<1>*(' + v + ')', fn)
      fn = fn.replace(k, v)

    return float(eval(fn))
  return call