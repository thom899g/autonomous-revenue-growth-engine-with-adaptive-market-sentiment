import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass

class PricingStrategist:
    """
    Determines optimal pricing based on market analysis and constraints.
    
    Attributes:
        logger (logging.Logger): Logging instance for tracking operations.
        min_price (float): Minimum acceptable price.
        max_price (float): Maximum acceptable price.
    """
    
    def __init__(self, min_price: float = 0.9, max_price: float = 1.1) -> None:
        """Initializes the PricingStrategist with price constraints."""
        self.logger = logging.getLogger(__name__)
        self.min_price = min_price
        self.max_price = max_price
        
    def calculate_optimal_price(self, market_data: Dict[str, Any]) -> float:
        """
        Calculates optimal price based on market conditions.
        
        Args:
            market_data (Dict[str, Any]): Market data including sentiment and trends.
            
        Returns:
            float: The calculated optimal price.
        """
        try:
            # Simple pricing model for demonstration
            base_price = 1.0
            sentiment_impact = market_data.get('sentiment_score', 0) * 0.1
            trend_impact = (market_data.get('forecast', 0) > 0) * 0.05
            
            optimal_price = base_price + sentiment_impact + trend_impact
            
            # Apply constraints
            optimal_price = max(self.min_price, min(optimal_price, self.max_price))
            
            return optimal_price
        except Exception as e:
            self.logger.error(f"Price calculation failed: {e}")
            raise
        
    def update_constraints(self, new_min: Optional[float] = None, 
                          new_max: Optional[float] = None) -> None:
        """
        Updates the pricing constraints.
        
        Args:
            new_min (Optional[float]): New minimum price constraint.
            new_max (Optional[float]): New maximum price constraint.
        """
        if new_min is not None:
            self.min_price = max(new_min, 0.0)
        if new_max is not None:
            self.max_price = min(new_max, float('inf'))