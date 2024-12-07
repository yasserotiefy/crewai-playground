#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from crews.stock_analysis_crew.stock_analysis_crew import StockAnalysisCrew

import openlit

openlit.init(
    otlp_endpoint="http://127.0.0.1:4318", 
)

from dotenv import load_dotenv

load_dotenv()


class StockAnalysisState(BaseModel):
    company_name: str = ""
    report: str = ""


class StockAnalysisFlow(Flow[StockAnalysisState]):

    @start()
    def generate_company_name(self):
        print("Generating company name")
        self.state.company_name = "Google"

    @listen(generate_company_name)    
    def generate_report(self):
        print("Generating report")
        result = (
            StockAnalysisCrew()
            .crew()
            .kickoff(inputs={"company_name": self.state.company_name})
        )

        print("Report generated", result.raw)
        self.state.report = result.raw

    @listen(generate_report)
    def save_report(self):
        print("Saving report")
        with open("report.md", "w") as f:
            f.write(self.state.report)


def kickoff():
    stock_analysis_flow = StockAnalysisFlow()
    stock_analysis_flow.kickoff()


def plot():
    stock_analysis_flow = StockAnalysisFlow()
    stock_analysis_flow.plot()


if __name__ == "__main__":
    kickoff()
    plot()
