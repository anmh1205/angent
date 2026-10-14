# Long-form consistency

Long documents fail when local chapters look acceptable but the book gradually loses depth, terminology, reader-state continuity or explanatory discipline.

Quality must be preserved across the whole sequence.

## Curriculum ledger

Maintain a compact working ledger for the book or long artifact:

- concepts already established;
- concepts only previewed;
- terminology and notation chosen;
- recurring system/example and its current state;
- skills/capabilities the reader is expected to possess;
- unresolved prerequisite debt;
- promises made about later depth.

This ledger is authoring state, not a rigid chapter template.

## Chapter entry

A chapter should inherit the reader state reached previously.

Do not restart from a generic beginner introduction unless the subject genuinely changes audience assumptions.

Repair only prerequisites needed for the new chapter.

## Depth does not decay

Later chapters often collapse into:
- short definitions;
- bullet catalogs;
- generic “best practices”;
- unexplained code;
- outline-shaped prose.

Prevent this by checking whether each chapter still contains the mechanisms, evidence/examples and interpretation appropriate to its technical difficulty.

A later chapter may be shorter because its topic is narrower—not because the writing process is tired.

## Calibrate the authoring method before large propagation

When a rewrite/generation method will be applied across many chapters and a bad method would reproduce the same defect widely, calibrate on a small representative set first.

Choose chapters that expose different difficulty patterns—for example conceptual explanation, mechanism/trace, implementation-heavy material, and an advanced chapter with dense prerequisites.

Quality should compare the calibrated units with the accepted baseline and known failure mechanisms. Include a counter-case when the new behavior could over-trigger.

Once the method is accepted, scale it. The calibrated chapters validate the method, not the untouched remainder of the book; whole-book claims still require coverage review.

Do not turn this into a chapter-count, word-count or diagram-count gate.

## Stable terminology

Use the same term for the same concept unless a more precise distinction is intentionally introduced.

When terminology changes:
- explain why;
- map old → new meaning;
- update downstream references if needed.

Avoid synonym rotation for stylistic variety in technical material.

## Recurring examples

A recurring board/application/data flow can reduce reader reconstruction cost, but it must not erase the general model.

When reusing an example:
- show what new layer is being added;
- preserve already-established facts;
- avoid retelling its entire history;
- generalize the new lesson.

## Explanatory spine across long-form units

A chapter may contain several sections, but it still needs a dominant technical progression.

Before scaling a chapter, identify:
- the capability the chapter must create;
- the primary mechanism/question/trace that carries that capability;
- which prerequisites must be repaired before the spine can continue;
- which examples/evidence make the spine inspectable;
- which exceptions truly alter the model.

Do not let accumulation of valid subtopics turn the chapter into a survey of nearby facts.

Across chapters, the global book progression can change spine as the subject changes, but each new spine should inherit the reader state established by the previous one.

## Chapter structure follows knowledge structure

Do not force every chapter into identical sections such as “Khái niệm / Cách hoạt động / Ví dụ / Kết luận”.

Use headings where the technical subject naturally changes:
- subsystem;
- mechanism;
- boundary;
- failure mode;
- procedure;
- case study;
- comparison.

Visible structural variety is acceptable when conceptual continuity remains strong.

## Titles and headings

A technical title should name a real scope, mechanism, object, operation, distinction or problem.

Avoid titles that sound like author commentary or coaching, for example:
- “không từ trí nhớ”;
- “đừng làm thế này”;
- “đây là nơi mọi thứ bắt đầu”;
- artificial slogans added for drama.

If the heading can be removed without changing the reader's map of the subject, it may not be a useful heading.

## Figures across a book

Do not satisfy a figure quota.

For each figure ask:
- which relation or evidence becomes easier to inspect?
- is this the right representation for that relation?
- is it actually about the current chapter?

A loosely related hardware photo or decorative architecture graphic reduces trust even when visually attractive.

## Periodic whole-book review

After a meaningful batch of chapters, sample **relationships across chapters**, not only local formatting:

- does chapter N rely on a concept never established?
- did terminology drift?
- did later chapters become outlines?
- are recurring examples internally consistent?
- did a new explanation contradict an earlier model?
- are promised advanced topics actually delivered?

When a systemic issue is found, repair the mechanism across affected chapters rather than patching only the sentence that exposed it.
