import json
import math

# Load data from `data.json` file
with open('data_1108_0014.json', 'r') as file:
    # Assuming `data.json` contains a JSON structure
    data = json.load(file)

# Initialize accumulators for votes and extrapolated totals
total_votes_trump = 0
total_votes_harris = 0
extrapolated_votes_trump = 0
extrapolated_votes_harris = 0

# Iterate over each state entry
for race in data:
    # Check if race has the expected structure and candidates
    if 'candidates' in race and 'pctIn' in race:
        pct_in = race['pctIn'] / 100  # Convert to a decimal

        state = race['stateCode'];

        trump_pickup = 0
        harris_pickup = 0
        # Iterate over candidates in each state
        if (state != 'US'):
            for candidate in race['candidates']:
                candidate_name = candidate['fullName']
                vote_count = candidate['vote']

                # Accumulate votes for Trump and Harris, and extrapolate based on `pctIn`
                if candidate_name == 'Donald Trump':
                    total_votes_trump += vote_count
                    trump_extrapolated = math.floor(vote_count / pct_in)
                    extrapolated_votes_trump += trump_extrapolated
                    trump_pickup = trump_extrapolated - vote_count

                elif candidate_name == 'Kamala Harris':
                    total_votes_harris += vote_count
                    harris_extrapolated = math.floor(vote_count / pct_in)
                    extrapolated_votes_harris += harris_extrapolated
                    harris_pickup = harris_extrapolated - vote_count
            # Display state results
            print(f"{state} Trump +{trump_pickup:,}, Harris +{harris_pickup:,}")

# Display final results
print("Total Votes (reported):")
print(f"Donald Trump: {total_votes_trump:,}")
print(f"Kamala Harris: {total_votes_harris:,}")
print("\nExtrapolated Final Vote Counts (based on percent in):")
print(f"Donald Trump: {int(extrapolated_votes_trump):,}")
print(f"Kamala Harris: {int(extrapolated_votes_harris):,}")
print("\nFinal Pickup")
print(f"Donald Trump: {int(extrapolated_votes_trump-total_votes_trump):,}")
print(f"Kamala Harris: {int(extrapolated_votes_harris-total_votes_harris):,}")

