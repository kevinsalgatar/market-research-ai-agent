from typing import Dict

class Prompts:
    MARKET_RESEARCH_PROMPTS = {
        'company_research': '''
            Conduct thorough research on {company_name}. Focus on:
            1. Company Overview
               - History and background
               - Mission and values
               - Key executives
            
            2. Products and Services
               - Main offerings
               - Unique selling propositions
               - Product development pipeline
            
            3. Market Position
               - Market share
               - Competitive advantages
               - Geographic presence
            
            4. Recent Developments
               - News and announcements
               - Strategic initiatives
               - Partnerships and acquisitions
            
            Provide specific citations for all information.
        ''',
        
        'market_analysis': '''
            Analyze the {industry} market with focus on:
            1. Market Size and Growth
               - Current market size
               - Historical growth rates
               - Future projections
            
            2. Competitive Landscape
               - Key players
               - Market shares
               - Competitive dynamics
            
            3. Market Drivers
               - Growth factors
               - Challenges
               - Opportunities
            
            4. Industry Economics
               - Revenue models
               - Cost structures
               - Profitability trends
            
            Use specific data points and metrics where available.
        ''',
        
        'trend_analysis': '''
            Identify and analyze key trends in the {timeframe} period:
            1. Technology Trends
               - Emerging technologies
               - Adoption rates
               - Impact assessment
            
            2. Consumer Behavior
               - Changing preferences
               - Buying patterns
               - Demographics
            
            3. Regulatory Environment
               - Current regulations
               - Pending legislation
               - Compliance requirements
            
            4. Future Outlook
               - Short-term predictions
               - Long-term forecasts
               - Risk factors
            
            Prioritize trends by impact and probability.
        ''',
        
        'report_generation': '''
            Create a comprehensive market research report using the provided data:
            
            Research Data:
            {research_data}
            
            Analysis Data:
            {analysis_data}
            
            Trends Data:
            {trends_data}
            
            Format the report with:
            1. Executive Summary
               - Key findings
               - Strategic implications
            
            2. Detailed Analysis
               - Company analysis
               - Market overview
               - Competitive landscape
            
            3. Trend Analysis
               - Current trends
               - Future outlook
            
            4. Recommendations
               - Strategic opportunities
               - Risk mitigation
               - Action items
            
            Use clear headers, bullet points, and data visualizations where appropriate.
        '''
    }
    
    @classmethod
    def get_prompt(cls, prompt_type: str, **kwargs) -> str:
        """Get formatted prompt by type"""
        prompt_template = cls.MARKET_RESEARCH_PROMPTS.get(prompt_type, "")
        return prompt_template.format(**kwargs) if prompt_template else ""