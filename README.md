# Licensed Drivers Analysis by State and Gender

A comprehensive analysis of licensed drivers data across US states, focusing on driver distribution by state and gender differences using Python data analysis and interactive mapping.

## 📊 Dataset

- **Source**: Licensed drivers by state dataset
- **Time Period**: 1994-2018 (analysis focuses on 2017 data)
- **Coverage**: All 50 US states + DC
- **Variables**: Year, Gender, Age Cohort, State, Driver Count

## 🎯 Analysis Objectives

- Identify states with the highest number of licensed drivers
- Analyze gender distribution patterns across states
- Visualize geographic distribution of drivers using interactive maps
- Calculate gender differences and identify most balanced states

## 📁 Files

- `Licensed_drivers_By_State.csv` - Raw dataset
- `driver_analysis.py` - Python script for complete analysis
- `driver_analysis.ipynb` - Jupyter notebook with interactive analysis
- `driver_analysis_map.html` - Interactive Folium map output

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas folium numpy
```

### Run Analysis
```bash
# Python script
python3 driver_analysis.py

# Or use Jupyter notebook
jupyter notebook driver_analysis.ipynb
```

## 📈 Key Findings

### Top 5 States by Total Drivers (2017)
1. **California** - 26.8M drivers
2. **Texas** - 17.1M drivers  
3. **Florida** - 15.1M drivers
4. **New York** - 12.2M drivers
5. **Pennsylvania** - 9.0M drivers

### Gender Analysis
- **Total Male Drivers**: ~115M
- **Total Female Drivers**: ~118M
- **Overall**: Females slightly outnumber males nationally
- **Average Gender Split**: 49.4% Male, 50.6% Female

## 🗺️ Interactive Map Features

- **Color-coded markers** by driver count:
  - 🔴 Red: >10M drivers
  - 🟠 Orange: 5M-10M drivers  
  - 🟡 Yellow: 2M-5M drivers
  - 🔵 Blue: <2M drivers

- **Popup information** includes:
  - Total drivers per state
  - Male/Female breakdown with percentages
  - Gender difference calculations

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Folium** - Interactive mapping
- **NumPy** - Numerical computations
- **Jupyter** - Interactive development

## 📊 Analysis Highlights

- **Most Male-Dominant States**: Alaska, Wyoming, North Dakota
- **Most Female-Dominant States**: Rhode Island, Massachusetts, New York
- **Most Gender-Balanced**: Delaware, Nevada, New Hampshire
- **Geographic Patterns**: Coastal states tend to have more female drivers

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/analysis-improvement`)
3. Commit changes (`git commit -am 'Add new analysis'`)
4. Push to branch (`git push origin feature/analysis-improvement`)
5. Create Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

For questions or suggestions, please open an issue.