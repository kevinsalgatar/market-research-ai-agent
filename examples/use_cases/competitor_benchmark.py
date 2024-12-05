from crewai import Crew
from agents.market_researcher import MarketResearcherAgent
from agents.data_analyst import DataAnalystAgent
from agents.report_writer import ReportWriterAgent
from tasks.market_research_tasks import MarketResearchTasks
from typing import List

def benchmark_competitors(main_company: str, competitors: List[str], industry: str):
    """Perform competitive benchmarking analysis"""
    
    # Initialize agents
    researcher = MarketResearcherAgent().create()
    analyst = DataAnalystAgent().create()
    writer = ReportWriterAgent().create()
    
    # Create tasks
    tasks = MarketResearchTasks(researcher, analyst, writer)
    
    # Research main company
    main_company_research = tasks.research_company(
        main_company,
        extra_context={'competitor_comparison': True}
    )
    
    # Research competitors
    competitor_tasks = [
        tasks.research_company(
            competitor,
            extra_context={'competitor_comparison': True}
        )
        for competitor in competitors
    ]
    
    # Market analysis
    market_analysis = tasks.analyze_market_data(
        industry,
        extra_context={
            'focus_areas': [
                'market_share',
                'pricing_strategies',
                'product_features',
                'customer_satisfaction'
            ]
        }
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[main_company_research] + competitor_tasks + [market_analysis],
        verbose=True
    )
    
    return crew.kickoff()

def main():
    # Example usage
    main_company = "MainCorp"
    competitors = ["Competitor1", "Competitor2", "Competitor3"]
    industry = "Software Development"
    
    report = benchmark_competitors(main_company, competitors, industry)
    
    # Save the report
    with open(f"reports/{main_company.lower()}_competitive_analysis.md", 'w') as f:
        f.write(report)

if __name__ == "__main__":
    main()