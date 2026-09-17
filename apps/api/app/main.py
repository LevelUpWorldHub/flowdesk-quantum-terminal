from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")


class RegimeResponse(BaseModel):
    symbol: str
    regime: Literal["low", "normal", "elevated", "crisis"]
    as_of: datetime
    note: str


class IVPoint(BaseModel):
    expiry: str
    strike: float
    iv: float


class IVSurfaceResponse(BaseModel):
    symbol: str
    points: list[IVPoint]
    source: str


class PaperOrderRequest(BaseModel):
    symbol: str = Field(min_length=1, max_length=12)
    side: Literal["buy", "sell"]
    qty: float = Field(gt=0)
    type: Literal["market", "limit"] = "market"
    limit_price: float | None = None


class PaperOrderResponse(BaseModel):
    id: str
    status: str
    paper: bool
    accepted: bool


@app.get("/health")
def health() -> dict[str, str | bool]:
    return {"status": "ok", "service": settings.app_name, "paper_only": settings.paper_only}


@app.get("/v1/regime/{symbol}", response_model=RegimeResponse)
def regime(symbol: str) -> RegimeResponse:
    # Deterministic mock for foundation demos
    bucket = ["low", "normal", "elevated", "crisis"][sum(ord(c) for c in symbol.upper()) % 4]
    return RegimeResponse(
        symbol=symbol.upper(),
        regime=bucket,  # type: ignore[arg-type]
        as_of=datetime.now(timezone.utc),
        note="mock_regime_not_live_market_data",
    )


@app.get("/v1/iv-surface/{symbol}", response_model=IVSurfaceResponse)
def iv_surface(symbol: str) -> IVSurfaceResponse:
    base = 0.18 + (sum(ord(c) for c in symbol.upper()) % 10) / 100
    points = [
        IVPoint(expiry="2026-10-17", strike=100 + i * 5, iv=round(base + i * 0.01, 4))
        for i in range(5)
    ]
    return IVSurfaceResponse(symbol=symbol.upper(), points=points, source="mock")


@app.post("/v1/paper/orders", response_model=PaperOrderResponse)
def paper_order(body: PaperOrderRequest) -> PaperOrderResponse:
    if not settings.paper_only:
        raise HTTPException(status_code=403, detail="live_trading_disabled")
    oid = f"paper_{body.symbol.upper()}_{body.side}_{int(body.qty)}"
    return PaperOrderResponse(id=oid, status="accepted", paper=True, accepted=True)
