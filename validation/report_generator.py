#generates pass/fail report

from datetime import datetime

class ReportGenerator:
    def __init__(self, logger):
        self.logger = logger

    def generate(self, output_file="report.txt"):
        summary = self.logger.get_summary()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        lines = [
            "=" * 50,
            "       ESP32 SENSOR VALIDATION REPORT",
            "=" * 50,
            f"Date:        {timestamp}",
            f"Total Tests: {summary['total']}",
            f"Passed:      {summary['passed']}",
            f"Failed:      {summary['failed']}",
            f"Pass Rate:   {summary['pass_rate']}",
            "=" * 50,
            "",
            "DETAILED RESULTS:",
            "-" * 50,
        ]

        for entry in self.logger.entries:
            status_symbol = "✓" if entry["status"] == "PASS" else "✗"
            lines.append(
                f"[{status_symbol}] {entry['timestamp']} | "
                f"Temp: {entry['temperature']}°C | "
                f"Humidity: {entry['humidity']}% | "
                f"Light: {entry['light']} | "
                f"Status: {entry['status']}"
                + (f" | Error: {entry['error']}" if entry['error'] else "")
            )

        lines += ["=" * 50]

        report = "\n".join(lines)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(report)
        return report