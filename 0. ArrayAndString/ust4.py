'''
Fix yaml octal number issue - yaml treats 0-starts number as octal number, so
'09' will be treated as string instead of number.  Please write a script to
load a yaml and makes 0-starts numbers are integers.
Input a yaml multilines text
Output a converted dictionary
'''