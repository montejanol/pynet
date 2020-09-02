Value PORT (\S+)

Start
  ^Port.*Type\s*$$ -> SHOW_PORT

SHOW_PORT
  ^${PORT} -> Record

