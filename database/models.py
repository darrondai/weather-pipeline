from decimal import Decimal
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, DateTime, Numeric

from database.db import Base


class Weather(Base):
    __tablename__ = "weather"

    latitude: Mapped[Decimal] = mapped_column(Numeric, primary_key=True)
    longitude: Mapped[Decimal] = mapped_column(Numeric, primary_key=True)
    apparent_temperature: Mapped[Decimal] = mapped_column(Numeric)
    uv_index: Mapped[Decimal] = mapped_column(Numeric)
    is_day: Mapped[bool] = mapped_column(Boolean)
    relative_humidity_2m_perc: Mapped[Decimal] = mapped_column(Numeric)
    utc_time: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
