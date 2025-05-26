from dataclasses import dataclass

@dataclass
class CoinDTO:
    symbol: str
    baseAsset: str
    quoteAsset: str

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "baseAsset": self.baseAsset,
            "quoteAsset": self.quoteAsset
        }
