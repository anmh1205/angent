# Vietnamese technical language

Compose from the intended proposition and technical relation, not an English sentence skeleton or a stock “technical-document” voice.

## Register

Use calm, direct technical Vietnamese with concrete subjects and verbs.

Rigor comes from precise claims, not bureaucratic or solemn phrasing.

Keep conventional technical terms such as kernel, userspace, driver, filesystem, Device Tree, binding, toolchain, ABI, event loop and exact API identifiers when clearer than forced translations.

## Meaning and cohesion

Preserve cause, condition, contrast, sequence, scope and uncertainty.

Rebuild an unnatural clause rather than translating word-by-word.

Maintain stable referents and real given→new flow across sentences and paragraphs. Adjacent sentences should usually share a visible conceptual relation; do not make every sentence a detached fact.

When a paragraph teaches one mechanism, prefer a continuous explanation over a sequence of mini-declarations separated by author comments.

## Remove meta-commentary, not just phrases

Do not add sentences whose main function is to:

- announce that something is important;
- tell the reader what not to memorize;
- narrate what “we” will or will not learn next;
- praise/summarize the author's own explanation;
- create conversational transitions without technical information.

State the underlying technical relation directly.

Example of the mechanism:

Weak: “Điểm quan trọng là stack pointer phải luôn thỏa căn chỉnh.”

Better: “AAPCS64 yêu cầu SP căn chỉnh 16 byte tại các public interface; vi phạm điều kiện này có thể làm callee hoặc mã sinh bởi compiler truy cập stack sai giả định.”

The lesson is not to ban “Điểm quan trọng là”. It is to replace meta-commentary with the actual rule, reason, or consequence.

## Internal process vocabulary boundary

Do not leak the vocabulary used to manage ANGENT's own work into an unrelated technical document.

Words such as `owner`, `gate`, `baseline`, `artifact state`, `repair target`, `quality floor`, `active obligation` or `calibration` are valid only when the subject itself requires those concepts.

When internal state helped produce a sentence, realize the sentence in the domain's objects, relations and consequences instead of narrating the authoring/reasoning machinery.

## Formal technical writing

Avoid habitual direct-address coaching, fake rhetorical questions and conversational filler.

Do not compensate with administrative nominalization.

Headings name technical scope, operation, distinction or real problem. They are not slogans or author advice.

## Examples and terminology

Explain why a code block, command, diagram or example matters.

A recurring example anchors concepts but does not replace the general model.
