# Covid genome assembly QC scripts

- **PercentCoverage.py:** Create Assembly_QC w/ # of unambiguous bases, Reference Coverage %, & # of consecutive unambiguous bases
  - Samples that pass QC go to HighCoverage.csv
  - To pass QC must be >89% reference coverage or > 10k consecutive unambiguous bases
