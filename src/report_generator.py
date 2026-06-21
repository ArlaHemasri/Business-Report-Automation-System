def generate_business_report(company, period, achievements, challenges, plans):
    return (
        f"Business Report for {company}\n"
        f"Reporting Period: {period}\n\n"
        f"Key Achievements:\n{achievements}\n\n"
        f"Challenges Faced:\n{challenges}\n\n"
        f"Future Plans:\n{plans}\n"
    )


def generate_executive_summary(company, achievements, plans):
    return (
        f"Executive Summary:\n"
        f"{company} has demonstrated strong performance with notable achievements such as "
        f"{achievements}. Moving forward, the organization plans to focus on {plans} "
        f"to sustain growth and competitiveness."
    )