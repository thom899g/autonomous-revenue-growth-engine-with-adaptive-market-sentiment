import logging
from typing import Dict, Any
from .market_analyzer import MarketAnalyzer
from .pricing_strategist import PricingStrategist

class RevenueEngine:
    """
    Orchestrates the autonomous revenue growth process.
    
    Attributes:
        market_analyzer (MarketAnalyzer): Analyzes market conditions.
        pricing_strategist (PricingStrategist): Determines optimal pricing.
        logger (logging.Logger): Logging instance for tracking operations.
    """
    
    def __init__(self, api_key: str) -> None:
        """Initializes the RevenueEngine with necessary components."""
        self.market_analyzer = MarketAnalyzer(api_key)
        self.pricing_strategist = PricingStrategist()
        self.logger = logging.getLogger(__name__)
        
    def run_revenue_cycle(self, market: str, timeframe: str) -> Dict[str, Any]:
        """
        Executes the revenue growth cycle.
        
        Args:
            market (str): Market identifier (e.g., 'BTC/USDT').
            timeframe (str): Timeframe string (e.g., '1D', '1H').
            
        Returns:
            Dict[str, Any]: Results including price and forecast data.
        """
        try:
            # Step 1: Fetch market data
            self.logger.info("Fetching market data...")
            data = self.market_analyzer.fetch_market_data(market, timeframe)
            
            # Step 2: Analyze sentiment
            self.logger.info("Analyzing sentiment...")
            sentiment_score = self.market_analyzer.analyze_sentiment(data['news'])
            
            # Step 3: Predict market trend
            self.logger.info("Predicting market trend...")
            forecast = self.market_analyzer.predict_market_trend(data)
            
            # Step 4: Calculate optimal price
            self.logger.info("Calculating optimal price...")
            optimal_price = self.pricing_strategist.calculate_optimal_price({
                'sentiment_score': sentiment_score,
                'forecast': forecast['forecast']
            })
            
            return {
                'optimal_price': optimal_price,
                'market_forecast': forecast['forecast'],
                'timestamp': datetime