def transform_kline_data(data):
    candles = []
    for d in data:
        candles.append({
            'x': d[0],  # timestamp
            'o': float(d[1]),
            'h': float(d[2]),
            'l': float(d[3]),
            'c': float(d[4])
        })
    return candles
