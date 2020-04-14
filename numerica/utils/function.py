from re import sub

def f(txt):
  if type(txt) != str:
    return txt

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

def parse_f(count = 1):
  def wrapper(fn):
    def function(*args, **kwargs):
      argz = [f(v) if i < count else v for (i,v) in enumerate(list(args))]
      return fn(*argz, **kwargs)
    return function
  return wrapper