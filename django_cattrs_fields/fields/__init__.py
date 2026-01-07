import datetime
from decimal import Decimal
import uuid

from attrs import frozen


@frozen
class Params:
    """param class for passing extra data to fields"""

    max_digits: int  # DecimalField
    decimal_places: int  # DecimalField


type BooleanField = bool

type CharField = str

type EmailField = str

type SlugField = str

type URLField = str

type UUIDField = uuid.UUID

type IntegerField = int

type DecimalField = Decimal

type FloatField = float

type DateField = datetime.date

type DateTimeField = datetime.datetime
