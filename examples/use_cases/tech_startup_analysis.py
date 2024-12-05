from crewai import Crew
from agents.market_researcher import MarketResearcherAgent
from agents.data_analyst import DataAnalystAgent
from agents.report_writer import ReportWriterAgent
from tasks.market_research_tasks import MarketResearchTasks

def analyze_tech_startup(startup_name: str, target_market: str):
    """Analyze a technology startup and its market potential"""
    
    # Initialize agents
    researcher = MarketResearcherAgent().create()
    analyst = DataAnalystAgent().create()
    writer = ReportWriterAgent().create()
    
    # Create tasks
    tasks = MarketResearchTasks(researcher, analyst, writer)
    
    # Define specific research tasks
    company_research = tasks.research_company(
        startup_name,
        extra_context={
            'focus_areas': [
                'funding history',
                'technology stack',
                'team background',
                'product roadmap'
            ]
        }
    )
    
    market_analysis = tasks.analyze_market_data(
        target_market,
        extra_context={
            'focus_areas': [
                'market size',
                'growth potential',
                'entry barriers',
                'competition'
            ]
        }
    )
    
    trend_analysis = tasks.identify_trends(
        '12months',
        extra_context={
            'focus_areas': [
                'technology trends',
                'investment patterns',
                'customer preferences'
            ]
        }
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[company_research, market_analysis, trend_analysis],
        verbose=True
    )
    
    return crew.kickoff()

def main():
    # Example usage
    startup_name = "TechStartup Inc"
    target_market = "AI Software"
    
    report = analyze_tech_startup(startup_name, target_market)
    
    # Save the report
    with open(f"reports/{startup_name.lower().replace(' ', '_')}_analysis.md", 'w') as f:
        f.write(report)

if __name__ == "__main__":
    main()