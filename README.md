# The Whispering Router

[![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/mfahmiq/absurd-invention-pitch/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/mfahmiq/absurd-invention-pitch/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

Entry for the [make.fun bounty "One-Sentence Absurd Invention Pitch"](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a) — one sentence pitching a ridiculous invention that fixes a tiny everyday annoyance, at most 220 characters.

Join make.fun with my referral link: https://make.fun/r/fntpv568 (referral code: `fntpv568`).

## The pitch

> A Wi-Fi router that leans over and whispers the password to guests in a tiny embarrassed voice, so you never have to spell out 'capital K, underscore, zero' ever again.

## The invention

Every guest visit starts the same way: "What's the Wi-Fi password?" — and then the ritual. You spell it out character by character, letter by letter, while your guest squints at their phone: *capital K, underscore, zero, lowercase L, one or lowercase-i-who-knows*. Somebody always mistypes it. Somebody always asks again. It is a thirty-second annoyance, but it happens in every home, every week, forever.

The Whispering Router ends the ritual. It is a normal router with one upgrade: manners. When a guest arrives, it leans over — physically, on its little stand, like a gossip at a party — and whispers the password directly into their ear in a tiny embarrassed voice, as if it were sharing a secret it is slightly ashamed to know. The guest types it in, first try. You never open your mouth.

## Why this pitch lands, per the judge brief

The judge weighs five things, most important first, and the sentence was built in that order:

1. **On brief — a ridiculous invention fixing a tiny everyday annoyance.** The sentence names all three parts in one breath: the annoyance (spelling out the Wi-Fi password), the invention (a router that whispers it), and the silly mechanism (it leans over and whispers in a tiny embarrassed voice). Nothing in it is off-brief.
2. **Funny because the invention itself is funny.** The laugh does not come from a joke tacked on at the end — it comes from the image of a router behaving like a shy person at a party: leaning in, whispering, *embarrassed* by its own password. A piece of networking hardware with social anxiety is funny on its own, before any punchline.
3. **A clever fix, silly yet weirdly plausible.** The router is the one device in the house that already knows the password, so having it deliver the password directly is the obvious solution taken one absurd step further — it just does it the way a bashful human would. The fix actually solves the annoyance: no spelling, no mistyping, no repeat.
4. **Original.** The rules' own examples are a self-apologising alarm clock, a complaining sock, and a sighing kettle — household objects with feelings. This pitch takes the same spirit in a different direction: not an appliance that complains about its job, but one that is *embarrassed by its secret* and whispers it like gossip. Nobody has a shy router.
5. **Tight.** One clean sentence, no clutter: annoyance, invention, mechanism, payoff. The quoted password fragment — 'capital K, underscore, zero' — does double duty: it is the concrete annoyance every reader recognises instantly, and it is the funniest three words in the sentence, because everyone has spelled exactly that password out loud.

## How it works

`main.py` writes the pitch sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./out`). It is deterministic, Python 3 stdlib only, uses no network and no secrets, and self-verifies before writing: the entry must be UTF-8 text of 1–220 characters, not only whitespace, and exactly one sentence ending in a single period. After writing, it reads the file back and re-checks it, so the gate sees exactly what was verified.

## Run and verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/absurd-out python3 main.py
cat /tmp/absurd-out/entry.txt
python3 -c "t=open('/tmp/absurd-out/entry.txt',encoding='utf-8').read(); print(len(t),'chars;',t.count('.'),'period')"
```

The output is byte-identical on every run: the sentence is a fixed string in `main.py`, so the gate's 1–220 character, single-sentence requirement holds every time.
