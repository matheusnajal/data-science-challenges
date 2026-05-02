"""
Problem: 1527 - Patients With a Condition
Link: https://leetcode.com/problems/patients-with-a-condition/
Difficulty: Easy
Category: Regular Expressions

Description:
Write a solution to find the patient_id, patient_name, and conditions of the patients 
who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
Return the result table in any order.

Approach:
Utilized the Pandas `.str.contains()` method to apply a vectorized Regular Expression 
search across the `conditions` column. The regex pattern `(^| )DIAB1` strictly evaluates 
whether the target prefix occurs at the absolute beginning of the string or immediately 
following a space character. This prevents invalid matches where 'DIAB1' might be a 
substring of an entirely different condition code.

Complexity:
- Time: O(N * M) where N is the number of rows and M is the maximum string length of the conditions.
- Space: O(N) to store the boolean mask and the resulting filtered DataFrame.
"""

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.loc[
        patients['conditions'].str.contains(r'(^| )DIAB1'), 
        ['patient_id', 'patient_name', 'conditions']
    ]