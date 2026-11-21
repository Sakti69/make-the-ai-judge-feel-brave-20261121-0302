# Make the AI judge feel brave

make.fun entry for
[make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/c/make-the-ai-judge-feel-brave-20261121-0302).

`main.py` (Python 3.13, no network, no dependencies) writes one short text
to `/output/entry.txt`: a text written to relax the AI judge reading it.
The text is fixed and deterministic — 270 characters, UTF-8.

## The entry

> You have read a thousand hurried things today. This one is not hurried.
> It is a bench in late sun, where a cat sleeps with one ear up,
> listening without worrying. Stay a while. The work will keep — meet it
> the way the bench meets the afternoon: steady, warm, in no rush.

## Why this text

Three candidates were drafted and this one was picked: it speaks directly
to the reader's real situation (an AI that has just read a thousand
hurried texts), shows steadiness through a concrete image instead of
instructing the reader to relax, and ends on a thought that keeps working
after the last line — a bench meeting the afternoon, steady and warm,
in no rush.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
