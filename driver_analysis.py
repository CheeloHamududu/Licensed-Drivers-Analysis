import pandas as pd
import folium
import numpy as np
from folium import plugins
import json

# Read the CSV data
df = pd.read_csv('Licensed_drivers_By_State.csv')

# Filter for 2017 data only (most recent year)
df_2017 = df[df['Year'] == 2017].copy()

# Group by state and gender to get total drivers per state by gender
state_gender_totals = df_2017.groupby(['State', 'Gender'])['Drivers'].sum().reset_index()

# Get total drivers per state
state_totals = df_2017.groupby('State')['Drivers'].sum().reset_index()
state_totals.columns = ['State', 'Total_Drivers']

# Pivot to get male and female columns
gender_pivot = state_gender_totals.pivot(index='State', columns='Gender', values='Drivers').reset_index()
gender_pivot = gender_pivot.fillna(0)

# Merge with totals
analysis_df = pd.merge(state_totals, gender_pivot, on='State')

# Calculate gender difference
analysis_df['Gender_Difference'] = analysis_df['Male'] - analysis_df['Female']
analysis_df['Male_Percentage'] = (analysis_df['Male'] / analysis_df['Total_Drivers']) * 100
analysis_df['Female_Percentage'] = (analysis_df['Female'] / analysis_df['Total_Drivers']) * 100

# Sort by total drivers to find states with most drivers
analysis_df = analysis_df.sort_values('Total_Drivers', ascending=False)

print("=== TOP 10 STATES WITH MOST DRIVERS (2017) ===")
print(analysis_df[['State', 'Total_Drivers', 'Male', 'Female', 'Gender_Difference']].head(10).to_string(index=False))

print("\n=== GENDER ANALYSIS SUMMARY ===")
print(f"Total Male Drivers: {analysis_df['Male'].sum():,}")
print(f"Total Female Drivers: {analysis_df['Female'].sum():,}")
print(f"Overall Gender Difference (Male - Female): {analysis_df['Gender_Difference'].sum():,}")

# State coordinates for mapping
state_coords = {
    'Alabama': [32.806671, -86.791130],
    'Alaska': [61.370716, -152.404419],
    'Arizona': [33.729759, -111.431221],
    'Arkansas': [34.969704, -92.373123],
    'California': [36.116203, -119.681564],
    'Colorado': [39.059811, -105.311104],
    'Connecticut': [41.767, -72.677],
    'Delaware': [39.161921, -75.526755],
    'District of Columbia': [38.9047, -77.0164],
    'Florida': [27.766279, -81.686783],
    'Georgia': [33.76, -84.39],
    'Hawaii': [21.30895, -157.826182],
    'Idaho': [44.240459, -114.478828],
    'Illinois': [40.349457, -88.986137],
    'Indiana': [39.790942, -86.147685],
    'Iowa': [42.011539, -93.210526],
    'Kansas': [38.526600, -96.726486],
    'Kentucky': [37.66814, -84.86311],
    'Louisiana': [31.169546, -91.867805],
    'Maine': [44.323535, -69.765261],
    'Maryland': [39.063946, -76.802101],
    'Massachusetts': [42.230171, -71.530106],
    'Michigan': [43.326618, -84.536095],
    'Minnesota': [45.7326, -93.9196],
    'Mississippi': [32.320, -90.207],
    'Missouri': [38.572954, -92.189283],
    'Montana': [47.052952, -110.454353],
    'Nebraska': [41.12537, -98.268082],
    'Nevada': [39.161921, -117.055374],
    'New Hampshire': [43.452492, -71.563896],
    'New Jersey': [40.221741, -74.756138],
    'New Mexico': [34.97273, -105.032363],
    'New York': [42.659829, -75.615],
    'North Carolina': [35.771, -78.638],
    'North Dakota': [47.555513, -101.002012],
    'Ohio': [40.367474, -82.996216],
    'Oklahoma': [35.482309, -97.534994],
    'Oregon': [44.931109, -123.029159],
    'Pennsylvania': [40.269789, -76.875613],
    'Rhode Island': [41.82355, -71.422132],
    'South Carolina': [33.836082, -81.163727],
    'South Dakota': [44.299782, -99.438828],
    'Tennessee': [35.771, -86.25],
    'Texas': [31.106, -97.6475],
    'Utah': [39.161921, -111.892622],
    'Vermont': [44.26639, -72.580536],
    'Virginia': [37.54, -78.46],
    'Washington': [47.042418, -122.893077],
    'West Virginia': [38.349497, -81.633294],
    'Wisconsin': [44.268543, -89.616508],
    'Wyoming': [42.7475, -107.2085]
}

