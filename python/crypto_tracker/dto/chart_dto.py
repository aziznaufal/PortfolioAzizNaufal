from datetime import datetime

class ChartDTO:
    @staticmethod
    def format(raw_data, chart_type="line"):
        if chart_type == "candlestick":
            return [{
                "x": datetime.fromtimestamp(int(c[0]) / 1000).isoformat(),
                "o": float(c[1]),
                "h": float(c[2]),
                "l": float(c[3]),
                "c": float(c[4])
            } for c in raw_data]
        else:
            return [{
                "x": datetime.fromtimestamp(int(c[0]) / 1000).isoformat(),
                "y": float(c[4])
            } for c in raw_data]
