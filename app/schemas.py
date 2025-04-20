from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class CalculatorSubmission(BaseModel):
    id: Optional[UUID] = None
    timestamp: datetime
    ip_address: str
    num_properties: int
    average_rent: float
    occupancy_rate: float
    default_rate: float
    average_commission: float
    average_contract_duration: int
    terminated_contracts_per_month: int
    new_contracts_per_month: int
    contracts_expiring_12_months: int
    contracts_expiring_12_to_24_months: int
    contracts_expiring_24_to_36_months: int
    contracts_expiring_over_36_months: int
    expired_indefinite_contracts: int
    predominant_guarantee_type: str
    residential_percentage: float
    commercial_percentage: float
    city: str
    state: str
    valor_criterio: float
    estoque_atual: float
    portfolio_value: float
    monthly_revenue: float
    annual_revenue: float
    potential_growth: float
    stability_score: float
    growth_rate: float
    is_submitted: bool

    class Config:
        orm_mode = True