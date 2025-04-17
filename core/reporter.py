import os
import json
import jinja2

def generate_report(static_results, dynamic_results, report_type="md", output_dir="./reports"):
    os.makedirs(output_dir, exist_ok=True)
    
    if report_type == "md":
        report_content = f"## Static Analysis Results\n{static_results}\n\n## Dynamic Testing Results\n{dynamic_results}"
        report_file = os.path.join(output_dir, "report.md")
        with open(report_file, "w") as f:
            f.write(report_content)
    elif report_type == "json":
        report_data = {"static_results": static_results, "dynamic_results": dynamic_results}
        report_file = os.path.join(output_dir, "report.json")
        with open(report_file, "w") as f:
            json.dump(report_data, f, indent=4)
    else:
        raise ValueError("Invalid report type. Use 'md' or 'json'.")
    print(f"Report saved to {report_file}")
