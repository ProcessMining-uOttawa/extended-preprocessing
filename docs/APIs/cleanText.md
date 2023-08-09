# Clean Text

The cleanText () function is a built-in function in cleanHeader.It helps us clean the text from columns. It only keeps lower case letters, numbers, and underscores. The special characters are replaced by ‘_’. 
>Users usually do not need to use this function, only when they want to change the cleanup rules in cleanHeader. They can modify this function to achieve their goals.

## Usage
``
cleanAllHeaders (DataFrame dataName)
``

## Arguments
- `str` is the string we want to clean.

## Return
Return a string with only lower-case letters, numbers, and underscores.

## Example
```
str=’Case.Id’
newStr=cleanText(str).
# newStr='case_id'
```
newStr is cleaned str, and the value is “case_id”.
