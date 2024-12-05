from crewai import Crew
from agents.market_researcher import MarketResearcherAgent
from agents.data_analyst import DataAnalystAgent
from agents.report_writer import ReportWriterAgent
from tasks.market_research_tasks import MarketResearchTasks

def analyze_market_entry(company: str, target_market: str, entry_strategy: str):
    """Analyze market entry potential and strategy"""
    
    # Initialize agents
    researcher = MarketResearcherAgent().create()
    analyst = DataAnalystAgent().create()
    writer = ReportWriterAgent().create()
    
    # Create tasks
    tasks = MarketResearchTasks(researcher, analyst, writer)
    
    # Market analysis
    market_analysis = tasks.analyze_market_data(
        target_market,
        extra_context={
            'focus_areas': [
                'market_size',
                'entry_barriers',
                'regulatory_requirements',
                'competition'
            ]
        }
    )
    
    # Consumer analysis
    consumer_analysis = tasks.analyze_market_data(
        target_market,
        extra_context={
            'focus_areas': [
                'consumer_preferences',
                'buying_behavior',
                'price_sensitivity',
                'brand_perception'
            ]
        }
    )
    
    # Local competition
    local_competition = tasks.analyze_market_data(
        target_market,
        extra_context={
            'focus_areas': [
                'local_players',
                'market_share',
                'competitive_advantages',
                'pricing_strategies'
            ]
        }
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[market_analysis, consumer_analysis, local_competition],
        verbose=True
    )
    
    return crew.kickoff()

def main():
    # Example usage
    company = "GlobalCorp"
    target_market = "Southeast Asia E-commerce"
    entry_strategy = "Joint Venture"
    
    report = analyze_market_entry(company, target_market, entry_strategy)
    
    # Save the report
    with open(f"reports/{company.lower()}_market_entry_analysis.md", 'w') as f:
        f.write(report)

if __name__ == "__main__":
    main()