from report_generator import (
    generate_business_report,
    generate_executive_summary
)

def main():
    print("=== Business Report Automation System ===")

    company = input("Enter company name: ")
    period = input("Enter reporting period: ")
    achievements = input("Enter key achievements: ")
    challenges = input("Enter challenges faced: ")
    plans = input("Enter future plans: ")

    report = generate_business_report(
        company, period, achievements, challenges, plans
    )

    summary = generate_executive_summary(
        company, achievements, plans
    )

    print("\n--- Business Report ---\n")
    print(report)

    print("\n--- Executive Summary ---\n")
    print(summary)

if __name__ == "__main__":
    main()