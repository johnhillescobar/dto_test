from datetime import datetime
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

try:
    from langchain_core.tools import ArgsSchema
except Exception:
    ArgsSchema = type[BaseModel]
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CelsiusToFahrenheit(BaseModel):
    celsius: float | None = Field(description="The temperature in Celsius")


class CelsiusToFahrenheitResponse(BaseModel):
    input_value: float | None = Field(description="The input value")
    input_unit: str | None = Field(description="The input unit")
    output_value: float | None = Field(description="The output value")
    output_unit: str | None = Field(description="The output unit")
    timestamp: datetime | None = Field(description="The timestamp of the conversion")


class CelsiusToFahrenheitTool(BaseTool):
    """Convert Celsius to fahrenheit"""

    name: str = "celsius_to_fahrenheit"
    description: str = "Convert Celsius to fahrenheit"
    args_schema: ArgsSchema = CelsiusToFahrenheit

    def _run(self, **kwargs: dict) -> CelsiusToFahrenheitResponse:
        validated_input = CelsiusToFahrenheit(**kwargs)
        celsius = validated_input.celsius

        logger.info(f"Converting Celsius to fahrenheit: {celsius}")
        if celsius is None:
            raise ValueError("Celsius is required")

        fahrenheit = (celsius * 9 / 5) + 32

        logger.info(f"fahrenheit: {fahrenheit}")
        return CelsiusToFahrenheitResponse(
            input_value=celsius,
            input_unit="celsius",
            output_value=fahrenheit,
            output_unit="fahrenheit",
            timestamp=datetime.now(),
        )

    async def _arun(self, **kwargs: dict) -> CelsiusToFahrenheitResponse:
        validated_input = CelsiusToFahrenheit(**kwargs)
        celsius = validated_input.celsius

        logger.info(f"Converting Celsius to fahrenheit: {celsius}")
        if celsius is None:
            raise ValueError("Celsius is required")

        fahrenheit = (celsius * 9 / 5) + 32

        logger.info(f"fahrenheit: {fahrenheit}")
        return CelsiusToFahrenheitResponse(
            input_value=celsius,
            input_unit="celsius",
            output_value=fahrenheit,
            output_unit="fahrenheit",
            timestamp=datetime.now(),
        )
