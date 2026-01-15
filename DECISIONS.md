\# Design Decisions



\## Data format choice



I chose a CSV file because the dataset is small, personal, and manually collected.

A relational database would introduce unnecessary operational complexity without clear benefits at this scale.



The CSV format keeps the data transparent, portable, and easy to version-control.



\## Tooling choices



pandas was selected for its expressive and readable support for tabular data manipulation.

matplotlib was used because it provides sufficient control for simple, interpretable visualizations without additional dependencies.



The focus of this project is analytical clarity rather than visualization aesthetics.



\## Scope limitations



\- Machine learning models were intentionally excluded due to the small dataset size and lack of predictive validity.

\- Performance optimization was not considered a priority, as the data volume is minimal.

\- No external data sources were used to preserve the authenticity of the self-recorded logs.



\## Possible extensions



\- Automate data logging

\- Add weekly or monthly aggregated summaries

\- Extend the analysis into a lightweight web application

