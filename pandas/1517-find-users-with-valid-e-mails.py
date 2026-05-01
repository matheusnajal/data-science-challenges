"""
Problem: 1517 - Find Users With Valid E-Mails
Link: https://leetcode.com/problems/find-users-with-valid-e-mails/
Difficulty: Easy
Category: Regular Expressions

Description:
Write a solution to find the users who have valid emails.
A valid e-mail has a prefix name and a domain where:
- The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
- The domain is '@leetcode.com'.

Approach:
Defined a strict Regular Expression (Regex) pattern to validate the email structure:
- `^[a-zA-Z]`: Ensures the string starts with a letter.
- `[a-zA-Z0-9_.-]*`: Allows zero or more valid characters in the prefix.
- `@leetcode\.com$`: Forces the exact domain match at the end of the string.
The pattern is evaluated using the vectorized `.str.match()` method, generating a boolean 
mask passed into `.loc` to filter the rows efficiently.

Complexity:
- Time: O(N * M), where N is the number of rows and M is the maximum length of the email strings being evaluated by the regex engine.
- Space: O(N) for the allocation of the boolean mask and the resulting DataFrame.
"""

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    padrao_regex = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    
    return users.loc[
        users['mail'].str.match(padrao_regex), 
        ['user_id', 'name', 'mail']
    ]