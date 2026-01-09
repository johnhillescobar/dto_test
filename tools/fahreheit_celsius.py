from langchain.tools import BaseTool
from pydantic import BaseModel, Field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FahrenheitToCelsius(BaseModel):
    fahrenheit: float | None = Field(description="The temperature in Fahrenheit")


class FahrenheitToCelsiusTool(BaseTool):
    """Convert Fahrenheit to Celsius"""

    name: str = "fahrenheit_to_celsius"
    description: str = "Convert Fahrenheit to Celsius"

    def _run(self, fahrenheit: float) -> float:
        logger.info(f"Converting Fahrenheit to Celsius: {fahrenheit}")

        if fahrenheit is None:
            raise ValueError("Fahrenheit is required")

        celsius = (fahrenheit - 32) * 5 / 9

        logger.info(f"Celsius: {celsius}")
        return celsius

    async def _arun(self, fahrenheit: float) -> float:
        logger.info(f"Converting Fahrenheit to Celsius: {fahrenheit}")

        if fahrenheit is None:
            raise ValueError("Fahrenheit is required")

        celsius = (fahrenheit - 32) * 5 / 9

        logger.info(f"Celsius: {celsius}")
        return celsius
