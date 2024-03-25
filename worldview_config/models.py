from datetime import datetime

from pydantic import BaseModel, Field, RootModel


class LayerConfig(BaseModel):
    id: str
    satellite: str
    instrument: str
    measurement: str
    discipline: str
    title: str
    format: str
    colormap_id: str
    matrix_set: str
    source_name: str
    description: str = Field(default="")
    tags: list[str] = Field(default=[])
    period: str | None
    start_date: datetime | None
    temporal_start: datetime | None
    temporal_end: datetime | None
    date_interval: str | None


class LayerConfigs(RootModel):
    root: list[LayerConfig]
