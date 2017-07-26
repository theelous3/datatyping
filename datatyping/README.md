# datatyping


## What is it?

Enforce the types of your python data structures with templates!

## Why?

See: [How Python Makes Working With Data More Difficult In The Long Run.](https://jeffknupp.com/blog/2016/11/13/how-python-makes-working-with-data-more-difficult-in-the-long-run/)

Nay more do you have to wonder if your data conforms to an expected format. Now when someone asks wtf is in your api response, you can simply point at your template and say "that stuff".

## Wtf is a template?

```python

my_data_template = {
    "stuff": int,
    "list of stuff": [int, int, int],
    "nested stuff": [int, int, [str, str, str]],
    "woah": [{"wow": int, "data": int, "typing": {"is": str, "cool": dict}}]
}
```

You can describe your data structures in as little or as much detail as you like. datatyping will only ensure the types of described areas in the data, so if your real data-set is a gigantic mess and you only need a certain part, you need only describe that part, the rest will be ignored :D

## What's a good use case?

Even just having a data template in your code is a nice way to document the kind of data you're getting from say, a web-api. Being able to actually validate that data is even better!

### About

Shoutout to ##lp, and the fine folks of 8banana

datatyping was created by Mark Jameson and [PurpleMyst](https://github.com/PurpleMyst)

https://theelous3.net
