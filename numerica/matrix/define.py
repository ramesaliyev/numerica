def m(matrix):
  if (type(matrix) == list):
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