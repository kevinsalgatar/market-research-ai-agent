import os
from datetime import datetime
from typing import Dict, Any
import json
import markdown2
import jinja2

class ReportGenerator:
    def __init__(self, template_dir: str = 'examples/templates'):
        self.template_dir = template_dir
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=jinja2.select_autoescape(['html', 'xml'])
        )
    
    def generate_report(self, template_name: str, data: Dict[str, Any], output_format: str = 'md') -> str:
        """Generate a report using a template and data"""
        try:
            template = self.env.get_template(f"{template_name}.{output_format}")
            report = template.render(**data)
            
            # Add metadata
            metadata = {
                'generated_at': datetime.now().isoformat(),
                'template_used': template_name,
                'data_sources': data.get('data_sources', [])
            }
            
            report = f"""---\nmetadata: {json.dumps(metadata, indent=2)}\n---\n\n{report}"""
            
            return report
        
        except Exception as e:
            return f"Error generating report: {str(e)}"
    
    def save_report(self, content: str, filename: str, output_dir: str = 'reports') -> str:
        """Save the generated report to a file"""
        try:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return filepath
        
        except Exception as e:
            return f"Error saving report: {str(e)}"
    
    def convert_to_html(self, markdown_content: str) -> str:
        """Convert markdown report to HTML"""
        try:
            html = markdown2.markdown(
                markdown_content,
                extras=['metadata', 'tables', 'fenced-code-blocks']
            )
            
            # Add basic styling
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Market Research Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                    h1, h2, h3 {{ color: #333; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f5f5f5; }}
                    code {{ background-color: #f5f5f5; padding: 2px 5px; border-radius: 3px; }}
                </style>
            </head>
            <body>
                {html}
            </body>
            </html>
            """
            
            return html
        
        except Exception as e:
            return f"Error converting to HTML: {str(e)}"