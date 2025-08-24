from recommenders import get_recommendations

print("\n--- Property Recommender (CLI) ---")
print("Enter your property search query (searching............).")
print("Type 'exit' to quit.\n")

while True:
    query = input("Enter your query (or type 'exit'): ").strip()
    if query.lower() == "exit":
        break

    results = get_recommendations(query)

    if results.empty:
        print("❌ No properties found for your query!\n")
    else:
        print(f"\n✅ Found {len(results)} matching properties:\n")
        for _, row in results.iterrows():
            print(
                f"🏠 {row['bedrooms']} BHK | {row['location']} | "
                f"{row['total_sqft']} sqft | ₹{row['price']:,}"
            )
        print()
