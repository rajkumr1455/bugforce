import sys
from core.fetcher import fetch_contract, fetch_source_code
from core.static_analyzer import run_static_analysis
from core.dynamic_tester import run_foundry
from core.report import generate_report

def main():
    # Parsing the arguments
    parser = argparse.ArgumentParser(description="BugForce Smart Contract Analyzer")
    parser.add_argument('--smartcontract', type=str, required=True, help="Contract address to analyze")
    parser.add_argument('--network', type=str, default="bsc", help="Blockchain network (bsc, ethereum, etc.)")
    parser.add_argument('--poc', action='store_true', help="Run dynamic PoC testing with Foundry")
    parser.add_argument('--report', type=str, default="bugforce_report.md", help="Path to output report")
    parser.add_argument('--output', type=str, default="./", help="Directory to save results")
    
    args = parser.parse_args()

    print("🔍 Checking environment requirements...")
    # Make sure environment is ready (code omitted for brevity)

    # Fetch the contract data (either ABI or source code)
    try:
        if args.network == "bsc":
            contract_data = fetch_contract(args.smartcontract, args.network)  # ABI only
            source_code = fetch_source_code(args.smartcontract, args.network)  # Full source code
        else:
            print(f"⚠️ Network '{args.network}' is not supported yet. Only BSC is currently available.")
            sys.exit(1)
        
        if not contract_data:
            print("⚠️ Failed to fetch contract data.")
            sys.exit(1)

    except Exception as e:
        print(f"⚠️ Error: {str(e)}")
        sys.exit(1)

    # Static Analysis (Slither)
    print("🔍 Running static analysis...")
    static_results = run_static_analysis(source_code)  # Run Slither on full source code

    # Dynamic Analysis (Foundry)
    dynamic_results = None
    if args.poc:
        print("🧪 Running dynamic PoC analysis with Foundry...")
        dynamic_results = run_foundry(source_code)

    # Generate and write the report
    print("📑 Generating the report...")
    generate_report(static_results, dynamic_results, args.report, args.output)

if __name__ == "__main__":
    main()
