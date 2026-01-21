## Methodology, Result Table, and Result Graph

### Methodology

The TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method is a multi-criteria decision-making approach used to rank alternatives based on their relative closeness to an ideal solution.

The methodology followed in this project is explained step-by-step below:

1. **Input Data Construction**  
   The input CSV file consists of multiple alternatives (e.g., mutual funds or students) and multiple criteria.  
   - The **first column** is treated as an identifier.
   - All remaining columns are treated as **numeric criteria**.

2. **Normalization of Decision Matrix**  
   Each criterion is normalized using vector normalization to remove scale differences between criteria.

3. **Weighted Normalized Matrix**  
   The normalized values are multiplied by user-defined weights to reflect the importance of each criterion.

4. **Identification of Ideal Best and Ideal Worst**  
   - For **benefit criteria (+)**, the maximum value is ideal best and minimum is ideal worst.
   - For **cost criteria (-)**, the minimum value is ideal best and maximum is ideal worst.

5. **Distance Calculation**  
   Euclidean distance of each alternative is calculated from:
   - Ideal Best Solution
   - Ideal Worst Solution

6. **TOPSIS Score Calculation**  
   The TOPSIS score (closeness coefficient) is calculated using:

## Result Table and Analysis

The table below shows the final results obtained after applying the **TOPSIS methodology** on the given dataset of mutual funds.

### Result Table

```csv
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.84,0.71,6.7,42.1,12.59,0.376947,6
M2,0.91,0.83,7.0,31.7,10.11,0.306839,8
M3,0.79,0.62,4.8,46.7,13.23,0.484067,3
M4,0.78,0.61,6.4,42.4,12.55,0.336020,7
M5,0.94,0.88,3.6,62.2,16.91,0.977223,1
M6,0.88,0.77,6.5,51.5,14.91,0.590263,2
M7,0.66,0.44,5.3,48.9,13.83,0.439521,5
M8,0.93,0.86,3.4,37.0,10.55,0.456554,4
```

### Result Interpretation

Each alternative (M1–M8) represents a mutual fund.

The TOPSIS Score indicates how close an alternative is to the ideal best solution.

A higher TOPSIS score means better overall performance based on the given criteria, weights, and impacts.

The Rank column assigns rank 1 to the best-performing alternative.

From the table:

M5 has the highest TOPSIS score (0.9772) and is ranked 1, making it the most preferred option.

M6 and M3 are ranked 2nd and 3rd, respectively, indicating strong performance.

M2 has the lowest TOPSIS score and is ranked 8, making it the least preferred alternative.

### Result Graph Interpretation

The above bar graph represents the **TOPSIS Score Comparison** among all alternatives (M1–M8).

- The **X-axis** shows the alternatives.
- The **Y-axis** represents the calculated TOPSIS score for each alternative.
- A **higher bar indicates a better-performing alternative** based on the given criteria, weights, and impacts.

From the graph, it is clearly observed that:

- **M5** has the highest TOPSIS score and is therefore ranked **1st**, making it the most preferred alternative.
- **M6** and **M3** follow next, indicating strong performance relative to other alternatives.
- **M2** and **M4** have comparatively lower TOPSIS scores, indicating weaker performance.
- The visual comparison makes it easy to identify the best and worst alternatives without relying only on numerical tables.

This graphical representation helps in **quick decision-making**, improves interpretability, and validates the ranking obtained through the TOPSIS methodology.
