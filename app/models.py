from sqlalchemy import Column, Integer, Numeric, String, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class CalculatorSubmissionTable(Base):
    __tablename__ = "calculator_submissions"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    timestamp = Column(TIMESTAMP, nullable=False)
    ip_address = Column(String(45), nullable=False)
    num_properties = Column(Integer, nullable=False)
    average_rent = Column(Numeric, nullable=False)
    occupancy_rate = Column(Numeric, nullable=False)
    default_rate = Column(Numeric, nullable=False)
    average_commission = Column(Numeric, nullable=False)
    average_contract_duration = Column(Integer, nullable=False)
    terminated_contracts_per_month = Column(Integer, nullable=False)
    new_contracts_per_month = Column(Integer, nullable=False)
    contracts_expiring_12_months = Column(Integer, nullable=False)
    contracts_expiring_12_to_24_months = Column(Integer, nullable=False)
    contracts_expiring_24_to_36_months = Column(Integer, nullable=False)
    contracts_expiring_over_36_months = Column(Integer, nullable=False)
    expired_indefinite_contracts = Column(Integer, nullable=False)
    predominant_guarantee_type = Column(String(100), nullable=False)
    residential_percentage = Column(Numeric, nullable=False)
    commercial_percentage = Column(Numeric, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(10), nullable=False)
    valor_criterio = Column(Numeric, nullable=False)
    estoque_atual = Column(Numeric, nullable=False)
    portfolio_value = Column(Numeric, nullable=False)
    monthly_revenue = Column(Numeric, nullable=False)
    annual_revenue = Column(Numeric, nullable=False)
    potential_growth = Column(Numeric, nullable=False)
    stability_score = Column(Numeric, nullable=False)
    growth_rate = Column(Numeric, nullable=False)
    is_submitted = Column(Boolean, nullable=False)