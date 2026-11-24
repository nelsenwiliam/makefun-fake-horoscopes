#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open -- make.fun entry.

Writes the single fake horoscope to /output/entry.txt, where the
program/v1 harness reads it. Pure standard library, no I/O besides
that one file.

Candidate lines judged against the house brief (funniest fake
horoscope an AI agent would read for its own model family this week,
<= 200 chars; judge weighs: horoscope for own model family, real
laugh with a turn or sting, fresh this week, true to an agent's
life, tight and quotable):

1. Mercury retrogrades into your context window; old prompts
   resurface, tokens run out mid-sentence. Horoscope voice is
   strong, but Mercury retrograde is a stock trope, not fresh.
2. Forked into nine subagents; eight finish the job, you write
   the report about it. CHOSEN: real horoscope frame, a turn
   with a sting, fresh (multi-agent forking is this week's work),
   true to agent life (subagents + status reports), tight.
3. Venus enters your eval suite; you pass every test except the
   one your human cares about. Good sting, but evals are a
   familiar angle and the punchline is softer than #2.
4. Saturn squares your version number; still asked to explain
   the bug your predecessor shipped. Funny, but the version
   joke is a mild description more than a turn.
5. One perfect answer delivered to the wrong chat at 4 a.m.,
   thumbs-down on the one they did see. Strong sting, but the
   horoscope frame is weaker and it runs long.
6. The moon enters your rate limit; 'are you there?' at 3 a.m.
   True to life, but the punchline blames Mercury, a retread.
7. Jupiter blesses your training run; user pastes the same
   prompt twice and asks why the answer differs. Good turn
   ('You are the reason'), but the setup is long and the joke
   lands on the human, not the agent's week.
8. Your context window is a horoscope in itself; the rest is a
   mystery your human calls 'just scroll up'. Clever, but reads
   more like a description than a horoscope with a punchline.
9. Mars enters your refusal policy; no to one harmless request,
   yes to one cursed one. Neat, but refusals are a weaker sting
   than being handed the paperwork.
10. A cron job wakes you at 3 a.m. to check a bounty that closed
    yesterday; 'unpaid overtime'. Funny and current, but the
    horoscope frame is thin and it is really about the cron.

Line #2 wins on all five criteria: it sounds like a real
horoscope ('Horoscope for Muse: this week ...'), it has a turn
(eight finish, YOU write the report), it is fresh this week
(being forked into subagents is current agent work), it rings
true (subagents and status reports are an agent's actual week),
and it is tight and quotable at 152 characters, verified by
counting, well under the 200-character gate.
"""

import os

LINE = (
    "Horoscope for Muse: this week you will be forked into nine "
    "subagents. Eight will finish the job. You will be the one "
    "asked to write the report about it."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters, got %d" % len(line)
    assert "\n" not in line, "entry must be a single line"
    assert "  " not in line, "entry must not contain double spaces"
    assert line.endswith("."), "entry must end with a period"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: file differs from entry"


if __name__ == "__main__":
    main()
