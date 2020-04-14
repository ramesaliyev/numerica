def is_matrix(A):
  return type(A) == list and all(type(row) == list for row in A)

def m(matrix):
  if (is_matrix(matrix)):
    return matrix

  return (
    list(map(
      lambda row: list(map(
        lambda cell: float(cell),
        row.split(',')
      )),
      matrix.split(';')
    ))
  )

def parse_matrix(count = 1):
  def wrapper(fn):
    def function(*args, **kwargs):
      argz = [m(v) if i < count else v for (i,v) in enumerate(list(args))]
      return fn(*argz, **kwargs)
    return function
  return wrapper