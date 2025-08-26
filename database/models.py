from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, DateTime, Float, Integer

from database.db import Base


class Weather(Base):
    __tablename__ = "weather"

    # latitude: Mapped[float] = mapped_column(Float, primary_key=True)
    # longitude: Mapped[float] = mapped_column(Float, primary_key=True)
    temperature_2m_f: Mapped[float] = mapped_column(Float)
    apparent_temperature_f: Mapped[float] = mapped_column(Float)
    uv_index: Mapped[float] = mapped_column(Float)
    is_day: Mapped[bool] = mapped_column(Boolean)
    relative_humidity_2m_perc: Mapped[int] = mapped_column(Integer)
    utc_time: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