# Create the map
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add markers for each state
for _, row in analysis_df.iterrows():
    state = row['State']
    if state in state_coords:
        lat, lon = state_coords[state]
        
        # Create popup text
        popup_text = f"""
        <b>{state}</b><br>
        Total Drivers: {row['Total_Drivers']:,}<br>
        Male: {row['Male']:,} ({row['Male_Percentage']:.1f}%)<br>
        Female: {row['Female']:,} ({row['Female_Percentage']:.1f}%)<br>
        Gender Difference: {row['Gender_Difference']:,}
        """
        
        # Color based on total drivers (top 10 states get different colors)
        if row['Total_Drivers'] > 10000000:  # Top tier
            color = 'red'
            radius = 15
        elif row['Total_Drivers'] > 5000000:  # Second tier
            color = 'orange'
            radius = 12
        elif row['Total_Drivers'] > 2000000:  # Third tier
            color = 'yellow'
            radius = 10
        else:
            color = 'blue'
            radius = 8
            
        folium.CircleMarker(
            location=[lat, lon],
            radius=radius,
            popup=folium.Popup(popup_text, max_width=300),
            color='black',
            weight=1,
            fillColor=color,
            fillOpacity=0.7
        ).add_to(m)

# Add a legend
legend_html = '''
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 200px; height: 120px; 
            background-color: white; border:2px solid grey; z-index:9999; 
            font-size:14px; padding: 10px">
<p><b>Driver Count Legend</b></p>
<p><i class="fa fa-circle" style="color:red"></i> > 10M drivers</p>
<p><i class="fa fa-circle" style="color:orange"></i> 5M - 10M drivers</p>
<p><i class="fa fa-circle" style="color:yellow"></i> 2M - 5M drivers</p>
<p><i class="fa fa-circle" style="color:blue"></i> < 2M drivers</p>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map
m.save('driver_analysis_map.html')

print(f"\n=== MAP SAVED ===")
print("Interactive map saved as 'driver_analysis_map.html'")

# Additional analysis
print("\n=== STATES WITH LARGEST GENDER DIFFERENCES ===")
print("States where males significantly outnumber females:")
male_dominant = analysis_df[analysis_df['Gender_Difference'] > 0].nlargest(5, 'Gender_Difference')
print(male_dominant[['State', 'Gender_Difference', 'Male_Percentage', 'Female_Percentage']].to_string(index=False))

print("\nStates where females significantly outnumber males:")
female_dominant = analysis_df[analysis_df['Gender_Difference'] < 0].nsmallest(5, 'Gender_Difference')
print(female_dominant[['State', 'Gender_Difference', 'Male_Percentage', 'Female_Percentage']].to_string(index=False))

print("\n=== GENDER DISTRIBUTION INSIGHTS ===")
avg_male_pct = analysis_df['Male_Percentage'].mean()
avg_female_pct = analysis_df['Female_Percentage'].mean()
print(f"Average Male Percentage across all states: {avg_male_pct:.2f}%")
print(f"Average Female Percentage across all states: {avg_female_pct:.2f}%")

# States with most balanced gender distribution
analysis_df['Gender_Balance'] = abs(analysis_df['Male_Percentage'] - 50)
most_balanced = analysis_df.nsmallest(5, 'Gender_Balance')
print(f"\nMost gender-balanced states:")
print(most_balanced[['State', 'Male_Percentage', 'Female_Percentage']].to_string(index=False))