
# PathMatcher
## Intro
The goal of the Tool to get a list of files from two diffrent Vendors and match them to eliminate duplica and to merge diffrent names from diffrent Vendors  , etc!

## Example Input:

```
list1 = ["electronics/computers/notebook", "electronics/phones/smartphones"]
list2 = ["elec/Computers/laptops", "electronics/phones/mobiles"]
```

## Expected Output:

```
[("electronics/computers/notebook", "elec/Computers/laptops"), 
 ("electronics/phones/smartphones", "electronics/phones/mobiles")]
```

## Getting started 

Python version used 3.12.8

### Install the requirements

```bash
pip install -r requirements.txt 
```

## Authors

- [@3xpp](https://github.com/3xpp)

