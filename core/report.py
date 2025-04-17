import os

def generate_report(static_results, dynamic_results, filename, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, filename)

    with open(report_path, "w") as report:
        report.write("# 🐞 BugForce Smart Contract Report\n\n")

        report.write("## 🔍 Static Analysis\n")
        report.write("```\n")
        report.write(static_results or "No static results.")
        report.write("\n```\n")

        report.write("## 🧪 Dynamic Analysis\n")
        report.write("```\n")
        report.write(dynamic_results or "No dynamic analysis run.")
        report.write("\n```\n")

    print(f"✅ Report saved to {report_path}")
